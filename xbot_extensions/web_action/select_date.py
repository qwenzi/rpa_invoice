# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块
import os
import re
from os.path import join, dirname

import xbot
from xbot import print, sleep
from . import package
from .package import variables as glv
from xbot.web import WebBrowser, WebElement
from xbot import logging


tool_code = '''
function main(rootElement) {
    let total = 1
    let $x = (xpath, element) => {
        if (element == null) element = document
        let xpathResult = document.evaluate(xpath, element, null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null);
        let nodes = []
        let node = null
        while (node = xpathResult.iterateNext()) {
            nodes.push(node)
        }
        return nodes
    };


    function init() {
        let elems = $x("//*[@shadow_date]", document)
        for (let elem of elems) {
            elem.removeAttribute("shadow_date");
            elem.removeAttribute("shadow_date_num");
            //elem.style.border = '';
        }
    }

    /**
     * 迭代后代元素
     * @param {*} elem
     * @param {(function(*): (null|undefined))|*} callback
     */
    function traverseDescendants(elem, callback) {
        // if (isExcludeElem(elem)) return;
        callback(elem);
        let eleList = elem.children;
        for (let i = 0; i < eleList.length; i++) {
            traverseDescendants(eleList[i], callback);
        }

    }

    /**
     * 判断是否排除元素
     * @param elem
     * @returns {boolean}
     */
    function isExcludeElem(elem) {
        let tagName = elem.tagName;
        let excludeTagName = ["INPUT", "SVG", "PATH"]
        let isExclude = excludeTagName.includes(tagName);
        if (isExclude) return true;

        return elem.offsetParent === null || // Element is not visible in layout
            getComputedStyle(elem).display === 'none' || // Element is set to display: none
            getComputedStyle(elem).visibility === 'hidden' ||  // Element is set to visibility: hidden
            elem.offsetWidth === 0 ||
            elem.offsetHeight === 0
    }


    /**
     *  获取所有可用元素
     * @returns {*[]}
     */
    window.getShadowDateElems = () => {
        let elems = []
        traverseDescendants(rootElement, function (elem) {
            let size = elem.children.length;
            if (size > 1) return;
            if (size === 1) {
                let tagName = elem.children[0].tagName;
                if (tagName !== 'svg' && tagName !== 'path') return
            }
            processElem(elem);
            elems.push(elem);
        });
        return elems;
    };


    function getYearMonthElem(elem) {
        while (true) {
            if (elem.parentNode === null) return elem;
            if (elem.innerText !== elem.parentNode.innerText) return elem.parentNode;
            elem = elem.parentNode;
        }
    }

    function getMonthElem() {
        let yearElems = $x('.//*[@shadow_date="shadow_year"]', rootElement)
        for (let yearElem of yearElems) {
            let elems = $x('.//following::*[@shadow_date]', yearElem)
            for (let i = 0; i < elems.length; i++) {
                if (/\d{1,2}月*/.test(elems[i].innerText)) {
                    elems[i].setAttribute("shadow_date", "shadow_month");
                    break
                }
            }
        }
        let monthElems = $x('.//*[@shadow_date="shadow_month"]', rootElement)
        return yearElems.length === monthElems.length;
    }

    /**
     * 元素加工
     * @param elem
     */
    function processElem(elem) {
        if (isExcludeElem(elem)) return;
        let text = elem.innerText;
        // elem.style.border = '2px dashed red';
        elem.setAttribute("shadow_date", true)
        elem.setAttribute("shadow_date_num", total)
        if (/\d{4}年*/.test(text)) elem.setAttribute("shadow_date", "shadow_year");
        total += 1;
    }


    window.monitorDropdownBox = (mode='month') => {
        // console.log("monitorDropdownBox");
        if (window.shadowDateObserver) window.shadowDateObserver.disconnect();

        let targetNode = document.body;
        let config = {attributes: true, childList: true, subtree: true};
        let boxElem = null;
        let callback = function (mutationsList, observer) {
            for (let mutation of mutationsList) {
                if (mutation.attributeName === "shadow_date") continue
                if (boxElem === mutation.target) break
                let text = mutation.target.innerText;
                if (mode === "year" && /(\d{4}\D*?){8,}/.test(text)) {
                    if (boxElem !== null) boxElem.removeAttribute("shadow_date");
                    boxElem = mutation.target;
                    boxElem.setAttribute("shadow_date", "shadow_year_box")
                    console.log("shadow_year_box", boxElem)
                    break
                } else if (mode !== "year" && (/(\d{1,2}\D*?){12}/.test(text) || /\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/.test(text))) {
                    if (boxElem !== null) boxElem.removeAttribute("shadow_date");
                    boxElem = mutation.target;
                    boxElem.setAttribute("shadow_date", "shadow_month_box")
                    console.log("shadow_month_box", boxElem)
                    break
                }
            }
        };
        window.shadowDateObserver = new MutationObserver(callback);
        window.shadowDateObserver.observe(targetNode, config);
    };


    /**
     * 运行入口函数
     */
    window.shadowDataRun = () => {
        init();
        let result = {mode: -1, msg: '未解析到年元素, 请检查日期框元素是否包含了年月日元素'};
        window.getShadowDateElems();
        let yearElems = $x('.//*[@shadow_date="shadow_year"]', rootElement)

        let yearTotal = yearElems.length;
        if (yearTotal === 0) return result;

        result.msg = "解析的年月数量不一致";
        if (!getMonthElem()) return result;


        result.msg = "解析到多个年月元素"
        if (yearTotal > 2) return result;


        // 解析向前按钮
        let preBtnElems = $x('./preceding::*[@shadow_date and .=""]', yearElems[0])
        let preNextElems = $x('./following::*[@shadow_date and .=""]', yearElems[yearTotal - 1])
        console.log("btnElems", preBtnElems)
        console.log(preNextElems, "btnElems")


        if (preBtnElems.length < 1 || preNextElems.length < 1) {
            result.mode = 2 + yearTotal;
            result.msg = "无切换按钮"
            return result
        }

        result.mode = -1;
        result.msg = "解析切换年月按钮失败"
        preBtnElems[0].setAttribute("shadow_date", "shadow_pre_year")
        console.log("shadow_pre_year", preBtnElems[0])
        preBtnElems[preBtnElems.length - 1].setAttribute("shadow_date","shadow_pre_month")
        console.log("shadow_pre_month", preBtnElems[preBtnElems.length - 1])
        getYearMonthElem(yearElems[0]).setAttribute("shadow_date","shadow_year_month")

        // 解析向后按钮
        preNextElems[0].setAttribute("shadow_date","shadow_next_month")
        console.log("shadow_next_month", preNextElems[0])
        preNextElems[preNextElems.length - 1].setAttribute("shadow_date", "shadow_next_year")
        console.log("shadow_next_year", preNextElems[preNextElems.length - 1])
        getYearMonthElem(yearElems[yearTotal - 1]).setAttribute("shadow_date", "shadow_year_month")


        result.mode = yearTotal;
        result.msg = ""
        return result;


    };
}
'''

