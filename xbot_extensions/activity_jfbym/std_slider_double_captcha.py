import xbot
import os
import xbot_visual
import base64
import json
import base64
import io
import urllib
import http.client
import ctypes

from PIL import ImageGrab, Image

from PIL import Image
from io import BytesIO
from ctypes import windll
from xbot.web.element import WebElement
from xbot.web.chrome import ChromeAutomation

from xbot import print, sleep, win32, web
from .import package
from .package import variables as glv

from xbot._core import robot


def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")


def recg(token, slide_image_base64, background_image_base64):
    """请求云码识别淘"""
    conn = http.client.HTTPConnection("api.jfbym.com")
    headers = { 'Content-Type': 'application/json'}
    data = { 
        "slide_image": slide_image_base64,
        "background_image": background_image_base64,
        'token': token, 
        'type': 11268
    }

    data_json = json.dumps(data)
    conn.request("POST", "/api/YmServer/customApi", body=data_json, headers=headers)
    response = conn.getresponse()
    response_data = response.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    return response_json

def yd_recg(slide_image_base64, background_image_base64):
    token = get_xbot_client()
    conn = http.client.HTTPSConnection("api.yingdao.com")
    payload = json.dumps({
        "thirdPartyInterfaceCode": "jfbym_20111",
        "data": {},
        "thirdPartyReqData": {
            "headers": {},
            "params": {},
            "body": {
                "slide_image": slide_image_base64,
                "background_image": background_image_base64
            },
            "pathVariable": {}
        },
        "bizType": "rpa-command"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }
    conn.request("POST", "/api/openapi/v2/thirdParty/interface/call", payload, headers)
    res = conn.getresponse()
    response_data = res.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    return response_json


def encode_image(image):
    """图片转base64"""
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    base64_string = base64.b64encode(img_bytes).decode('utf-8')
    return base64_string

def drag(drag_ele:WebElement, distance:int):
    x, y, width, height = drag_ele.get_bounding()
    pos_center_x = x + width / 2
    pos_center_y = y + height / 2
    move_speed = "middle"
    win32.manual_motion_on(motion_move=True, motion_click=True, motion_delay=True, min_time=0.1, max_time=0.5)
    win32.mouse_move(point_x=pos_center_x, point_y=pos_center_y, move_speed=move_speed)
    win32.mouse_click(button="left", click_type="down", delay_after=0)
    win32.mouse_move(pos_center_x + distance, pos_center_y, move_speed=move_speed)
    win32.mouse_click(button="left", click_type="up", )
    win32.manual_motion_off()

def _moveTo(x, y):
    """Send the mouse move event to Windows by calling SetCursorPos() win32
    function.

    Args:
      button (str): The mouse button, either 'left', 'middle', or 'right'
      x (int): The x position of the mouse event.
      y (int): The y position of the mouse event.

    Returns:
      None
    """
    ctypes.windll.user32.SetCursorPos(x, y)


def get_ppi():
    """获取屏幕的缩放"""
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    user32 = windll.user32
    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    res = float.as_integer_ratio(round(pix_per_inch / 96,2))
    return res[1]/res[0]


def handle_captcha(web_page:xbot.web.WebBrowser, background_ele, slider_ele, retry_count: int=5, offset=0, token=None):
    
    # xbot.logging.info(f"Cache Dir:{cache_folder}")
    
    if not retry_count: retry_count=5
    
    for i in range(retry_count):
        # slider_ele = web_page.find(slider_ele)
        s_x, s_y, s_w, s_h = web_page.find(slider_ele).get_bounding(to96dpi=False)
        b_x, b_y, b_w, b_h = web_page.find(background_ele).get_bounding(to96dpi=False)

        # screen background
        # xbot.win32.screenshot.save_screen_to_clipboard(s_x+s_w, b_y, b_x + b_w, b_y + b_h)
        xbot.win32.screenshot.save_screen_to_clipboard(b_x, b_y, b_x + b_w, b_y + b_h)
        background_img = ImageGrab.grabclipboard()
        xbot.win32.clipboard.clear()
        background_image_base64  = encode_image(background_img)

        # screen slider
        xbot.win32.screenshot.save_screen_to_clipboard(s_x, s_y, s_x + s_w, s_y + s_h)
        slider_img = ImageGrab.grabclipboard()
        xbot.win32.clipboard.clear()
        slider_image_base64  = encode_image(slider_img)

        if not token:
            # 影刀暂时不支持
            data = yd_recg(slider_image_base64, background_image_base64)
            data = data.get("data")
        else:
            data = recg(token, slider_image_base64, background_image_base64)
        
        if data.get("msg") != "识别成功":
            raise Exception("识别失败, 请重试")

        data_x, data_y = json.loads(data.get("data").get("data"))
        xbot.logging.info(f"Distant:{data_x}, {data_y}")

        # move
        # move to start position

        s_x, s_y, s_w, s_h = web_page.find(slider_ele).get_bounding(to96dpi=True)
        b_x, b_y, b_w, b_h = web_page.find(background_ele).get_bounding(to96dpi=False)
        ppi = get_ppi()
        xbot.win32.mouse_move(int(s_x + s_w/2), int(s_y + s_h/2))
        xbot.win32.mouse_click(button="left", click_type="down")
        xbot.win32.mouse_move(int(s_x + s_w/2 + data_x * ppi), int(s_y + s_h/2 + data_y*ppi))
        xbot.win32.mouse_click(button="left", click_type="up")

        sleep(3)
        if not xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=background_ele):
            break

def main(args):
    web_page = args.get("web_page")
    background_ele = args.get("background_ele")
    slider_ele = args.get("slider_ele")
    retry_count = args.get("retry_count")
    offset = args.get("offset")

    web_page = web.get_active(mode="chrome")
    background_ele = "std_slider_double_background_ele"
    slider_ele = "std_slider_double_slider_ele"
    retry_count = 5
    offset = 0
    token = ""
    handle_captcha(web_page, background_ele, slider_ele, retry_count, offset, token)
