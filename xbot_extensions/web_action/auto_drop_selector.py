# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep, web
from .import package
from .package import variables as glv



add_ob_js_code = """
function(ele, args) {
    let obj = JSON.parse(args);
    let text = obj["text"]
    console.log(text);
    const xobt_observed_elements = [];
    window.xobt_observed_elements = xobt_observed_elements;

    function areChildrenTextEmpty(node) {
        const flag = []
        for (var i = 0; i < node.childNodes.length; i++) {
            var child = node.childNodes[i];
            flag.push(child.textContent.trim() === ''); 
        }
        // 如果所有子元素文本都为空，则返回true

        return Array.from(flag).some(element => element === true);
    }

    const observer = new MutationObserver((mutationsList, observer) => {
        
        for (let mutation of mutationsList) {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === Node.ELEMENT_NODE && node.textContent.trim() !== '') {
                        Array.from(node.querySelectorAll('*')).forEach(child => {

                            if (child.textContent.trim() === text && child.children.length === 0) {
                                console.log("新增节点-变化元素文本", child.textContent, child.children.length);

                                // child.style.border = '2px solid red';
                                // child.style.color = 'red';
                                xobt_observed_elements.push(child);
                            }
                        });
                    }
                });
            }
            else if (mutation.type === 'attributes' && (mutation.attributeName === 'style' || mutation.attributeName === 'class' ) ) {
                Array.from(mutation.target.querySelectorAll('*')).forEach(child => {
                    // console.log(child.textContent.trim());
                    // console.log(child);
                    const text_flag = child.textContent.trim() === text;
                    const children_cout_flag = child.children.length === 0;
                    let children_empty_text_flag = false;
                    if (child.children.length != 0 && areChildrenTextEmpty(child)) {
                        children_empty_text_flag = true;
                    }

                    if (text_flag) {
                        console.log(child);
                        console.log(areChildrenTextEmpty(child));
                        console.log(text_flag ,children_cout_flag, children_empty_text_flag);

                    }
                    
                    if (text_flag && (children_cout_flag || children_empty_text_flag)) {
                        console.log(child);
                        console.log("属性变化-变化元素文本", child.textContent, child.children.length);
                        // child.style.border = '2px solid red';
                        // child.style.color = 'red';
                        xobt_observed_elements.push(child);

                    }
                });
            }
        }
    });

    window.xbot_observer = observer;

    observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['style', 'class']
    });
}"""

remove_ob_js_code = """
function(ele, args) {
    window.xbot_observer.disconnect();
}"""

click_js_code = """
function(ele, args) {
    let obj = JSON.parse(args);
    console.log(obj);
    let click_flag = obj["click_flag"];
    function getCSSPath(element) {
        if (element === document.body)
            return element.tagName.toLowerCase();

        var ix = 0;
        var siblings = element.parentNode.children;
        for (var i = 0; i < siblings.length; i++) {
            var sibling = siblings[i];
            if (sibling === element)
                return getCSSPath(element.parentNode) + '>' + element.tagName.toLowerCase() + ':nth-child(' + (i + 1) + ')';
        }
    }
    let uniqueObservedElements = new Set(window.xobt_observed_elements);
    uniqueObservedElements = Array.from(uniqueObservedElements);

    if ( click_flag ) {
        uniqueObservedElements[0].click();
    }
    console.log(getCSSPath(uniqueObservedElements[0]));
    return getCSSPath(uniqueObservedElements[0]);
}"""

def set_dropdown(web_page: web.WebBrowser, target_text, drop_ele, click_flag=True, simulative=True) -> str:
    click_flag = "true" if click_flag else "false"
    web_page.execute_javascript(add_ob_js_code, f'{{"text":"{target_text}"}}')
    if isinstance(drop_ele, xbot.web.WebElement):
        drop_ele.click(simulative=simulative)
    else:
        web_page.find(drop_ele).click(simulative=simulative)
    css_path = web_page.execute_javascript(click_js_code, f'{{"click_flag": {click_flag}}}')
    web_page.execute_javascript(remove_ob_js_code)
    return css_path

def main(args):

    web_page = args.get("web_page")
    drop_ele = args.get("drop_ele")
    click_flag = args.get("click_flag")
    target_text = args.get("target_text")
    simulative = args.get("simulative")
    css_path = set_dropdown(web_page, target_text, drop_ele, click_flag, simulative)
    args["css_path"] = css_path
    sleep(1)
