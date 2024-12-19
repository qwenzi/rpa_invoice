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
        web_page = None
        if xbot_visual.workflow.test(operand1=web_type, operator="==", operand2="0", operator_options="{}", _block=("巨量登录", 2, "IF 条件")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="url", value="https://business.oceanengine.com/login?appKey=0", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://business.oceanengine.com/login?appKey=0", _block=("巨量登录", 3, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第3条指令: {e}')
                time.sleep(3)
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("巨量登录", 4, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第4条指令: {e}')
                time.sleep(3)
        else:
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="url", value="https://business.oceanengine.com/login?appKey=0", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://business.oceanengine.com/login?appKey=0", _block=("巨量登录", 6, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第6条指令: {e}')
                time.sleep(3)
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("巨量登录", 7, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第7条指令: {e}')
                time.sleep(3)
        #endif
        xbot_visual.web.element.input(browser=web_page, element=package.selector("巨量引擎_邮箱_输入框"), text=lambda: str(username), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量登录", 9, "填写输入框(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("巨量引擎_密码_输入框"), text=lambda: str(password), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量登录", 10, "填写输入框(web)"))
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("巨量引擎_已阅读并同意 服务协议 勾选状态"), text="", _block=("巨量登录", 11, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("巨量引擎_已阅读并同意 服务协议 勾选状态"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量登录", 12, "点击元素(web)"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("巨量引擎_登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("巨量登录", 14, "点击元素(web)"))
        # 验证码验证【滑块验证或文字点选验证】
        _ = xbot_visual.process.run(process="process48", package=__name__, inputs={
            "web_page": web_page,
            "验证码失败最大重试次数": "5",
            }, outputs=[
        ], _block=("巨量登录", 16, "调用流程"))
        # web.element.wait
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
