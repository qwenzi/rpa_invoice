import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    网页对象 = None
    if args is None:
        浏览器类型 = ""
        账号 = ""
        密码 = ""
        识别引擎 = "云码引擎(付费增值服务)"
    else:
        浏览器类型 = args.get("浏览器类型", "")
        账号 = args.get("账号", "")
        密码 = args.get("密码", "")
        识别引擎 = args.get("识别引擎", "云码引擎(付费增值服务)")
    try:
        if xbot_visual.workflow.multiconditional_judgment(relation="or", conditionals=[{"operand1": 账号.strip(),"operand2": "","operator": "is empty"},{"operand1": 密码.strip(),"operand2": "","operator": "is empty"}], _block=("拼多多登录", 1, "IF 多条件")):
            raise Exception("拼多多账号、密码均不能为空")
        #endif
        pdd_login_url = xbot_visual.programing.variable(value="https://mms.pinduoduo.com/login/"
        , _block=("拼多多登录", 4, "设置变量"))
        web_page = xbot_visual.process.invoke_module(module="utils", package=__name__, function="sdk_create_web_page", params={
            "url": pdd_login_url,
            "mode": 浏览器类型,
            "load_timeout": lambda: 30,
            "stop_if_timeout": False,
        }, _block=("拼多多登录", 5, "调用模块"))
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多登录", 6, "等待"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("拼多多登录", 7, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 8, "IF 元素可见(web)")):
                break
            #endif
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "",
                "background_ele": package.selector("拼多多-验证码-背景"),
                "slider_ele": package.selector("拼多多-验证码-拖拽滑块"),
                "ym_token": "",
                "retry_count": lambda: 5,
                "offset": lambda: 0,
                "speed": lambda: 1,
                }, outputs=[
            ], _block=("拼多多登录", 11, "通用单图滑块验证"))
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多登录", 12, "等待"))
        #endloop
        if xbot_visual.workflow.test(operand1=lambda: loop_index, operator="==", operand2="5", operator_options="{}", _block=("拼多多登录", 14, "IF 条件")):
            xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("拼多多登录", 15, "等待"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 16, "IF 元素可见(web)")):
                raise Exception("拼多多登录失败")
            #endif
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("拼多多_登录页_账户登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 20, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多登录", 21, "等待"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("拼多多登录", 22, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 23, "IF 元素可见(web)")):
                break
            #endif
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "xbot",
                "background_ele": package.selector("拼多多-验证码-背景"),
                "slider_ele": package.selector("拼多多-验证码-拖拽滑块"),
                "ym_token": "",
                "retry_count": lambda: 5,
                "offset": lambda: 0,
                "speed": lambda: 1,
                }, outputs=[
            ], _block=("拼多多登录", 26, "通用单图滑块验证"))
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多登录", 27, "等待"))
        #endloop
        if xbot_visual.workflow.test(operand1=lambda: loop_index, operator="==", operand2="5", operator_options="{}", _block=("拼多多登录", 29, "IF 条件")):
            xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("拼多多登录", 30, "等待"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 31, "IF 元素可见(web)")):
                raise Exception("拼多多登录失败")
            #endif
        #endif
        # 临时修改, 兼容虚拟机剪切板算法异常的bug; bug修复后, 恢复默认
        xbot_visual.web.element.click(browser=web_page, element=package.selector("拼多多_登录页_账号输入框"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 36, "点击元素(web)"))
        xbot_visual.win32.clipboard_set_text(text=账号, _block=("拼多多登录", 37, "设置剪切板内容"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("拼多多_登录页_账号输入框"), text="^{a}^{v}", append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=True, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 38, "填写输入框(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("拼多多_登录页_密码输入框"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 39, "点击元素(web)"))
        xbot_visual.win32.clipboard_set_text(text=密码, _block=("拼多多登录", 40, "设置剪切板内容"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("拼多多_登录页_密码输入框"), text="^{a}^{v}", append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=True, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 41, "填写输入框(web)"))
        xbot_visual.win32.clipboard_clear(_block=("拼多多登录", 42, "清空剪切板"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("拼多多_登录页_登录按钮"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="3", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("拼多多登录", 43, "点击元素(web)"))
        # 添加验证码验证
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("拼多多登录", 45, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 46, "IF 元素可见(web)")):
                break
            #endif
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "",
                "background_ele": package.selector("拼多多-验证码-背景"),
                "slider_ele": package.selector("拼多多-验证码-拖拽滑块"),
                "ym_token": "",
                "retry_count": lambda: 5,
                "offset": lambda: 0,
                "speed": lambda: 1,
                }, outputs=[
            ], _block=("拼多多登录", 49, "通用单图滑块验证"))
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多登录", 50, "等待"))
        #endloop
        if xbot_visual.workflow.test(operand1=lambda: loop_index, operator="==", operand2="5", operator_options="{}", _block=("拼多多登录", 52, "IF 条件")):
            xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("拼多多登录", 53, "等待"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("拼多多-验证码-背景"), _block=("拼多多登录", 54, "IF 元素可见(web)")):
                raise Exception("拼多多登录失败")
            #endif
        #endif
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("拼多多_登录页_未登录原因"), text="", _block=("拼多多登录", 58, "IF 网页包含")):
            未登录原因_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("拼多多_登录页_未登录原因"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("拼多多登录", 59, "获取元素信息(web)"))
            raise Exception(未登录原因_attribute)
        #endif
        web_url = xbot_visual.process.invoke_module(module="utils", package=__name__, function="get_web_url", params={
            "mode": 浏览器类型,
            "load_timeout": lambda: 30,
            "stop_if_timeout": False,
        }, _block=("拼多多登录", 62, "调用模块"))
        if xbot_visual.workflow.test(operand1=web_url, operator="in", operand2="login", operator_options="{\"ignoreCase\":\"False\"}", _block=("拼多多登录", 63, "IF 条件")):
            raise Exception("当前拼多多账号未成功登录，原因未知。")
        #endif
        网页对象 = xbot_visual.programing.variable(value=lambda: web_page
        , _block=("拼多多登录", 66, "设置变量"))
    finally:
        args["网页对象"] = 网页对象
