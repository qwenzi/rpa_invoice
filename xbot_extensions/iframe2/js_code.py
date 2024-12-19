
xpathFunc = """
    function $x(xpath, element) {
        
        if (element == null) {
            element = document
        }
        console.log(element)
        let xpathResult = document.evaluate(xpath, element, null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); 
        let nodes = []
        let node = null               
        while (node = xpathResult.iterateNext()) {
            nodes.push(node)
        } 
        return nodes     
    }   
"""


getPath = """
    function getPath(element) {
        const path = [];
        while (element && element.nodeType === Node.ELEMENT_NODE) {
            let index = 0;
            let sibling = element.previousSibling;
            while (sibling) {
                if (sibling.nodeType === Node.ELEMENT_NODE) {
                    index++;
                }
                sibling = sibling.previousSibling;
            }
            const tagName = element.nodeName.toLowerCase();
            const pathIndex = index;
            let required = true;
            if (tagName === 'html' || tagName === 'body') {
                required = false
            }
            path.unshift({
                'name': tagName,
                'type': "web",
                'attributes': [{'name': 'index', 'value': index, 'required': required, 'operator': 'Equal'}]
            });
            element = element.parentNode;
        }
        return path;
    }
"""


getElementByXpath = """
function a(element, xpath) {

    %s     
    %s

    let eles = $x(xpath, element)
    if (eles.length == 1) {
        let path = getPath(eles[0])
        return path
    }
    if (eles.length == 0) {
        return "未找到元素"
    }
    if (eles.length > 1) {
        return "找到多个元素，无法唯一确定"
    }
}
      
""" % (xpathFunc, getPath)





getElementsByXpath = """
function a(element, xpath) {
    %s
    %s
    let eles = $x(xpath, element)
    let paths = []
    for (let ele of eles) {
        let tagName = ele.tagName
        if (tagName == "IFRAME" || tagName === "FRAME") {
            let src = ele.getAttribute("src");
            if (src) {
                if (src.substring(0, 17) == "chrome-extension:") continue
            }
        }
        let path = getPath(ele)
        paths.push(path)
    }
    return paths
}    
""" % (xpathFunc, getPath)

getShadowRootByJsPath = """
function (element, xpath) {    
    %s
    %s
    if (ele == null) {
        return "未找到元素"
    }
    let path = getPath(ele)
    ele = ele.shadowRoot.querySelector("*")
    return [path, ele.tagName]
}
""" % (getPath, 'let ele = %s')


getShadowRootByXpath = """
function (element, xpath) {
    %s
    %s
    let eles = $x(xpath, element)
    if (eles.length == 0) {
        return "未找到元素"
    }
    if (eles.length != 1) {
        return "找到多个元素，无法唯一定位"
    }
    if (eles[0].shadowRoot == null) {
        return "该路径未找到shadowRoot，" + xpath
    }
    let path = getPath(eles[0])
    ele = eles[0].shadowRoot.querySelector("*")
    return [path, ele.tagName]
}
""" % (xpathFunc, getPath)
