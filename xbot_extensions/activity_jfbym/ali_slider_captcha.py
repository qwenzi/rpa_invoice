# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
import xbot_visual
import base64
import json
import base64    
import io
import os
import http.client
from PIL import ImageGrab
import random
import sqlite3
import time
import ast
from xbot_extensions import iframe2
from PIL import Image
from io import BytesIO
from ctypes import windll
from xbot.web.element import WebElement
from xbot.web.chrome import ChromeAutomation

from xbot import print, sleep, win32, web
from .import package
from .package import variables as glv  

from xbot._core import robot
from .utils import get_xbot_activity_cache_folder, file2base64, get_ppi, start_upload, end_upload, get_boundary_value, upload_captcha_screenshot, report_data
import ctypes
from .xtrace import XTrace
from xbot._core import robot

def get_data_by_distance(distance, one=True):
    db_path = xbot_visual.resourcesfile.get_resourcesfile_path(file_name="database.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if distance < 50:
        di = 50
        cursor.execute(f"SELECT * FROM Tracker WHERE distance = 50")
    elif 50 < distance < 150:
        di = 100
        cursor.execute(f"SELECT * FROM Tracker WHERE distance = 100")
    else:
        di = 150
        cursor.execute(f"SELECT * FROM Tracker WHERE distance = 150")

    rows = cursor.fetchall()

    if one:
        random_index = random.randint(0, len(rows) - 1)
        data = json.loads(rows[random_index][2])
        tmp = []
        for item in data:
            tmp.append([item[0], item[1] + random.randint(-2, 2), item[2]])
        # print("rows[random_index][2]:", rows[random_index][2])
        result = ast.literal_eval(rows[random_index][2])
        for i in range(len(result)):
            result[i][0] = result[i][0] / di * distance
        # print("result:", result)
        result = json.dumps(result)
        return json.loads(result)
    return [json.loads(row[2]) for row in rows]

def drag_gen(drag_ele:WebElement, distance:int):
    mouse_pos_path = get_data_by_distance(distance)
    xbot.win32.manual_motion_on()
    drag_ele.hover(simulative=True)
    point_x, point_y = xbot.win32.get_mouse_position()
    win32.mouse_click(button="left", click_type="down")

    for offset_x, offset_y, t in mouse_pos_path:
        print(offset_x, offset_y, t)
        xPoint = point_x + int(offset_x )
        yPoint = point_y + int(offset_y )
        _moveTo(xPoint, yPoint)
        sleep(t/800)
    
    win32.mouse_click(button="left", click_type="up")
    xbot.win32.manual_motion_off()  

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


def drag_g(drag_ele:WebElement, distance:int):
    trace = XTrace()
    _, mouse_pos_path = trace.get_mouse_pos_path(distance)
    x, y, width, height = drag_ele.get_bounding(to96dpi=True)
    point_x = x+ int(width/2)
    point_y = y+ int(height/2)
    win32.mouse_move(point_x=point_x, point_y=point_y, move_speed="middle")
    win32.mouse_click(button="left", click_type="down")

    for offset_x, offset_y, t in mouse_pos_path:
        xPoint = point_x + int(offset_x )
        yPoint = point_y + int(offset_y )
        _moveTo(xPoint, yPoint)
        sleep(t/1000)
    
    win32.mouse_click(button="left", click_type="up")


def join_images(image1, image2):
    """图片拼接"""
    width1, height1 = image1.size
    width2, height2 = image2.size
    new_image = Image.new('RGB', (max(width1, width2), height1+height2 +11), (255, 255, 255))
    new_image.paste(image1, (0, 0)) 
    new_image.paste(image2, (0, height1+11))
    return new_image


def encode_image(image):
    """图片转base64"""
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    base64_string = base64.b64encode(img_bytes).decode('utf-8')
    return base64_string


def decode_image(base64_string):
    """字符串转图片"""
    missing_padding = len(base64_string) % 4
    if missing_padding:
        base64_string += '=' * (4 - missing_padding)
    img_data = base64.b64decode(base64_string)
    img = Image.open(BytesIO(img_data))
    return img.convert('RGBA')


def get_ppi():
    """
    获取屏幕的缩放
    """
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    user32 = windll.user32
    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)   
    pix_per_inch = windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    res = float.as_integer_ratio(round(pix_per_inch / 96,2))
    return res[1]/res[0]


