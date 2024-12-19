import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        账号 = ""
        密码 = ""
        重试次数 = "3"
        浏览器类型 = "chrome"
    else:
        账号 = args.get("账号", "")
        密码 = args.get("密码", "")
        重试次数 = args.get("重试次数", "3")
        浏览器类型 = args.get("浏览器类型", "chrome")
    try:
        web_page = xbot_visual.programing.variable(value="https://loginmyseller.taobao.com"
        , _block=("千牛登录", 1, "设置变量"))
        if xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="chrome", operator_options="{}", _block=("千牛登录", 2, "IF 条件")):
            web_page = xbot_visual.web.create(web_type="chrome", value="https://loginmyseller.taobao.com", silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("千牛登录", 3, "打开网页"))
        else:
            web_page = xbot_visual.web.create(web_type="edge", value="https://loginmyseller.taobao.com", silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("千牛登录", 5, "打开网页"))
        #endif
        xbot_visual.win32.manual_motion_on(motion_move=True, motion_click=True, motion_delay=False, min_time="1", max_time="3", _block=("千牛登录", 7, "开启模拟真人操作"))
        xbot_visual.web.element.hover(browser=web_page, element=package.selector("qn_uername_input"), simulate=True, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("千牛登录", 8, "鼠标悬停在元素上(web)"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="click", hardware_driver_click=False, keys="null", delay_after="1", _block=("千牛登录", 9, "鼠标点击"))
        xbot_visual.win32.send_keys(keys=账号, hardware_driver_input=False, force_ime_eng=True, contains_hotkey=False, send_key_delay="50", delay_after="1", _block=("千牛登录", 10, "键盘输入"))
        # web.element.input
        # web.element.input_password
        xbot_visual.web.element.hover(browser=web_page, element=package.selector("密码输入框"), simulate=True, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("千牛登录", 13, "鼠标悬停在元素上(web)"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="click", hardware_driver_click=False, keys="null", delay_after="1", _block=("千牛登录", 14, "鼠标点击"))
        xbot_visual.win32.send_keys(keys=密码, hardware_driver_input=False, force_ime_eng=True, contains_hotkey=False, send_key_delay="50", delay_after="1", _block=("千牛登录", 15, "键盘输入"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop=重试次数, step="1", _block=("千牛登录", 16, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("qn_login_verify"), _block=("千牛登录", 17, "IF 元素可见(web)")):
                _ = xbot_visual.process.run(process="process11", package=__name__, inputs={
                    "web_page": lambda: web_page,
                    "drag_start_element": package.selector("qn_slide"),
                    "background_element": package.selector("qn_login_verify"),
                    }, outputs=[
                ], _block=("千牛登录", 18, "调用流程"))
            else:
                break
            #endif
        #endloop
        xbot_visual.web.element.click(browser=web_page, element=package.selector("qn_login"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("千牛登录", 23, "点击元素(web)"))
        xbot_visual.win32.manual_motion_off(_block=("千牛登录", 24, "结束模拟真人操作"))
    finally:
        pass