def select_date(web_page: WebBrowser, elem: WebElement, date_start: str, date_end: str):
    def click(elem):
        elem.execute_javascript('''
        function (element) {
            let config = {view: window, bubbles: true, cancelable: true}
            events = ['pointermove', 'mousemove', 'focus', 'pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']
            for (var i = 0; i < events.length; i++) {
                element.dispatchEvent(new MouseEvent(events[i], config));
            }
        }
    ''')


    def disconnect_monitor(elem):
        elem.execute_javascript('''
        function (ele, _) {
            if (window.shadowDateObserver) window.shadowDateObserver.disconnect();
        }
        ''')


    def monitor_dropdown_box(elem, mode=None):
        elem.execute_javascript('''function (ele, mode) { window.monitorDropdownBox(mode); }''', mode)


    assert any([date_start, date_end]), "开始日期和结束日期不能同时为空"
    date_list = [date_start, date_end]

    if not isinstance(elem, WebElement): elem = web_page.find(elem)
    elem.execute_javascript(tool_code)

    data = elem.execute_javascript(''' function (element, input) { return window.shadowDataRun() }''')
    logging.debug(data)
    mode = data["mode"]
    msg = data["msg"]

    assert 0 < mode < 5, msg
    month_list = [None, "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if mode == 1 or mode == 2:
        if mode == 1: assert bool(date_start) , "在单日期选择下，开始日期不能为空"
        
        shadow_year_months = elem.find_all_by_xpath('.//*[@shadow_date="shadow_year_month"]', timeout=1)
        assert len(shadow_year_months) == mode, "年月元素数量与识别的不一致， {}".format(len(shadow_year_months))
        shadow_pre_year = elem.find_by_xpath('.//*[@shadow_date="shadow_pre_year"]', timeout=1)
        shadow_pre_month = elem.find_by_xpath('.//*[@shadow_date="shadow_pre_month"]', timeout=1)
        shadow_next_month = elem.find_by_xpath('.//*[@shadow_date="shadow_next_month"]', timeout=1)
        shadow_next_year = elem.find_by_xpath('.//*[@shadow_date="shadow_next_year"]', timeout=1)

        for i, shadow_year_month in enumerate(shadow_year_months):
            data_text = date_list[i]
            if not bool(data_text): continue
            year, month, day = data_text.split("-")
            day = int(day)
            now_date_list = []
            # 选择年月
            while True:
                now_date = shadow_year_month.get_text()
                if now_date in now_date_list: raise Exception("切换年月失败")
                now_date_list.append(now_date)
                # logging.debug(f"target_date: {data_text} - now_date: {now_date}")
                
                now_year = re.search(r"\d{4}", now_date).group()
                now_date = re.sub(r"\d{4}", "", now_date)
                now_month = re.search(r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|\d{1,2})", now_date).group()
                if now_month in month_list: now_month = month_list.index(now_month)
 

                offset_y, offset_m = int(year) - int(now_year), int(month) - int(now_month)

                if offset_y > 0: click(shadow_next_year)
                if offset_y < 0: click(shadow_pre_year)
                if offset_y != 0: continue
                if offset_m > 0: click(shadow_next_month)
                if offset_m < 0: click(shadow_pre_month)
                if offset_m == 0: break

            # 选择日
            elem.execute_javascript('''
            function (element, input) {
                window.getShadowDateElems()
            }            
            ''')
            axes = "preceding" if mode == 2 and i == 0 else "following"
            xpath = '(./{}::*[.={} and @shadow_date])[.>15 and position()=last() or .<16 and position()=1]'.format(axes, day)
            # 重新标记
            shadow_year_months[-1].find_by_xpath(xpath, timeout=1).click(delay_after=0.3)
    else:
        try:
            shadow_years = elem.find_all_by_xpath('.//*[@shadow_date="shadow_year"]', timeout=1)
            shadow_months = elem.find_all_by_xpath('.//*[@shadow_date="shadow_month"]', timeout=1)
            for i, shadow_year in enumerate(shadow_years):
                data_text = date_list[i]
                year, month, day = data_text.split("-")
                month = int(month)
                day = int(day)
                shadow_month = shadow_months[i]

                elem.execute_javascript('''function (ele, _) { window.monitorDropdownBox("year"); }''')
                monitor_dropdown_box(elem, "year")
                click(shadow_year)
                disconnect_monitor(elem)
                shadow_year_box = elem.find_by_xpath('//*[@shadow_date="shadow_year_box"]', timeout=1)
                shadow_year_box.find_by_xpath('.//*[contains(text(), "{}")]'.format(year)).click(delay_after=0.3)

                elem.execute_javascript('''function (ele, _) { window.monitorDropdownBox(); }''')
                click(shadow_month)
                disconnect_monitor(elem)
                shadow_month_box = elem.find_by_xpath('//*[@shadow_date="shadow_month_box"]', timeout=1)

                en_month = month_list[month]
                shadow_month_box.find_by_xpath('(.//*[contains(text(), "{}") or text()="{}"])[1]'.format(month, en_month), timeout=1).click(delay_after=0.3)
                
            # 选择日
            # 重新标记
            elem.execute_javascript('''
            function (element, input) {
                window.getShadowDateElems()
            }            
            ''')
            axes = "preceding" if mode == 2 and i == 0 else "following"
            xpath = '(./{}::*[.={} and @shadow_date])[.>15 and position()=last() or .<16 and position()=1]'.format(axes, day)

            shadow_years[-1].find_by_xpath(xpath, timeout=1).click(delay_after=0.3)
        finally:
            disconnect_monitor(elem)


def main(args):
    web_page = args.get("web_page")
    elem = args.get("date_elem")
    date_start = args.get("date_start")
    date_end = args.get("date_end")
    
    select_date(web_page, elem, date_start, date_end)
    
