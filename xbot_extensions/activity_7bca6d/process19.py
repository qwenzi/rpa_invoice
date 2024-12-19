import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        web_page = None
        百度OCR账号 = ""
        百度OCR密码 = ""
    else:
        web_page = args.get("web_page", None)
        百度OCR账号 = args.get("百度OCR账号", "")
        百度OCR密码 = args.get("百度OCR密码", "")
    try:
        OCR_engine = xbot_visual.programing.variable(value=lambda: None
        , _block=("zfb验证码识别", 1, "设置变量"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("验证码"), _block=("zfb验证码识别", 2, "IF 元素可见(web)")):
            loop_index = -1
            while True:
                loop_index += 1
                if xbot_visual.workflow.test(operand1=百度OCR账号, operator="not empty", operand2="", operator_options="{}", _block=("zfb验证码识别", 4, "IF 条件")):
                    OCR_engine = xbot_visual.ocr.create_ai_engine(engine="baidu", use_custom_account=True, param1=百度OCR账号, param2=百度OCR密码, _block=("zfb验证码识别", 5, "配置AI引擎"))
                else:
                    OCR_engine = xbot_visual.ocr.create_ai_engine(engine="shadowbot", use_custom_account=False, param1="", param2="", _block=("zfb验证码识别", 7, "配置AI引擎"))
                #endif
                captcha_result = xbot_visual.web_service.captcha(engine_type="shadowbot", username=None, password=xbot_visual.decrypt(""), captcha_type="3", third_party_code="ttshitu_3_predict", image_source="web_element", image_file=None, image_browser=web_page, image_web_selector=package.selector("验证码元素"), image_window="", image_win_selector=None, image_region_x1="0", image_region_y1="0", image_region_x2="0", image_region_y2="0", imageback_source="screen", back_image_file=None, imageback_browser="", imageback_web_selector=None, imageback_window="", imageback_win_selector=None, imageback_region_x1="0", imageback_region_y1="0", imageback_region_x2="0", imageback_region_y2="0", typename=None, is_to96dpi=False, remark=None, _block=("zfb验证码识别", 9, "验证码识别"))
                if xbot_visual.workflow.test(operand1=lambda: len(captcha_result.strip()), operator="!=", operand2="4", operator_options="{}", _block=("zfb验证码识别", 10, "IF 条件")):
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("验证码"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("zfb验证码识别", 11, "点击元素(web)"))
                    continue
                #endif
                xbot_visual.web.element.click(browser=web_page, element=package.selector("输入框_checkCode"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("zfb验证码识别", 14, "点击元素(web)"))
                xbot_visual.web.element.input(browser=web_page, element=package.selector("输入框_checkCode"), text=captcha_result.strip(), append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="2", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("zfb验证码识别", 15, "填写输入框(web)"))
                try:
                    web_wait_result2 = xbot_visual.web.element.wait(browser=web_page, element=package.selector("验证码输入正确"), state="appear", iswait=True, timeout="5", _block=("zfb验证码识别", 16, "等待元素(web)"))
                except Exception as e:
                    xbot_visual.programing.log(type='info',text=e,_block=("zfb验证码识别", 16,"等待元素(web)"))
                    web_wait_result2 = None
                if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("验证码输入正确"), text="", _block=("zfb验证码识别", 17, "IF 网页包含")):
                    break
                else:
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("验证码"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("zfb验证码识别", 20, "点击元素(web)"))
                #endif
            #endloop
        #endif
    finally:
        pass
