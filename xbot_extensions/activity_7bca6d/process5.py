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
        youzan_url = xbot_visual.programing.variable(value="https://account.youzan.com/login"
        , _block=("有赞登录", 1, "设置变量"))
        if xbot_visual.workflow.test(operand1=web_type, operator="==", operand2="0", operator_options="{}", _block=("有赞登录", 2, "IF 条件")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="url", value=youzan_url, use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url=youzan_url, _block=("有赞登录", 3, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("有赞登录", 3,"获取已打开的网页对象"))
                time.sleep(3)
        else:
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="url", value=youzan_url, use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://account.youzan.com/login", _block=("有赞登录", 5, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("有赞登录", 5,"获取已打开的网页对象"))
                time.sleep(3)
        #endif
        # 判断是否已经登录, 如果已经登录, 退出登录
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("有赞登录", 8, "等待"))
        web_page_attribute = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("有赞登录", 9, "获取网页信息"))
        if xbot_visual.workflow.test(operand1=web_page_attribute, operator="!=", operand2=youzan_url, operator_options="{}", _block=("有赞登录", 10, "IF 条件")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("我知道了"), _block=("有赞登录", 11, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("我知道了"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 12, "点击元素(web)"))
            #endif
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("有赞-账号昵称"), _block=("有赞登录", 14, "IF 元素可见(web)")):
                xbot_visual.web.element.hover(browser=web_page, element=package.selector("有赞-账号昵称"), simulate=True, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 15, "鼠标悬停在元素上(web)"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("有赞-账号昵称"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 16, "点击元素(web)"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("有赞-退出登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 17, "点击元素(web)"))
            #endif
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("有赞-选择店铺"), _block=("有赞登录", 19, "IF 元素可见(web)")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("有赞-选择店铺-退出"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 20, "点击元素(web)"))
            #endif
        #endif
        # 账号登录
        try:
            web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("行内元素_使用帐号登录"), state="appear", iswait=True, timeout="5", _block=("有赞登录", 24, "等待元素(web)"))
        except Exception as e:
            xbot_visual.programing.log(type='info',text=e,_block=("有赞登录", 24,"等待元素(web)"))
            web_wait_result = False
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("行内元素_使用帐号登录"), text="", _block=("有赞登录", 25, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("行内元素_使用帐号登录"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 26, "点击元素(web)"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("行内元素_密码登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 28, "点击元素(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("有赞手机号_输入框"), text=username, append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 29, "填写输入框(web)"))
        xbot_visual.web.element.input(browser=web_page, element=package.selector("有赞密码_输入框"), text=password, append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1600", delay_after="2", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 30, "填写输入框(web)"))
        xbot_visual.web.element.check(browser=web_page, element=package.selector("有赞_同意条款复选框"), mode="check", delay_after="1", timeout="20", _block=("有赞登录", 31, "设置复选框(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("有赞_登录"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("有赞登录", 32, "点击元素(web)"))
        web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("有赞背景_图片"), state="appear", iswait=True, timeout="20", _block=("有赞登录", 33, "等待元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("有赞登录", 34, "等待"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("有赞登录", 35, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("有赞背景_图片"), _block=("有赞登录", 36, "IF 元素可见(web)")):
                break
            #endif
            start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("有赞滑块_图片"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("有赞登录", 39, "获取元素对象(web)"))
            background_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("有赞背景_图片"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("有赞登录", 40, "获取元素对象(web)"))
            drag_start_element = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("有赞拖动滑块_按钮"), css_selector="", xpath_selector="", is_related_parent=False, parent="", timeout="20", _block=("有赞登录", 41, "获取元素对象(web)"))
            process_result = xbot_visual.process.run(process="process2", package=__name__, inputs={
                "start_element": start_element,
                "background_element": background_element,
                "tj_username": tj_username,
                "tj_password": tj_password,
                "web_page": lambda: web_page,
                }, outputs=[
                "distince",
            ], _block=("有赞登录", 42, "调用流程"))
            _ = xbot_visual.process.run(process="process3", package=__name__, inputs={
                "distance": process_result.distince,
                "drag_start_element": drag_start_element,
                "web_page": web_page,
                }, outputs=[
            ], _block=("有赞登录", 43, "调用流程"))
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("有赞登录", 44, "等待"))
        #endloop
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("有赞登录之后的提示框"), _block=("有赞登录", 46, "IF 元素可见(web)")):
            web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("有赞登录之后的提示框"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("有赞登录", 47, "获取元素信息(web)"))
            if xbot_visual.workflow.test(operand1=web_element_attribute, operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("有赞登录", 48, "IF 条件")):
                raise Exception("登录失败，" + xbot_visual.sh_str(web_element_attribute))
            #endif
        #endif
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("有赞登录", 52, "等待"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("有赞_登录"), _block=("有赞登录", 53, "IF 元素可见(web)")):
            raise Exception("登录失败，当前可能需要验证手机号或账号未设置密码登录")
        #endif
    finally:
        args["web_page"] = web_page
