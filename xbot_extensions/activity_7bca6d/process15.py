import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        网页对象 = None
        username = ""
        password = ""
        tj_username = ""
        tj_password = ""
        登录的店铺名称 = ""
        是否要退出已登录账号 = False
    else:
        网页对象 = args.get("网页对象", None)
        username = args.get("username", "")
        password = args.get("password", "")
        tj_username = args.get("tj_username", "")
        tj_password = args.get("tj_password", "")
        登录的店铺名称 = args.get("登录的店铺名称", "")
        是否要退出已登录账号 = args.get("是否要退出已登录账号", False)
    try:
        # 2023/04/13 星辰修复除验证码外所有元素
        web_page = xbot_visual.programing.variable(value=lambda: 网页对象
        , _block=("电商罗盘登录", 2, "设置变量"))
        if xbot_visual.workflow.test(operand1=web_page.get_url(), operator="not in", operand2="compass.jinritemai.com/shop", operator_options="{\"ignoreCase\":\"False\"}", _block=("电商罗盘登录", 3, "IF 条件")):
            xbot_visual.web.browser.navigate(browser=web_page, mode="url", url="https://compass.jinritemai.com/login", ignore_cache=False, load_timeout="20", _block=("电商罗盘登录", 4, "跳转至新网址"))
        #endif
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("电商罗盘登录", 6, "等待"))
        if xbot_visual.workflow.test(operand1=是否要退出已登录账号, operator="is true", operand2="", operator_options="{}", _block=("电商罗盘登录", 7, "IF 条件")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("右上角个人店铺名称"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 8, "点击元素(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("退出登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 9, "点击元素(web)"))
        else:
            if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("右上角个人店铺名称"), text="", _block=("电商罗盘登录", 11, "IF 网页包含")):
                xbot_visual.programing.log(type="info", text="当前账号已经登录，不必再重新登录", _block=("电商罗盘登录", 12, "打印日志"))
                return
            #endif
        #endif
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("电商罗盘登录", 16, "等待"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("电商罗盘_我是商家"), _block=("电商罗盘登录", 17, "IF 元素可见(web)")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("电商罗盘_我是商家"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 18, "点击元素(web)"))
        #endif
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("电商罗盘登录", 20, "等待"))
        # 处理点击邮箱登录失败的问题
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("电商罗盘_邮箱登录"), _block=("电商罗盘登录", 22, "IF 元素可见(web)")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("电商罗盘_切换登_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="custom", sudoku_part="MiddleCenter", offset_x="3", offset_y="3", timeout="20", _block=("电商罗盘登录", 23, "点击元素(web)"))
        #endif
        web_wait_result2 = xbot_visual.web.element.wait(browser=web_page, element=package.selector("电商罗盘_邮箱登录"), state="appear", iswait=True, timeout="3", _block=("电商罗盘登录", 25, "等待元素(web)"))
        for loop_index2 in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("电商罗盘登录", 26, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("电商罗盘_发送验证码"), _block=("电商罗盘登录", 27, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("电商罗盘_邮箱登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 28, "点击元素(web)"))
            else:
                break
            #endif
        #endloop
        xbot_visual.web.element.input(browser=web_page, element=package.selector("电商罗盘_账号_输入框"), text=lambda: str(username), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 33, "填写输入框(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("电商罗盘_密码_输入框"), text=lambda: str(password), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 34, "填写输入框(web)"))
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("电商罗盘_复选框_同意协议"), text="", _block=("电商罗盘登录", 35, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("电商罗盘_复选框_同意协议"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 36, "点击元素(web)"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("电商罗盘_登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="2", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 38, "点击元素(web)"))
        # 验证码验证【滑块验证或文字点选验证】
        for loop_index3 in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("电商罗盘登录", 40, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("电商罗盘_背景元素"), _block=("电商罗盘登录", 41, "IF 元素可见(web)")):
                xbot_visual.process.run(process="xbot_extensions.activity_jfbym.dy_slider_captcha", package=__name__, inputs={
                    "web_page": web_page,
                    "engine": "xbot",
                    "background_ele": package.selector("电商罗盘_背景元素"),
                    "slider_ele": package.selector("罗盘-拖拽元素"),
                    "offset": lambda: 0,
                    "token": "",
                    "retry_count": lambda: 5,
                    }, outputs=[
                ], _block=("电商罗盘登录", 42, "抖音滑块验证"))
            else:
                break
            #endif
        #endloop
        # 进行多店铺选择
        if xbot_visual.workflow.test(operand1=登录的店铺名称, operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("电商罗盘登录", 48, "IF 条件")):
            if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("选择店铺_返回"), text="", _block=("电商罗盘登录", 49, "IF 网页包含")):
                店铺名称元素列表 = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="//div[text()='请选择店铺']/following-sibling::div//div[@class='index_introName__2tsRs']", is_related_parent=False, parent=None, operation="element", absolute_url=False, attribute_name=None, timeout="10", output_with_element_count=False, _block=("电商罗盘登录", 50, "获取相似元素列表(web)"))
                for 当前循环的店铺名称 in xbot_visual.workflow.list_iterator(list=店铺名称元素列表, loop_start_index="0", loop_end_index="-1", output_with_index=False, _block=("电商罗盘登录", 51, "ForEach列表循环")):
                    try:
                        if xbot_visual.workflow.test(operand1=当前循环的店铺名称.get_text(), operator="==", operand2=登录的店铺名称, operator_options="{}", _block=("电商罗盘登录", 53, "IF 条件")):
                            xbot_visual.web.element.click(browser=web_page, element=当前循环的店铺名称, simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("电商罗盘登录", 54, "点击元素(web)"))
                        #endif
                    except Exception as exception:
                        exception = xbot_visual.trace(exception)
                        xbot_visual.programing.log(type="info", text=exception, _block=("电商罗盘登录", 57, "打印日志"))
                        continue
                    #endtry
                #endloop
            #endif
        #endif
        xbot_visual.programing.log(type="info", text="抖音罗盘登录成功", _block=("电商罗盘登录", 63, "打印日志"))
    finally:
        args["web_page"] = web_page
