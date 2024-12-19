import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        username = "17756164521"
        password = "jiandanlove520"
        web_mode = "0"
        tj_username = ""
        tj_password = ""
    else:
        username = args.get("username", "17756164521")
        password = args.get("password", "jiandanlove520")
        web_mode = args.get("web_mode", "0")
        tj_username = args.get("tj_username", "")
        tj_password = args.get("tj_password", "")
    try:
        web_page = None
        if xbot_visual.workflow.test(operand1=web_mode, operator="==", operand2="0", operator_options="{}", _block=("支付宝登录（嘻嘻嘻）", 2, "IF 条件")):
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="url", value="https://auth.alipay.com/login/index.htm", use_wildcard=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://auth.alipay.com/login/index.htm", _block=("支付宝登录（嘻嘻嘻）", 3, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第3条指令: {e}')
                time.sleep(3)
        else:
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="cef", mode="url", value="https://auth.alipay.com/login/index.htm", use_wildcard=False, wait_load_completed=True, load_timeout="60", stop_load_if_load_timeout="handleExcept", open_page=True, url="https://auth.alipay.com/login/index.htm", _block=("支付宝登录（嘻嘻嘻）", 5, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info', text=f'第5条指令: {e}')
                time.sleep(3)
        #endif
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("支付宝扫码_图像"), _block=("支付宝登录（嘻嘻嘻）", 7, "IF 元素可见(web)")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝_登录_按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录（嘻嘻嘻）", 8, "点击元素(web)"))
        #endif
        xbot_visual.web.element.input(browser=web_page, element=package.selector("支付宝_账号_输入框"), text=lambda: str(username), append=False, simulate=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录（嘻嘻嘻）", 10, "填写输入框(web)"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("支付宝登录（嘻嘻嘻）", 11, "For次数循环")):
            xbot_visual.web.element.input(browser=web_page, element=package.selector("支付宝_密码_输入框"), text=lambda: str(password), append=False, simulate=False, save_to_clipboard=False, input_type="automatic", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录（嘻嘻嘻）", 12, "填写输入框(web)"))
            captcha_result = ""
            if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": lambda: bool(tj_username),"operand2": "","operator": "is true"}], _block=("支付宝登录（嘻嘻嘻）", 14, "IF 多条件")):
                captcha_result = xbot_visual.web_service.captcha(engine_type="ttshitu", username=tj_username, password=tj_password, captcha_type="3", third_party_code="ttshitu_3_predict", image_source="web_element", image_file=None, image_browser=web_page, image_web_selector=package.selector("支付宝_验证码_图片"), image_window="", image_win_selector=None, image_region_x1="0", image_region_y1="0", image_region_x2="0", image_region_y2="0", imageback_source="screen", back_image_file=None, imageback_browser="", imageback_web_selector=None, imageback_window="", imageback_win_selector=None, imageback_region_x1="0", imageback_region_y1="0", imageback_region_x2="0", imageback_region_y2="0", typename=None, is_to96dpi=False, remark=None, _block=("支付宝登录（嘻嘻嘻）", 15, "验证码识别"))
            else:
                captcha_result = xbot_visual.web_service.captcha(engine_type="shadowbot", username=None, password="", captcha_type="3", third_party_code="ttshitu_3_predict", image_source="web_element", image_file=None, image_browser=web_page, image_web_selector=package.selector("支付宝_验证码_图片"), image_window="", image_win_selector=None, image_region_x1="0", image_region_y1="0", image_region_x2="0", image_region_y2="0", imageback_source="screen", back_image_file=None, imageback_browser="", imageback_web_selector=None, imageback_window="", imageback_win_selector=None, imageback_region_x1="0", imageback_region_y1="0", imageback_region_x2="0", imageback_region_y2="0", typename=None, is_to96dpi=False, remark=None, _block=("支付宝登录（嘻嘻嘻）", 17, "验证码识别"))
            #endif
            xbot_visual.web.element.input(browser=web_page, element=package.selector("支付宝_验证码_输入框"), text=captcha_result, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录（嘻嘻嘻）", 19, "填写输入框(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("支付宝_登录_按钮2"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("支付宝登录（嘻嘻嘻）", 20, "点击元素(web)"))
        #endloop
    finally:
        args["web_page"] = web_page
