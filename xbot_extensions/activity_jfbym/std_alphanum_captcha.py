# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
import http
import json
import base64
import os
from io import BytesIO
from xbot import print, sleep, web 
from .import package
from .package import variables as glv
from PIL import ImageGrab
from xbot._core import robot
from .utils import get_xbot_activity_cache_folder, file2base64, get_ppi, start_upload, end_upload,upload_captcha_screenshot, report_data, get_boundary_value


def img_to_base64(image):
    """图片转base64"""
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    base64_string = base64.b64encode(img_bytes).decode('utf-8')
    return base64_string

def get_xbot_client():
    common_info = robot.execute(f'Common.CommonConfig', None)
    return common_info.get("token")

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


def handle_captcha(web_page, ele, token, captcha_type) -> str:
    """处理验证码"""
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
    if isinstance(captcha_type, int):
        captcha_type = int(captcha_type)

    e_x, e_y, e_w, e_h = web_page.find(ele).get_bounding(to96dpi=False)
    xbot.win32.clipboard.clear()
    xbot.win32.screenshot.save_screen_to_clipboard(e_x, e_y, e_x + e_w, e_y + e_h)
    background_img = ImageGrab.grabclipboard()
    xbot.win32.clipboard.clear()
    image_base64  = img_to_base64(background_img)
    payload = { 
        "image": image_base64,
        'token': token, 
        'type': captcha_type
    }
    # xbot.logging.info(payload)
    
    if token:
        data = ym_captcha_recognition(payload)
    else:
        data = yd_captcha_recognition(payload)

    background_boundary_list = get_boundary_value(web_page, ele)#得到拖动滑块的boundary,锚点
    try:
        captcha_code = '100015'
        site_url = web_page.get_url()
        report_data(site_url, captcha_url, current_file_name, 1, read_url, captcha_code,
                    background_boundary=background_boundary_list)
    except:
        pass
        
    return data.get("data").get("data")

def main(args):
    web_page = args.get("web_page")
    ele = args.get("ele")
    captcha_type = args.get("captcha_type")
    token = args.get("token")

    # web_page = web.get_active(mode="chrome")
    # # token = "SoDFyzf09ByPXq98GlxKz3gE1V4wGvm5I2bSNkmf6IY"
    # ele = "std_alphanum_captcha_ele"
    # captcha_type = "10110"
    data = handle_captcha(web_page, ele, token, captcha_type)
    # xbot.logging.info(f"caption code: {data}")
    args["data"] = data
