import xbot
import os
import xbot_visual
import base64
import json
import base64
import io
import urllib
import http.client
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
from .utils import get_xbot_activity_cache_folder, file2base64, get_ppi

def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")

def ym_captcha_recognition(payload):
    """请求云码识别验证码"""
    conn = http.client.HTTPConnection("api.jfbym.com")
    headers = {'Content-Type': 'application/json'}
    # print(payload.get("type"))
    data_json = json.dumps(payload)
    conn.request("POST",
                 "/api/YmServer/customApi",
                 body=data_json,
                 headers=headers)
    response = conn.getresponse()
    response_data = response.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    return response_json

def yd_recg(image_base64):
    token = get_xbot_client()
    conn = http.client.HTTPSConnection("api.yingdao.com")
    payload = json.dumps({
        "thirdPartyInterfaceCode": "jfbym_20110",
        "data": {},
        "thirdPartyReqData": {
            "headers": {},
            "params": {},
            "body": {
                "image": image_base64
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

def drag(drag_ele:WebElement, distance:int):
    x, y, width, height = drag_ele.get_bounding(to96dpi=False)
    pos_center_x = x + width / 2
    pos_center_y = y + height / 2
    move_speed = "middle"
    win32.manual_motion_on(motion_move=True, motion_click=True, motion_delay=True, min_time=0.1, max_time=0.5)
    win32.mouse_move(point_x=pos_center_x, point_y=pos_center_y, move_speed=move_speed)
    win32.mouse_click(button="left", click_type="down", delay_after=0)
    win32.mouse_move(pos_center_x + distance, pos_center_y, move_speed=move_speed)
    win32.mouse_click(button="left", click_type="up", )
    win32.manual_motion_off()

def handle_captcha(web_page:xbot.web.WebBrowser, background_ele, drag_ele, retry_count: int=5, offset=0):
    
    cache_folder = get_xbot_activity_cache_folder("activity_jfbym")
    xbot.logging.info(f"Cache Dir:{cache_folder}")
    
    if not retry_count: retry_count=5
    
    for i in range(retry_count):
        print(drag_ele)
        drag_element = web_page.find(drag_ele)

        web_page.find(background_ele).screenshot(cache_folder, filename="std_slider.png")

        image_path = os.path.join(cache_folder, "std_slider.png")
        background_ele_base64 = file2base64(image_path)
        # reslut = yd_recg(background_ele_base64)

        # ym_token = "SoDFyzf09ByPXq98GlxKz3gE1V4wGvm5I2bSNkmf6IY"
        # captcha_type = "14106"
        # payload = {"image": background_ele_base64, 'token': ym_token, 'type': captcha_type}
        # reslut = ym_captcha_recognition(payload)

        # print(reslut)
        
        # if reslut.get("msg") != "识别成功":
        #     raise Exception("识别失败, 请重试")
    
        # distance = int(reslut.get("data").get("data")) + int(offset)
        # distance = int(distance * get_ppi()) 
        # xbot.logging.info(f"Distant:{distance}")
        # drag(drag_element, distance)
        # sleep(3)
        # if not xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=background_ele):
        #     break

def main(args):
    web_page = args.get("web_page")
    background_ele = args.get("background_ele")
    slider_ele = args.get("slider_ele")
    retry_count = args.get("retry_count")
    offset = args.get("offset")

    web_page = web.get_active(mode="chrome")
    background_ele = "pdd_background_ele"
    slider_ele = "pdd_slider_ele"
    retry_count = 5
    offset = 0

    handle_captcha(web_page, background_ele, slider_ele, retry_count, offset)
