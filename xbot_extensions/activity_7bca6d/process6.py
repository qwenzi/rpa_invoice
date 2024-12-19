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
        web_mode = ""
        tj_username = ""
        tj_password = ""
        rec_count = 5
        login_url = ""
    else:
        username = args.get("username", "")
        password = args.get("password", "")
        web_mode = args.get("web_mode", "")
        tj_username = args.get("tj_username", "")
        tj_password = args.get("tj_password", "")
        rec_count = args.get("rec_count", 5)
        login_url = args.get("login_url", "")
    try:
        web_page = xbot_visual.programing.variable(value=lambda: None
        , _block=("京东登录", 1, "设置变量"))
        if xbot_visual.workflow.test(operand1=login_url, operator="empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("京东登录", 2, "IF 条件")):
            login_url = xbot_visual.programing.variable(value="https://passport.jd.com/new/login.aspx"
            , _block=("京东登录", 3, "设置变量"))
        #endif
        if xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="0", operator_options="{}", _block=("京东登录", 5, "IF 条件")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="url", value=login_url, use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url=login_url, _block=("京东登录", 6, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 6,"获取已打开的网页对象"))
                time.sleep(3)
        elif xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="edge", operator_options="{}", _block=("京东登录", 7, "Else IF")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="edge", mode="url", value=login_url, use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url=login_url, _block=("京东登录", 8, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 8,"获取已打开的网页对象"))
                time.sleep(3)
        else:
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="title", value=login_url, use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="stopLoad", open_page=True, url=login_url, _block=("京东登录", 10, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 10,"获取已打开的网页对象"))
                time.sleep(3)
        #endif
        # 如果已经存在登录界面, 且存在弹窗, 会造成登录异常, 刷新网页, 重新加载登录界面
        xbot_visual.programing.sleep(random_number=True, seconds="1", start_number="1", stop_number="2", _block=("京东登录", 13, "等待"))
        try:
            xbot_visual.web.browser.navigate(browser=web_page, mode="reload", url="", ignore_cache=False, load_timeout="40", _block=("京东登录", 14, "跳转至新网址"))
        except Exception as e:
            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 14,"跳转至新网址"))
        # 退出登录
        web_page_url = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 16, "获取网页信息"))
        # 新版京东页面的登录
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("新版京东登录界面"), _block=("京东登录", 18, "IF 元素可见(web)")):
            xbot_visual.programing.log(type="info", text="当前是新版本的京东登录界面", _block=("京东登录", 19, "打印日志"))
            for loop_index3 in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("京东登录", 20, "For次数循环")):
                # 切换至账号登录
                xbot_visual.web.element.click(browser=web_page, element=package.selector("新版京东界面-密码登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 22, "点击元素(web)"))
                xbot_visual.web.element.input(browser=web_page, element=package.selector("新版京东-账号输入框"), text=lambda: str(username), append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 23, "填写输入框(web)"))
                web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("新版京东-账号输入框"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("京东登录", 24, "获取元素信息(web)"))
                if xbot_visual.workflow.test(operand1=web_element_attribute, operator="==", operand2=username, operator_options="{}", _block=("京东登录", 25, "IF 条件")):
                    break
                else:
                    xbot_visual.web.element.input(browser=web_page, element=package.selector("新版京东-账号输入框"), text=lambda: username, append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 28, "填写输入框(web)"))
                #endif
                if xbot_visual.workflow.test(operand1=loop_index3, operator="==", operand2="5", operator_options="{}", _block=("京东登录", 30, "IF 条件")):
                    raise Exception("账号输入框填写失败")
                #endif
            #endloop
            xbot_visual.web.element.input(browser=web_page, element=package.selector("新版京东-密码填写框"), text=lambda: str(password), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="custom", sudoku_part="MiddleLeft", offset_x="5", offset_y="0", timeout="20", _block=("京东登录", 34, "填写输入框(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("新版京东-登录按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 35, "点击元素(web)"))
            # 用户判断网页是否处于加载过程中
            if xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="0", operator_options="{}", _block=("京东登录", 37, "IF 条件")):
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京东登录", 38, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 38,"获取已打开的网页对象"))
                    time.sleep(3)
            elif xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="edge", operator_options="{}", _block=("京东登录", 39, "Else IF")):
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="edge", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京东登录", 40, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 40,"获取已打开的网页对象"))
                    time.sleep(3)
            else:
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="cef", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="stopLoad", open_page=False, url=None, _block=("京东登录", 42, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 42,"获取已打开的网页对象"))
                    time.sleep(3)
            #endif
            try:
                web_wait_result2 = xbot_visual.web.element.wait(browser=web_page, element=package.selector("京东首页_搜索框"), state="appear", iswait=True, timeout="8", _block=("京东登录", 44, "等待元素(web)"))
            except Exception as e:
                xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 44,"等待元素(web)"))
                web_wait_result2 = None
            if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("京东首页_搜索框"), text="", _block=("京东登录", 45, "IF 网页包含")):
                if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="not_contains_element", selector=package.selector("京东首页_请登录"), text="", _block=("京东登录", 46, "IF 网页包含")):
                    return
                #endif
            #endif
            web_page_url = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 50, "获取网页信息"))
            for loop_index in xbot_visual.workflow.range_iterator(start="1", stop=rec_count, step="1", _block=("京东登录", 51, "For次数循环")):
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("京东滑块_图像"), _block=("京东登录", 52, "IF 元素可见(web)")):
                    break
                #endif
                xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("京东登录", 55, "等待"))
                start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东滑块_图像"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 56, "获取元素对象(web)"))
                background_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东滑块背景_图片"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 57, "获取元素对象(web)"))
                drag_start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东拖动滑块_按钮"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 58, "获取元素对象(web)"))
                process_result = xbot_visual.process.run(process="process2", package=__name__, inputs={
                    "start_element": start_element,
                    "background_element": background_element,
                    "tj_username": lambda: str(tj_username),
                    "tj_password": lambda: str(tj_password),
                    "web_page": web_page,
                    }, outputs=[
                    "distince",
                ], _block=("京东登录", 59, "调用流程"))
                # 调整滑块的拖动速度
                bound = xbot_visual.web.element.get_bounding(browser=web_page, element=drag_start_element, to96dpi=True, relative_to="screen", timeout="20", _block=("京东登录", 61, "获取元素位置(web)"))
                invoke_result = xbot_visual.process.invoke_module(module="utils", package=__name__, function="drag", params={
                    "point_x": bound.center_x,
                    "point_y": bound.center_y,
                    "distance": process_result.distince,
                    "move_speed": "fast",
                }, _block=("京东登录", 62, "调用模块"))
                xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("京东登录", 63, "等待"))
            #endloop
            # 判断是否成功登录的逻辑
            web_page_url_new = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 66, "获取网页信息"))
            if xbot_visual.workflow.test(operand1=web_page_url, operator="==", operand2=web_page_url_new, operator_options="{}", _block=("京东登录", 67, "IF 条件")):
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东滑块_图像"), _block=("京东登录", 68, "IF 元素可见(web)")):
                    raise Exception("由于验证码未通过导致登录失败")
                #endif
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("错误信息"), _block=("京东登录", 71, "IF 元素可见(web)")):
                    web_element_attribute2 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("错误信息"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("京东登录", 72, "获取元素信息(web)"))
                    raise Exception(web_element_attribute2)
                #endif
            else:
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东登录-登录之后的短信识别验证"), _block=("京东登录", 76, "IF 元素可见(web)")):
                    raise Exception("当前账号需要短信验证")
                #endif
            #endif
        else:
            # 兼容旧版京东登录
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("换个账号登录"), _block=("京东登录", 82, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("换个账号登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 83, "点击元素(web)"))
            #endif
            # 部分网页有此提示, 京东提示_我知道了
            xbot_visual.programing.sleep(random_number=True, seconds="1", start_number="1", stop_number="3", _block=("京东登录", 86, "等待"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东提示_我知道了"), _block=("京东登录", 87, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("京东提示_我知道了"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 88, "点击元素(web)"))
            #endif
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东账户登录_按钮"), _block=("京东登录", 90, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("京东账户登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 91, "点击元素(web)"))
            #endif
            for loop_index2 in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("京东登录", 93, "For次数循环")):
                xbot_visual.web.element.input(browser=web_page, element=package.selector("京东账号_输入框"), text=lambda: str(username), append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 94, "填写输入框(web)"))
                web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("京东账号_输入框"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("京东登录", 95, "获取元素信息(web)"))
                if xbot_visual.workflow.test(operand1=web_element_attribute, operator="==", operand2=username, operator_options="{}", _block=("京东登录", 96, "IF 条件")):
                    break
                else:
                    xbot_visual.web.element.input(browser=web_page, element=package.selector("京东账号_输入框"), text=None, append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 99, "填写输入框(web)"))
                #endif
                if xbot_visual.workflow.test(operand1=loop_index2, operator="==", operand2="5", operator_options="{}", _block=("京东登录", 101, "IF 条件")):
                    raise Exception("账号输入框填写失败")
                #endif
            #endloop
            xbot_visual.web.element.input(browser=web_page, element=package.selector("京东密码_输入框"), text=lambda: str(password), append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="custom", sudoku_part="MiddleLeft", offset_x="5", offset_y="0", timeout="20", _block=("京东登录", 105, "填写输入框(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("京东登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京东登录", 106, "点击元素(web)"))
            # 用户判断网页是否处于加载过程中
            if xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="0", operator_options="{}", _block=("京东登录", 108, "IF 条件")):
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京东登录", 109, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 109,"获取已打开的网页对象"))
                    time.sleep(3)
            elif xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="edge", operator_options="{}", _block=("京东登录", 110, "Else IF")):
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="edge", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京东登录", 111, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 111,"获取已打开的网页对象"))
                    time.sleep(3)
            else:
                for _xbot_retry_time in range(4):
                    try:
                        web_page = xbot_visual.web.get(web_type="cef", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="stopLoad", open_page=False, url=None, _block=("京东登录", 113, "获取已打开的网页对象"))
                        break
                    except Exception as e:
                        if _xbot_retry_time == 3:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 113,"获取已打开的网页对象"))
                    time.sleep(3)
            #endif
            try:
                web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("京东滑块_图像"), state="appear", iswait=True, timeout="3", _block=("京东登录", 115, "等待元素(web)"))
            except Exception as e:
                xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 115,"等待元素(web)"))
                web_wait_result = False
            # 等待滑块超时, 应抛出异常, 且滑块内容不可以见, 包含渲染dom, 但是未完全加载出来的场景
            if xbot_visual.workflow.test(operand1=web_wait_result, operator="is false", operand2="", operator_options="{}", _block=("京东登录", 117, "IF 条件")):
                # 企业账号跳转网页略有不同
                web_page_attribute = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 119, "获取网页信息"))
                if xbot_visual.workflow.test(operand1=web_page_attribute, operator="!=", operand2=login_url, operator_options="{}", _block=("京东登录", 120, "IF 条件")):
                    return
                #endif
                try:
                    web_wait_result2 = xbot_visual.web.element.wait(browser=web_page, element=package.selector("京东首页_搜索框"), state="appear", iswait=True, timeout="10", _block=("京东登录", 123, "等待元素(web)"))
                except Exception as e:
                    xbot_visual.programing.log(type='info',text=e,_block=("京东登录", 123,"等待元素(web)"))
                    web_wait_result2 = None
                if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("京东首页_搜索框"), text="", _block=("京东登录", 124, "IF 网页包含")):
                    if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="not_contains_element", selector=package.selector("京东首页_请登录"), text="", _block=("京东登录", 125, "IF 网页包含")):
                        return
                    #endif
                #endif
            else:
                web_page_url = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 130, "获取网页信息"))
                for loop_index in xbot_visual.workflow.range_iterator(start="1", stop=rec_count, step="1", _block=("京东登录", 131, "For次数循环")):
                    if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("京东滑块_图像"), _block=("京东登录", 132, "IF 元素可见(web)")):
                        break
                    #endif
                    xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("京东登录", 135, "等待"))
                    start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东滑块_图像"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 136, "获取元素对象(web)"))
                    background_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东滑块背景_图片"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 137, "获取元素对象(web)"))
                    drag_start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("京东拖动滑块_按钮"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("京东登录", 138, "获取元素对象(web)"))
                    process_result = xbot_visual.process.run(process="process2", package=__name__, inputs={
                        "start_element": start_element,
                        "background_element": background_element,
                        "tj_username": lambda: str(tj_username),
                        "tj_password": lambda: str(tj_password),
                        "web_page": web_page,
                        }, outputs=[
                        "distince",
                    ], _block=("京东登录", 139, "调用流程"))
                    # 调整滑块的拖动速度
                    bound = xbot_visual.web.element.get_bounding(browser=web_page, element=drag_start_element, to96dpi=True, relative_to="screen", timeout="20", _block=("京东登录", 141, "获取元素位置(web)"))
                    invoke_result = xbot_visual.process.invoke_module(module="utils", package=__name__, function="drag", params={
                        "point_x": bound.center_x,
                        "point_y": bound.center_y,
                        "distance": process_result.distince,
                        "move_speed": "fast",
                    }, _block=("京东登录", 142, "调用模块"))
                    xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("京东登录", 143, "等待"))
                #endloop
            #endif
            # 判断是否成功登录的逻辑
            web_page_url_new = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("京东登录", 147, "获取网页信息"))
            if xbot_visual.workflow.test(operand1=web_page_url, operator="==", operand2=web_page_url_new, operator_options="{}", _block=("京东登录", 148, "IF 条件")):
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东滑块_图像"), _block=("京东登录", 149, "IF 元素可见(web)")):
                    raise Exception("由于验证码未通过导致登录失败")
                #endif
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("错误信息"), _block=("京东登录", 152, "IF 元素可见(web)")):
                    web_element_attribute2 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("错误信息"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("京东登录", 153, "获取元素信息(web)"))
                    raise Exception(web_element_attribute2)
                #endif
            else:
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("京东登录-登录之后的短信识别验证"), _block=("京东登录", 157, "IF 元素可见(web)")):
                    raise Exception("当前账号需要短信验证")
                #endif
            #endif
        #endif
    finally:
        args["web_page"] = web_page
