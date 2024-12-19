import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = ""
    if args is None:
        web_type = ""
        username = ""
        password = ""
        tj_username = ""
        tj_password = ""
    else:
        web_type = args.get("web_type", "")
        username = args.get("username", "")
        password = args.get("password", "")
        tj_username = args.get("tj_username", "")
        tj_password = args.get("tj_password", "")
    try:
        web_page = None
        # 设置浏览器类型
        if xbot_visual.workflow.test(operand1=web_type, operator="==", operand2="0", _block=("法大大登录", 3, "IF 条件")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="url", value="https://saas-sso.fadada.com", use_wildcard=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://fxg.jinritemai.com/login", _block=("法大大登录", 4, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第4条指令: {e}')
                time.sleep(3)
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("法大大登录", 5, "等待"))
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("法大大登录", 6, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第6条指令: {e}')
                time.sleep(3)
        else:
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="title", value="https://saas-sso.fadada.com", use_wildcard=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://fxg.jinritemai.com/login", _block=("法大大登录", 8, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第8条指令: {e}')
                time.sleep(3)
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("法大大登录", 9, "等待"))
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="activated", value="", use_wildcard=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("法大大登录", 10, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第10条指令: {e}')
                time.sleep(3)
        #endif
        # 这里补上自己的登录逻辑，TODO
        background_element_list = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("法大大_背景图"), css_selector="", xpath_selector="", is_related_parent=False, parent="", operation="element", attribute_name=None, timeout="20", _block=("法大大登录", 13, "获取相似元素列表(web)"))
        process_result = xbot_visual.process.run(process="process14", package=__name__, inputs={
            "相似元素列表": lambda: background_element_list,
            "网页对象": lambda: web_page,
            }, outputs=[
            "可见的元素",
        ], _block=("法大大登录", 14, "调用流程"))
        background_element = process_result.可见的元素
        slide_element_list = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("法大大_滑块"), css_selector="", xpath_selector="", is_related_parent=False, parent="", operation="element", attribute_name=None, timeout="20", _block=("法大大登录", 16, "获取相似元素列表(web)"))
        process_result = xbot_visual.process.run(process="process14", package=__name__, inputs={
            "相似元素列表": lambda: slide_element_list,
            "网页对象": lambda: web_page,
            }, outputs=[
            "可见的元素",
        ], _block=("法大大登录", 17, "调用流程"))
        slice_element = process_result.可见的元素
        web_js_result = xbot_visual.web.browser.execute_javascript(browser=web_page, element=background_element, argument=None, code="function (element, input) {\r\n    // 在此处编写您的Javascript代码\r\n    // element表示选择的操作目标(HTML元素)\r\n    // input表示输入的参数(字符串)\r\n    element.style.display=\"none\"\r\n    return null;\r\n}", _block=("法大大登录", 19, "执行JS脚本"))
        screenshot_save_file_name = xbot_visual.web.element.screenshot(browser=web_page, capture_area="Element", element=slice_element, folder_path="C:\\Users\\zhuxia\\Desktop", random_filename=True, filename=None, overwrite_file=True, save_to_clipboard=True, height="25000", piece_height="3000", _block=("法大大登录", 20, "网页截图"))
        web_js_result = xbot_visual.web.browser.execute_javascript(browser=web_page, element=background_element, argument=None, code="function (element, input) {\r\n    // 在此处编写您的Javascript代码\r\n    // element表示选择的操作目标(HTML元素)\r\n    // input表示输入的参数(字符串)\r\n    element.style.display=\"block\"\r\n    return null;\r\n}", _block=("法大大登录", 21, "执行JS脚本"))
        web_js_result = xbot_visual.web.browser.execute_javascript(browser=web_page, element=slice_element, argument=None, code="function (element, input) {\r\n    // 在此处编写您的Javascript代码\r\n    // element表示选择的操作目标(HTML元素)\r\n    // input表示输入的参数(字符串)\r\n    element.style.display=\"none\"\r\n    return null;\r\n}", _block=("法大大登录", 22, "执行JS脚本"))
        captcha_result2 = xbot_visual.web_service.captcha(engine_type="shadowbot", username=None, password="", captcha_type="18", third_party_code="ttshitu_18_predict", image_source="clipboard", image_file=None, image_browser="", image_web_selector=None, image_window="", image_win_selector=None, image_region_x1="0", image_region_y1="0", image_region_x2="0", image_region_y2="0", imageback_source="web_element", back_image_file=None, imageback_browser=web_page, imageback_web_selector=background_element, imageback_window="0", imageback_win_selector=None, imageback_region_x1="0", imageback_region_y1="0", imageback_region_x2="0", imageback_region_y2="0", typename=None, remark=None, _block=("法大大登录", 23, "验证码识别"))
        web_js_result = xbot_visual.web.browser.execute_javascript(browser=web_page, element=slice_element, argument=None, code="function (element, input) {\r\n    // 在此处编写您的Javascript代码\r\n    // element表示选择的操作目标(HTML元素)\r\n    // input表示输入的参数(字符串)\r\n    element.style.display=\"block\"\r\n    return null;\r\n}", _block=("法大大登录", 24, "执行JS脚本"))
        xbot_visual.programing.log(type="info", text=captcha_result2, _block=("法大大登录", 25, "打印日志"))
        image_left = xbot_visual.text.extract_content_from_text(text=captcha_result2, extract_way="custom", regular_pattern="(\\d+),", just_get_first=True, ignore_case=False, _block=("法大大登录", 26, "从文本中提取内容"))
        # 分辨率的计算
        invoke_result = xbot_visual.process.invoke_module(module="utils", package=__name__, function="get_ppi", params={
        }, _block=("法大大登录", 28, "调用模块"))
        distince = int(int(image_left)*invoke_result)
        xbot_visual.programing.log(type="info", text=distince, _block=("法大大登录", 30, "打印日志"))
        # 拖拽
        slider_element_list = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("法大大_滑块_拖动"), css_selector="", xpath_selector="", is_related_parent=False, parent="", operation="element", attribute_name=None, timeout="20", _block=("法大大登录", 32, "获取相似元素列表(web)"))
        process_result = xbot_visual.process.run(process="process14", package=__name__, inputs={
            "相似元素列表": lambda: slider_element_list,
            "网页对象": lambda: web_page,
            }, outputs=[
            "可见的元素",
        ], _block=("法大大登录", 33, "调用流程"))
        drag_start_element = process_result.可见的元素
        xbot_visual.web.element.hover(browser=web_page, element=drag_start_element, simulate=True, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", _block=("法大大登录", 35, "鼠标悬停在元素上(web)"))
        point_x, point_y = xbot_visual.win32.get_mouse_position(relative_to="screen", _block=("法大大登录", 36, "获取鼠标当前位置"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="down", hardware_driver_click=False, keys="null", delay_after="1", _block=("法大大登录", 37, "鼠标点击"))
        xbot_visual.win32.move_mouse(point_x=distince, point_y="0", relative_to="currentmouseposition", move_speed="middle", delay_after="1", _block=("法大大登录", 38, "移动鼠标"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="up", hardware_driver_click=False, keys="null", delay_after="1", _block=("法大大登录", 39, "鼠标点击"))
    finally:
        args["web_page"] = web_page
