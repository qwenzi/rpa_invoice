import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        userid = ""
        password = ""
        mode = "chrome"
        path_to_chrome_exe = ""
        加载超时时间 = "20"
        ym_token = ""
        是否退出已登录 = True
        重试次数 = 5
    else:
        userid = args.get("userid", "")
        password = args.get("password", "")
        mode = args.get("mode", "chrome")
        path_to_chrome_exe = args.get("path_to_chrome_exe", "")
        加载超时时间 = args.get("加载超时时间", "20")
        ym_token = args.get("ym_token", "")
        是否退出已登录 = args.get("是否退出已登录", True)
        重试次数 = args.get("重试次数", 5)
    try:
        if xbot_visual.workflow.test(operand1=lambda: type(userid), operator="!=", operand2=lambda: str, operator_options="{}", _block=("淘宝登录", 1, "IF 条件")):
            raise Exception("登录账号类型错误，应为字符串类型")
        #endif
        if xbot_visual.workflow.test(operand1=lambda: type(password), operator="!=", operand2=lambda: str, operator_options="{}", _block=("淘宝登录", 4, "IF 条件")):
            raise Exception("登录密码类型错误，应为字符串类型")
        #endif
        if xbot_visual.workflow.test(operand1=lambda: bool(加载超时时间), operator="is true", operand2="", operator_options="{}", _block=("淘宝登录", 7, "IF 条件")):
            加载超时时间 = xbot_visual.programing.variable(value=lambda: int(加载超时时间)
            , _block=("淘宝登录", 8, "设置变量"))
        else:
            加载超时时间 = xbot_visual.programing.variable(value=lambda: 20
            , _block=("淘宝登录", 10, "设置变量"))
        #endif
        淘宝网址 = xbot_visual.programing.variable(value=lambda: None
        , _block=("淘宝登录", 12, "设置变量"))
        是否新打开 = xbot_visual.programing.variable(value=False
        , _block=("淘宝登录", 13, "设置变量"))
        if xbot_visual.workflow.test(operand1=mode, operator="==", operand2="chrome", operator_options="{}", _block=("淘宝登录", 14, "IF 条件")):
            web_page2 = xbot_visual.web.create(web_type="chrome", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=lambda: path_to_chrome_exe if path_to_chrome_exe else None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 15, "打开网页"))
            xbot_visual.web.browser.close(operation="close_specified", browser=web_page2, web_type="cef", task_kill=False, _block=("淘宝登录", 16, "关闭网页"))
            web_page = xbot_visual.web.create(web_type="chrome", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=lambda: path_to_chrome_exe if path_to_chrome_exe else None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 17, "打开网页"))
        elif xbot_visual.workflow.test(operand1=mode, operator="==", operand2="edge", operator_options="{}", _block=("淘宝登录", 18, "Else IF")):
            web_page2 = xbot_visual.web.create(web_type="edge", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 19, "打开网页"))
            xbot_visual.web.browser.close(operation="close_specified", browser=web_page2, web_type="cef", task_kill=False, _block=("淘宝登录", 20, "关闭网页"))
            web_page = xbot_visual.web.create(web_type="edge", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 21, "打开网页"))
        elif xbot_visual.workflow.test(operand1=mode, operator="==", operand2="cent", operator_options="{}", _block=("淘宝登录", 22, "Else IF")):
            web_page2 = xbot_visual.web.create(web_type="Cent Browser", value="https://login.taobao.com/member/login.jhtml", silent_running=True, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 23, "打开网页"))
            xbot_visual.web.browser.close(operation="close_specified", browser=web_page2, web_type="cef", task_kill=False, _block=("淘宝登录", 24, "关闭网页"))
            web_page = xbot_visual.web.create(web_type="Cent Browser", value="https://login.taobao.com/member/login.jhtml", silent_running=True, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 25, "打开网页"))
        else:
            web_page2 = xbot_visual.web.create(web_type="cef", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 27, "打开网页"))
            xbot_visual.web.browser.close(operation="close_specified", browser=web_page2, web_type="cef", task_kill=False, _block=("淘宝登录", 28, "关闭网页"))
            web_page = xbot_visual.web.create(web_type="cef", value="https://login.taobao.com/member/login.jhtml", silent_running=False, wait_load_completed=True, load_timeout=加载超时时间, stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("淘宝登录", 29, "打开网页"))
        #endif
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘系_新验证码_标识"), _block=("淘宝登录", 31, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "xbot",
                "background_ele": package.selector("淘系_新验证码_背景图"),
                "slider_ele": package.selector("淘系_新验证码_拖拽"),
                "ym_token": ym_token,
                "retry_count": lambda: 滑动次数,
                "offset": lambda: 0,
                "speed": lambda: 1,
                }, outputs=[
            ], _block=("淘宝登录", 32, "通用单图滑块验证"))
        #endif
        web_wait_result3 = xbot_visual.web.element.wait(browser=web_page, element=package.selector("链接_使用其他帐户登录"), state="appear", iswait=True, timeout="5", _block=("淘宝登录", 34, "等待元素(web)"))
        # 如果出现“快速进入”，需要点击“使用其他账户登录”才能出现用户名、密码输入控件
        if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 是否退出已登录,"operand2": "","operator": "is false"}], _block=("淘宝登录", 36, "IF 多条件")):
            if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("快速进入"), text="", _block=("淘宝登录", 37, "IF 网页包含")):
                xbot_visual.programing.log(type="info", text="已经快速进入当前账号中", _block=("淘宝登录", 38, "打印日志"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("快速进入"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 39, "点击元素(web)"))
                return
            else:
                xbot_visual.programing.log(type="info", text="当前没有账号登录中~", _block=("淘宝登录", 42, "打印日志"))
            #endif
        #endif
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("链接_使用其他帐户登录"), text="", _block=("淘宝登录", 45, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("链接_使用其他帐户登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 46, "点击元素(web)"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("密码登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 48, "点击元素(web)"))
        for loop_index2 in xbot_visual.workflow.range_iterator(start="1", stop="4", step="1", _block=("淘宝登录", 49, "For次数循环")):
            if xbot_visual.workflow.test(operand1=loop_index2, operator="==", operand2="4", operator_options="{}", _block=("淘宝登录", 50, "IF 条件")):
                raise Exception("当前输入框内容和实际账号不相等，请重新运行该指令")
            #endif
            xbot_visual.web.element.input(browser=web_page, element=package.selector("淘宝账号_输入框"), text=userid, append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 53, "填写输入框(web)"))
            xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("淘宝登录", 54, "等待"))
            web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("淘宝账号_输入框"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("淘宝登录", 55, "获取元素信息(web)"))
            if xbot_visual.workflow.test(operand1=userid, operator="==", operand2=web_element_attribute, operator_options="{}", _block=("淘宝登录", 56, "IF 条件")):
                break
            #endif
        #endloop
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘系_新验证码_标识"), _block=("淘宝登录", 60, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "xbot",
                "background_ele": package.selector("淘系_新验证码_背景图"),
                "slider_ele": package.selector("淘系_新验证码_拖拽"),
                "ym_token": ym_token,
                "retry_count": lambda: 滑动次数,
                "offset": lambda: 0,
                "speed": lambda: 1,
                }, outputs=[
            ], _block=("淘宝登录", 61, "通用单图滑块验证"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("淘宝密码_输入框"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 63, "点击元素(web)"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("阿里_滑块"), _block=("淘宝登录", 64, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.ali_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "xbot",
                "drag_ele": package.selector("阿里_滑块"),
                "refresh_ele": package.selector("阿里_刷新"),
                "ym_token": "",
                "retry_count": lambda: 重试次数,
                "offset": lambda: 0,
                "speed": "middle",
                "monitor_time": lambda: 3,
                }, outputs=[
            ], _block=("淘宝登录", 65, "阿里滑块验证"))
        #endif
        for loop_index2 in xbot_visual.workflow.range_iterator(start="1", stop="4", step="1", _block=("淘宝登录", 67, "For次数循环")):
            if xbot_visual.workflow.test(operand1=loop_index2, operator="==", operand2="4", operator_options="{}", _block=("淘宝登录", 68, "IF 条件")):
                raise Exception("当前输入框内容和实际账号不相等，请重新运行该指令")
            #endif
            xbot_visual.web.element.click(browser=web_page, element=package.selector("淘宝密码_输入框"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 71, "点击元素(web)"))
            xbot_visual.web.element.input(browser=web_page, element=package.selector("淘宝密码_输入框"), text=password, append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 72, "填写输入框(web)"))
            xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("淘宝登录", 73, "等待"))
            web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("淘宝密码_输入框"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("淘宝登录", 74, "获取元素信息(web)"))
            if xbot_visual.workflow.test(operand1=password, operator="==", operand2=web_element_attribute, operator_options="{}", _block=("淘宝登录", 75, "IF 条件")):
                break
            #endif
        #endloop
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("淘宝登录", 79, "等待"))
        xbot_visual.programing.log(type="info", text="检测滑条是否出现", _block=("淘宝登录", 80, "打印日志"))
        for loop_index in xbot_visual.workflow.range_iterator(start=lambda: 1, stop=重试次数, step="1", _block=("淘宝登录", 81, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘宝登录_横向滑块"), _block=("淘宝登录", 82, "IF 元素可见(web)")):
                xbot_visual.programing.log(type="info", text="当前检测到滑条，正在拖动", _block=("淘宝登录", 83, "打印日志"))
                _ = xbot_visual.process.run(process="process11", package=__name__, inputs={
                    "web_page": lambda: web_page,
                    "drag_start_element": package.selector("淘宝滑块"),
                    "background_element": package.selector("请按住滑块，拖动到最右边"),
                    }, outputs=[
                ], _block=("淘宝登录", 84, "调用流程"))
            else:
                break
            #endif
        #endloop
        xbot_visual.web.element.click(browser=web_page, element=package.selector("淘宝登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("淘宝登录", 89, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("淘宝登录", 90, "等待"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("阿里_滑块"), _block=("淘宝登录", 91, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_jfbym.ali_slider_captcha", package=__name__, inputs={
                "web_page": web_page,
                "engine": "xbot",
                "drag_ele": package.selector("阿里_滑块"),
                "refresh_ele": package.selector("阿里_刷新"),
                "ym_token": "",
                "retry_count": lambda: 重试次数,
                "offset": lambda: 0,
                "speed": "middle",
                "monitor_time": lambda: 3,
                }, outputs=[
            ], _block=("淘宝登录", 92, "阿里滑块验证"))
        #endif
        for loop_index in xbot_visual.workflow.range_iterator(start=lambda: 1, stop=重试次数, step="1", _block=("淘宝登录", 94, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘宝登录_横向滑块"), _block=("淘宝登录", 95, "IF 元素可见(web)")):
                xbot_visual.programing.log(type="info", text="当前检测到滑条，正在拖动", _block=("淘宝登录", 96, "打印日志"))
                _ = xbot_visual.process.run(process="process11", package=__name__, inputs={
                    "web_page": lambda: web_page,
                    "drag_start_element": package.selector("淘宝滑块"),
                    "background_element": package.selector("请按住滑块，拖动到最右边"),
                    }, outputs=[
                ], _block=("淘宝登录", 97, "调用流程"))
            else:
                break
            #endif
        #endloop
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘宝登录_按钮"), _block=("淘宝登录", 102, "IF 元素可见(web)")):
            try:
                xbot_visual.web.element.click(browser=web_page, element=package.selector("淘宝登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="5", _block=("淘宝登录", 103, "点击元素(web)"))
            except Exception as e:
                pass
        #endif
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("淘宝登录-错误提示"), _block=("淘宝登录", 105, "IF 元素可见(web)")):
            web_element_attribute2 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("淘宝登录-错误提示"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("淘宝登录", 106, "获取元素信息(web)"))
            raise Exception(web_element_attribute2)
        #endif
    finally:
        args["web_page"] = web_page
