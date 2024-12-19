# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep, win32, web
from .import package
from .package import variables as glv
from xbot_extensions.activity_jfbym import ali_slider_captcha

def login(mode, username, password, token, retry_count):
    url = "https://loginmyseller.taobao.com/"
    web_page = xbot.web.create(url, mode=mode)
    
    xbot.win32.manual_motion_on()
    # web_page = xbot.web.get_active(mode="chrome")
    username_input = web_page.find("qn_uername_input")
    username_input.input(username, force_ime_ENG=True)
    text = username_input.get_text()
    i = 1
    while text != username:
        username_input.clipboard_input(username)
        text = username_input.get_text()
        i += 1
        if i >3:
            raise Exception("输入失败，请手动登录")
    
    password_input = web_page.find("qn_password_input")
    password_input.click()

    if web_page.is_element_displayed('qn_drag_label'):
        refresh_ele = package.selector('qn_refresh')
        drag_ele = package.selector('qn_drag_ele')
        ali_slider_captcha.handle_verification(web_page, token, refresh_ele, drag_ele, retry_count,offset=-30)
    password_input.input(password)
    text = password_input.get_text()
    i = 1
    while text != password:
        password_input.clipboard_input(password)
        text = password_input.get_text()
        i += 1
        if i >3:
            raise Exception("输入失败，请手动登录")
    
    if web_page.is_element_displayed('qn_login_verify'):
        x, y, width, height = web_page.find('qn_slide').get_bounding()
        _, _, verify_width, _ = web_page.find('qn_login_verify').get_bounding()
        pos_center_x = x + width / 2
        pos_center_y = y + height / 2
        move_speed = "middle"
        win32.mouse_move(point_x=pos_center_x, point_y=pos_center_y, move_speed=move_speed)
        win32.mouse_click(button="left", click_type="down", delay_after=0)
        win32.mouse_move(pos_center_x + verify_width, pos_center_y, move_speed=move_speed)
        win32.mouse_click(button="left", click_type="up", )

    web_page.find("qn_login").click()
    xbot.win32.manual_motion_off()

def main(args):
    username = args.get('username','')
    password = args.get('password','yd88888888')
    mode = args.get('mode','chrome')
    token = args.get('token','')
    retry_count = args.get('retry_count',3)
    login(mode, username, password,token, retry_count)
    sleep(2)
    web_page = web.get_active(mode=mode)
    args["web_page"] = web_page
    
