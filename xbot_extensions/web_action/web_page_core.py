# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package
from .package import variables as glv

from .js_utility import execute_javascript

def get_active_by_web_page(web_page):
    product_name = getattr(web_page, "product_name", "cef" if web_page._controller == "CEFBrowser" else "firefox")
    return xbot.web.get_active(mode=product_name)


def close_other_web_page(web_page):
    product_name = getattr(web_page, "product_name", "cef" if web_page._controller == "CEFBrowser" else "firefox")
    web_page_list = xbot.web.get_all(mode=product_name)
    for _web_page in web_page_list:
        if _web_page.bid == web_page.bid:
            continue
        _web_page.close()




def chromium_options(images_enabled, port, user_data_dir, profile, hide_crash_restore_bubble, user_agent, maximized, incognito):
    cmds = []
    if images_enabled:
        cmds.append('--blink-settings=imagesEnabled=false')
    if port:
        cmds.append('--remote-debugging-port="{}"'.format(port))
    if user_data_dir:
        cmds.append('--user-data-dir="{}"'.format(user_data_dir))
    if profile:
        cmds.append('--profile-directory="{}"'.format(profile))
    if hide_crash_restore_bubble:
        cmds.append('hide_crash_restore_bubble')
    if user_agent:
        cmds.append('--user-agent="{}"'.format(user_agent))
    if maximized:
        cmds.append('--start-maximized')
    if incognito:
        cmds.append('--incognito')
    
    return " ".join(cmds)






def main(args):
    web_page = xbot.web.get_active(mode='chrome')
    close_other_web_page(web_page)
    pass
