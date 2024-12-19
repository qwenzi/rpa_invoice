import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        username = ""
        password = ""
        tj_username = ""
        tj_password = ""
        web_type = ""
    else:
        username = args.get("username", "")
        password = args.get("password", "")
        tj_username = args.get("tj_username", "")
        tj_password = args.get("tj_password", "")
        web_type = args.get("web_type", "")
    try:
        browser_type = web_type
        process_result = xbot_visual.process.run(process="process36", package=__name__, inputs={
            "browser_type": browser_type,
            }, outputs=[
            "有打开的网页",
            "当前是登录页",
        ], _block=("巨量纵横登录", 2, "调用流程"))
        # 开始登录
        登录页url = "https://business.oceanengine.com/login?appKey=51"
        web_page = None
        if xbot_visual.workflow.test(operand1=process_result.有打开的网页, operator="is false", operand2="", operator_options="{}", _block=("巨量纵横登录", 6, "IF 条件")):
            web_page = xbot_visual.process.invoke_module(module="utils_douyin", package=__name__, function="open_webpage", params={
                "url": 登录页url,
                "browser_type": browser_type,
                "load_timeout": "20",
                "stop_if_timeout": False,
            }, _block=("巨量纵横登录", 7, "调用模块"))
        else:
            web_page = xbot_visual.process.invoke_module(module="utils_douyin", package=__name__, function="get_webpage", params={
                "browser_type": browser_type,
                "match_type": "3",
                "title": "",
                "url": "",
                "use_wildcard": "",
            }, _block=("巨量纵横登录", 9, "调用模块"))
            url = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("巨量纵横登录", 10, "获取网页信息"))
            if xbot_visual.workflow.test(operand1=url, operator="not in", operand2=登录页url, operator_options="{\"ignoreCase\":\"True\"}", _block=("巨量纵横登录", 11, "IF 条件")):
                web_page = xbot_visual.process.invoke_module(module="utils_douyin", package=__name__, function="open_webpage", params={
                    "url": 登录页url,
                    "browser_type": browser_type,
                    "load_timeout": "20",
                    "stop_if_timeout": False,
                }, _block=("巨量纵横登录", 12, "调用模块"))
            #endif
        #endif
        # programing.comment
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("巨量纵横登录", 16, "等待"))
        # 执行登录
        xbot_visual.web.element.click(browser=web_page, element=package.selector("巨量纵横_切换账号"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量纵横登录", 18, "点击元素(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("巨量纵横_账号_输入框"), text=lambda: str(username), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量纵横登录", 19, "填写输入框(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("巨量纵横_密码_输入框"), text=lambda: str(password), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量纵横登录", 20, "填写输入框(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("巨量纵横_同意协议"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="0.3", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量纵横登录", 21, "点击元素(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("纵横按钮_登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量纵横登录", 22, "点击元素(web)"))
        # 验证码验证【滑块验证或文字点选验证】
        _ = xbot_visual.process.run(process="process48", package=__name__, inputs={
            "web_page": web_page,
            "验证码失败最大重试次数": "5",
            }, outputs=[
        ], _block=("巨量纵横登录", 24, "调用流程"))
        # web.element.wait
        # workflow.if
        # process.return
        # workflow.endif
        # programing.variable
        # workflow.infinite_loop
        # web.browser.element_display
        # workflow.break
        # workflow.endif
        # workflow.if
        # workflow.break
        # workflow.endif
        # web.element.get_element
        # web.element.get_element
        # web.element.get_element
        # process.run
        # process.run
        # programing.variable
        # programing.sleep
        # workflow.endloop
    finally:
        args["web_page"] = web_page
