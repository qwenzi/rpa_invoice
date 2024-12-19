import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        username = ""
        password = ""
    else:
        username = args.get("username", "")
        password = args.get("password", "")
    try:
        # web.get
        web_page = xbot_visual.process.run(process="xbot_extensions.activity_7bca6d.process7", package=__name__, inputs={
            "mode": "chrome",
            "userid": username.strip(),
            "password": xbot_visual.decrypt(password.strip()),
            "是否退出已登录": True,
            "ym_token": "",
            "加载超时时间": "20",
            "path_to_chrome_exe": "",
            "重试次数": lambda: 5,
            }, outputs=[
            "web_page",
        ], _block=("B登录流程", 2, "淘宝登录"))
        web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("首页_导航栏_财务"), state="appear", iswait=True, timeout="20", _block=("B登录流程", 3, "等待元素(web)"))
        xbot_visual.web.element.click(browser=web_page, element=package.selector("首页_导航栏_财务"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("B登录流程", 4, "点击元素(web)"))
        web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("财务_权限申请"), state="appear", iswait=True, timeout="20", _block=("B登录流程", 5, "等待元素(web)"))
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("财务_权限申请"), text="", _block=("B登录流程", 6, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("财务_权限申请_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("B登录流程", 7, "点击元素(web)"))
        #endif
        xbot_visual.web.element.click(browser=web_page, element=package.selector("首页_导航栏_财务_给买家开票"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("B登录流程", 9, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("B登录流程", 10, "等待"))
    finally:
        pass
