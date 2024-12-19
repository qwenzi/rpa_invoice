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
from . import package
from .package import variables as glv

from xbot._core import robot
from .utils import get_xbot_activity_cache_folder, file2base64, get_ppi, start_upload, end_upload, upload_captcha_screenshot, report_data, get_boundary_value
from xbot_extensions import iframe2

def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")


def yd_captcha_recognition(payload: dict):
    """使用增值服务请求验证码"""
    captcha_type = payload.get("type")
    payload.pop("type")

    token = get_xbot_client()
    conn = http.client.HTTPSConnection("api.yingdao.com")
    res_payload = json.dumps({
        "thirdPartyInterfaceCode": f"jfbym_{captcha_type}",
        "data": {},
        "thirdPartyReqData": {
            "headers": {},
            "params": {},
            "body": payload,
            "pathVariable": {}
        },
        "bizType": "rpa-command"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    conn.request("POST", "/api/openapi/v2/thirdParty/interface/call",
                 res_payload, headers)
    res = conn.getresponse()
    response_data = res.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    data = response_json.get("data")
    if not data:
        raise Exception(f"错误信息: {response_json}")
    return data


def ym_captcha_recognition(payload):
    """请求云码识别验证码"""
    conn = http.client.HTTPConnection("api.jfbym.com")
    headers = {'Content-Type': 'application/json'}
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


def drag(drag_ele: WebElement, distance: int):
    x, y, width, height = drag_ele.get_bounding()
    pos_center_x = x + width / 2
    pos_center_y = y + height / 2
    move_speed = "slow"
    win32.manual_motion_on(motion_move=True,
                           motion_click=True,
                           motion_delay=True,
                           min_time=0.5,
                           max_time=2)
    win32.mouse_move(point_x=pos_center_x,
                     point_y=pos_center_y,
                     move_speed=move_speed)
    win32.mouse_click(button="left", click_type="down", delay_after=0)
    win32.mouse_move(pos_center_x + distance,
                     pos_center_y,
                     move_speed=move_speed)
    win32.mouse_click(
        button="left",
        click_type="up",
    )
    win32.manual_motion_off()


def handle_captcha(web_page: xbot.web.WebBrowser,
                   background_ele,
                   drag_ele,
                   retry_count: int = 5,
                   offset=0,
                   token=""):
    current_file_path = __file__
    current_file_name = os.path.basename(current_file_path)  #获得当前文件名

    try:
        captcha_url = web_page.find_by_xpath('//iframe',timeout=3).get_attribute('src')
    except:
        captcha_url = ''
    try:
        read_url = upload_captcha_screenshot(web_page)
    except:
        pass

    cache_folder = get_xbot_activity_cache_folder("activity_jfbym")
    xbot.logging.info(f"Cache Dir:{cache_folder}")

    if not retry_count: retry_count = 5
    save_path = os.path.join(cache_folder, "dy_slider.png")

    background_boundary_list = get_boundary_value(web_page, background_ele)#得到背景图的boundary,锚点
    drag_boundary_list = get_boundary_value(web_page, drag_ele)#得到拖动滑块的boundary,锚点

    for i in range(retry_count):
        drag_element = web_page.find(drag_ele)

        x, y, width, height = web_page.find(background_ele).get_bounding(
            to96dpi=False)
        win32.screenshot.save_screen_to_file(save_path, "png", x, y, x + width,
                                             y + height)

        background_ele_base64 = file2base64(save_path)
        captcha_code = "20225"
        payload = {
            "image": background_ele_base64,
            'token': token,
            'type': captcha_code
        }

        if token:
            data = ym_captcha_recognition(payload)
        else:
            data = yd_captcha_recognition(payload)
        if data.get("msg") != "识别成功":
            raise Exception("识别失败, 请重试")


        distance = int(data.get("data").get("data")) + int(offset)
        distance = int(distance * get_ppi())
        xbot.logging.info(f"Distant:{distance}")
        drag(drag_element, distance)
        sleep(2)
        
        if not xbot_visual.web.browser.element_display(
                browser=web_page, content_type="display",
                selector=background_ele):
            try:
                site_url = web_page.get_url()
                report_data(site_url, captcha_url, current_file_name, i + 1, read_url, captcha_code,
                            background_boundary=background_boundary_list, drag_boundary=drag_boundary_list)
            except:
                pass
            break


def main(args):
    web_page = args.get("web_page")
    background_ele = args.get("background_ele")
    slider_ele = args.get("slider_ele")
    retry_count = args.get("retry_count")
    offset = args.get("offset")
    token = args.get("token")

    # web_page = web.get_active(mode='chrome')
    # background_ele = "std_slider_captcha_background"
    # slider_ele = "std_slider_captcha_drag"
    # retry_count = 5
    # offset = 0

    handle_captcha(web_page, background_ele, slider_ele, retry_count, offset,
                   token)