def recg(token, base64_im):
    """请求云码识别淘"""
    conn = http.client.HTTPConnection("api.jfbym.com")
    headers = { 'Content-Type': 'application/json'}
    data = { 'image': base64_im, 'token': token, 'type': 20226 }
    data_json = json.dumps(data)
    conn.request("POST", "/api/YmServer/customApi", body=data_json, headers=headers)
    response = conn.getresponse()
    response_data = response.read().decode('utf-8')
    response_json = json.loads(response_data)
    conn.close()
    return response_json


def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")

def yd_recg(base64_im):
    token = get_xbot_client()
    conn = http.client.HTTPSConnection("api.yingdao.com")
    payload = json.dumps({
        "thirdPartyInterfaceCode": "jfbym_20226",
        "data": {},
        "thirdPartyReqData": {
            "headers": {},
            "params": {},
            "body": {
            "image": base64_im
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


def drag(drag_ele:WebElement, distance:int, speed="middle"):
    x, y, width, height = drag_ele.get_bounding()
    pos_center_x = x + width / 2 + random.randint(-5, 5)
    pos_center_y = y + height / 2 + random.randint(-5, 5)

    move_speed = speed

    win32.manual_motion_on()
    win32.mouse_move(point_x=pos_center_x, point_y=pos_center_y, move_speed="instant")
    poit_x, point_y = win32.get_mouse_position(relative_to="screen")
    win32.mouse_click(button="left", click_type="down", delay_after=0)

    right_offset = random.randint(-5, 5)
    left_offset = random.randint(-5, 5)

    win32.mouse_move(pos_center_x + distance + right_offset, pos_center_y, move_speed="fast", delay_after=0)
    win32.mouse_move(pos_center_x + distance - left_offset, pos_center_y, move_speed=move_speed,  delay_after=0)
    win32.mouse_move(pos_center_x + distance, pos_center_y, move_speed=move_speed,  delay_after=0)
    win32.mouse_click(button="left", click_type="up", delay_after=0)
    win32.manual_motion_off()
    


def relative_drag(distance:int,move_speed = "fast", up_flag=True):
    poit_x, point_y = win32.get_mouse_position(relative_to="screen")
    win32.mouse_click(button="left", click_type="down")
    win32.manual_motion_on()
    win32.mouse_move(poit_x + distance, point_y, move_speed=move_speed)
    win32.manual_motion_off()
    if up_flag:
        win32.mouse_click(button="left", click_type="up")


def get_web_page_by_web_page(web_page):
    product_name = getattr(web_page, "product_name", "cef" if web_page._controller == "CEFBrowser" else "firefox")
    return xbot.web.get_active(mode=product_name)


def handle_verification(web_page: web.WebBrowser, token:str, refresh_ele: WebElement,drag_ele:WebElement,retry_count: int, offset=0, monitor_time=3, speed="middle"):
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

    _, _, drag_width, _ = web_page.find(drag_ele).get_bounding(to96dpi=True)

    if not retry_count: retry_count=5
    if not monitor_time: monitor_time=3

    drag_boundary_list = get_boundary_value(web_page, drag_ele)#得到拖动滑块的boundary,锚点

    for i in range(retry_count):
        xbot.logging.info(f"第 {i+1} 识别验证码")
        web_page.start_monitor_network( resource_type="Image")
        refresh_element = web_page.find(refresh_ele)
        refresh_element.click(delay_after=0, simulative=False)
        sleep(monitor_time)
        res_list = web_page.get_responses(resource_type="Image")
        web_page.stop_monitor_network()

        tip_images_base64 = []
        background_image_base64 = None

        try:
        
            for res_item in res_list:
                image_base64: str = res_item.get("url")
                if image_base64.startswith("https://"): continue
                img = decode_image(image_base64.split(",", 1)[-1])
                width, height = img.size

                if height == 180:
                    background_image_base64 = image_base64
                if height == 30:
                    tip_images_base64.append(image_base64)
        
        except Exception as e:
            continue

        if not (tip_images_base64 or background_image_base64):
            """
            默认当作成功通过情况
            """
            break

        distance = None

        for index, tip_image_base64 in enumerate(tip_images_base64):
            tip_image = decode_image(tip_image_base64.split(",", 1)[-1])
            background_image = decode_image(background_image_base64.split(",", 1)[-1])
            captcha_image: Image = join_images(tip_image, background_image)

            cache_folder = get_xbot_activity_cache_folder("activity_jfbym")
            ali_image_captcha_path = os.path.join(cache_folder, f"ali_image_captcha{i}{index}.png")
            xbot.logging.info(f"Cache ALI Captcha Image Path: {ali_image_captcha_path}" )
            with open(ali_image_captcha_path, "wb") as f:
                captcha_image.save(f)

            captcha_image_base64 = encode_image(captcha_image)


            if token:
                reslut = recg(token, captcha_image_base64)
            else:
                reslut = yd_recg(captcha_image_base64).get("data")
            if reslut.get("msg") != "识别成功":
                print("识别失败, 请重试, 本次不计费")
                continue
            else:
                distance = reslut.get("data").get("data")
                break

            
        xbot.logging.info(f"Distance: {distance}")

        
        if distance:
            distance = int((int(distance) - drag_width / 5 * 3 + offset))

            # 处理跨域下 img 显示非 320 的场景
            init_iframe = iframe2.init_iframe(web_page)
            try:
                init_iframe = iframe2.to_iframe(init_iframe, "//iframe[@id='alibaba-login-box']", False, 3)
                iframe_web_page = iframe2.to_iframe(init_iframe, "//iframe[@id='baxia-dialog-content']", False, 3)
                backgroud_img_ele = iframe_web_page.find_ele("//div[@class='scratch-captcha-container']")
                backgroud_img_ele_width = backgroud_img_ele.get_attribute('style')
                backgroud_img_ele_width_value = backgroud_img_ele_width.split(':')[1].split('p')[0]
                distance *= int(backgroud_img_ele_width_value) / 320
            except:
                pass    
        
            print(f"distance: {distance}")
            
            drag_element = web_page.find(drag_ele)
            drag(drag_element, distance, speed=speed)

            web_page = get_web_page_by_web_page(web_page)
            web_page.wait_disappear(drag_ele, 3)
        if refresh_element.is_displayed() == False:
            try:
                captcha_code = "20226"
                site_url = web_page.get_url()
                report_data(site_url, captcha_url, current_file_name, i + 1, read_url, captcha_code,
                            drag_boundary=drag_boundary_list)
            except:
                pass
            break
    

def main(args):
    web_page = args.get("web_page")
    token = args.get("ym_token")
    drag_ele = args.get("drag_ele")
    refresh_ele = args.get("refresh_ele")
    retry_count = args.get("retry_count")
    offset = args.get("offset")
    monitor_time = args.get("monitor_time", 1)
    speed = args.get("speed", "fast")

    # web_page = web.get_active(mode="chrome")
    # retry_count = 5
    # offset = 0
    # drag_ele = 'ali_slider_captcha_ele'
    # refresh_ele = 'ali_slider_back_refresh_ele'
    handle_verification(web_page, token, refresh_ele, drag_ele, retry_count, offset, monitor_time, speed)
    pass
