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
from PIL import Image, ImageDraw, ImageOps, ImageChops
from urllib.parse import urlparse

from xbot import print, sleep, win32, web
from .import package  
from .package import variables as glv

from xbot._core import robot 
from .utils import get_xbot_activity_cache_folder, file2base64, get_ppi, start_upload, end_upload,upload_captcha_screenshot, report_data, get_boundary_value

def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")



def yd_captcha_recognition(payload:dict):
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
    conn.request("POST", "/api/openapi/v2/thirdParty/interface/call", res_payload, headers)
    res = conn.getresponse()
    response_data = res.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    # print(response_json)
    data = response_json.get("data")
    if not data:
        raise Exception(f"错误信息: {response_json}")
    return data


def ym_captcha_recognition(payload):
    """请求云码识别验证码"""
    conn = http.client.HTTPConnection("api.jfbym.com")
    headers = { 'Content-Type': 'application/json'}
    # print(payload.get("type"))
    data_json = json.dumps(payload)
    conn.request("POST", "/api/YmServer/customApi", body=data_json, headers=headers)
    response = conn.getresponse()
    response_data = response.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    return response_json



def handle_captcha(web_page:xbot.web.WebBrowser, background_ele , retry_count: int=5, token=""):
    
    current_file_path = __file__  
    current_file_name = os.path.basename(current_file_path) #获得当前文件名
    
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
    if not retry_count: retry_count=5
    background_ele_save_path = os.path.join(cache_folder, "dw_background.png")
    
    background_boundary_list = get_boundary_value(web_page, background_ele)#得到背景图的boundary,锚点


    for i in range(retry_count):
        # upload(web_page)
        x, y, width, height = web_page.find(background_ele).get_bounding(to96dpi=False)
        win32.screenshot.save_screen_to_file(background_ele_save_path, "png", x, y,x+width, y+height)

        background_img_base64 = file2base64(background_ele_save_path)

        payload = { 
            "image": background_img_base64,
            'token': token, 
            'type': "34228"
        }
        
        if token:
            data = ym_captcha_recognition(payload)
        else:
            data = yd_captcha_recognition(payload)
        if data.get("msg") != "识别成功":
            raise Exception("识别失败, 请重试")

        data = data.get("data").get("data")
       

        positions = data.split("|")
        first_picture_x = positions[0].split(',')[0]
        first_picture_y = positions[0].split(',')[1]
        second_picture_x = positions[1].split(',')[0]
        second_picture_y = positions[1].split(',')[1]

        x, y, width, height = web_page.find(background_ele).get_bounding(to96dpi=True)
        first_p_x = x + int(int(first_picture_x) * get_ppi())
        first_p_y = y + int(int(first_picture_y) * get_ppi())
        target_p_x = x + int(int(second_picture_x) * get_ppi())
        target_p_y = y + int(int(second_picture_y) * get_ppi())
        xbot.win32.mouse_move(first_p_x, first_p_y)
        xbot.win32.mouse_click(click_type='down')
        xbot.win32.mouse_move(target_p_x, target_p_y, move_speed='middle')
        xbot.win32.mouse_click(click_type='up')

    
        sleep(2)
        
        if not xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=background_ele):
            try:
                site_url = web_page.get_url()
                captcha_code = '34228'
                report_data(site_url, captcha_url, current_file_name, i + 1, read_url, captcha_code,
                            background_boundary=background_boundary_list)
            except:
                pass 

            break
    

def main(args):
    web_page = args.get("web_page")
    background_ele = args.get("background_ele")
    retry_count = args.get("retry_count",'')
    token = args.get("token")

    # web_page = web.get_active(mode="chrome")
    # upload(web_page)
    # exit()
    
    # background_ele = "dw_capture"
    # token = "8Z23Nm44LCjMKhP18xJNMfHK5lA6TLz4-B3fdA4T1W8"
    handle_captcha(web_page, background_ele, retry_count, token)
