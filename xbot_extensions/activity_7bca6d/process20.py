import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        浏览器类型 = ""
        登录账号 = ""
        登录密码 = ""
        百度OCR账号 = ""
        百度OCR密码 = ""
        重试次数 = 5
    else:
        浏览器类型 = args.get("浏览器类型", "")
        登录账号 = args.get("登录账号", "")
        登录密码 = args.get("登录密码", "")
        百度OCR账号 = args.get("百度OCR账号", "")
        百度OCR密码 = args.get("百度OCR密码", "")
        重试次数 = args.get("重试次数", 5)
    try:
        # 目前版本仅支持chrome浏览器
        # 登录逻辑: 先尝试手动登录, 然后利用设置元素值, 键盘输入回车绕过去
        web_page = xbot_visual.programing.variable(value=lambda: None
        , _block=("支付宝登录", 3, "设置变量"))
        if xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="chrome", operator_options="{}", _block=("支付宝登录", 4, "IF 条件")):
            web_page = xbot_visual.web.create(web_type="chrome", value="https://auth.alipay.com/login/index.htm", silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("支付宝登录", 5, "打开网页"))
        elif xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="cef", operator_options="{}", _block=("支付宝登录", 6, "Else IF")):
            web_page = xbot_visual.web.create(web_type="cef", value="https://auth.alipay.com/login/index.htm", silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("支付宝登录", 7, "打开网页"))
        elif xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="edge", operator_options="{}", _block=("支付宝登录", 8, "Else IF")):
            web_page = xbot_visual.web.create(web_type="edge", value="https://auth.alipay.com/login/index.htm", silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("支付宝登录", 9, "打开网页"))
        elif xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="firefox", operator_options="{}", _block=("支付宝登录", 10, "Else IF")):
            web_page = xbot_visual.web.create(web_type="firefox", value="https://auth.alipay.com/login/index.htm", silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("支付宝登录", 11, "打开网页"))
        elif xbot_visual.workflow.test(operand1=浏览器类型, operator="==", operand2="360se", operator_options="{}", _block=("支付宝登录", 12, "Else IF")):
            web_page = xbot_visual.web.create(web_type="360se", value="https://auth.alipay.com/login/index.htm", silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("支付宝登录", 13, "打开网页"))
        #endif
        # 第一次登录
        xbot_visual.web.element.click(browser=web_page, element=package.selector("列表项目_账密登录"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 16, "点击元素(web)"))
        web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("支付宝账号输入框"), state="appear", iswait=True, timeout="20", _block=("支付宝登录", 17, "等待元素(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("支付宝账号输入框"), text=登录账号, append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 18, "填写输入框(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝密码输入框"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 19, "点击元素(web)"))
        xbot_visual.win32.manual_motion_on(motion_move=True, motion_click=True, motion_delay=True, min_time="1", max_time="3", _block=("支付宝登录", 20, "开启模拟真人操作"))
        xbot_visual.web.element.input_password(browser=web_page, element=package.selector("支付宝密码输入框"), text=xbot_visual.decrypt(登录密码), simulate=True, save_to_clipboard=False, input_type="simulate", force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", timeout="20", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", _block=("支付宝登录", 21, "填写密码框(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝_登录_按钮2"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 22, "点击元素(web)"))
        xbot_visual.win32.manual_motion_off(_block=("支付宝登录", 23, "结束模拟真人操作"))
        # 循环登录处理异常
        web_page = xbot_visual.process.run(process="xbot_extensions.web_action.process8", package=__name__, inputs={
            "网页对象": web_page,
            }, outputs=[
            "web_page",
        ], _block=("支付宝登录", 25, "获取当前激活的网页对象"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop=重试次数, step="1", _block=("支付宝登录", 26, "For次数循环")):
            xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("支付宝登录", 27, "等待"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("账号名或密码不对"), _block=("支付宝登录", 28, "IF 元素可见(web)")):
                raise Exception("登录名或密码不对，请核对后登录")
            #endif
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("行内元素_登录失败，你可以尝试使用扫码登..."), _block=("支付宝登录", 31, "IF 元素可见(web)")):
                # 通过设置元素值, 键入回车绕过去
                xbot_visual.programing.sleep(random_number=True, seconds="1", start_number="1", stop_number="10", _block=("支付宝登录", 33, "等待"))
                xbot_visual.web.element.set_value(browser=web_page, element=package.selector("支付宝_密码_输入框"), value=登录密码, timeout="20", _block=("支付宝登录", 34, "设置元素值(web)"))
                _ = xbot_visual.process.run(process="process19", package=__name__, inputs={
                    "web_page": web_page,
                    "百度OCR账号": "",
                    "百度OCR密码": "",
                    }, outputs=[
                ], _block=("支付宝登录", 35, "调用流程"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝_密码_输入框"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 36, "点击元素(web)"))
                xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("支付宝登录", 37, "键盘输入"))
            else:
                # 存在失败但是没有显示字样, 需要继续登录
                xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("支付宝登录", 40, "等待"))
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("支付宝_密码_输入框"), _block=("支付宝登录", 41, "IF 元素可见(web)")):
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝_切换登录_账密登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 42, "点击元素(web)"))
                    xbot_visual.web.element.input(browser=web_page, element=package.selector("支付宝账号输入框"), text=登录账号, append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录", 43, "填写输入框(web)"))
                    xbot_visual.web.element.set_value(browser=web_page, element=package.selector("支付宝_密码_输入框"), value=登录密码, timeout="20", _block=("支付宝登录", 44, "设置元素值(web)"))
                    _ = xbot_visual.process.run(process="process19", package=__name__, inputs={
                        "web_page": web_page,
                        "百度OCR账号": "",
                        "百度OCR密码": "",
                        }, outputs=[
                    ], _block=("支付宝登录", 45, "调用流程"))
                    xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("支付宝登录", 46, "键盘输入"))
                else:
                    break
                #endif
            #endif
        #endloop
        # 异常处理部分
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("验证码"), _block=("支付宝登录", 53, "IF 元素可见(web)")):
            raise Exception("验证码未通过，请自行登录")
        #endif
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("块元素_为确保你的账户资金安全，需要验..."), _block=("支付宝登录", 56, "IF 元素可见(web)")):
            raise Exception("需手机短信验证，请自行登录")
        #endif
    finally:
        args["web_page"] = web_page
