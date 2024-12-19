import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("测试_抖店登录", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("测试_抖店登录", 1,"获取已打开的网页对象"))
            time.sleep(3)
        process_result = xbot_visual.process.run(process="process4", package=__name__, inputs={
            "username": "13060336353@163.com",
            "password": "Lj310085",
            "验证邮箱": "",
            "邮箱授权码": "",
            "获取授权码间隔时长": lambda: 20,
            "验证码失败最大重试次数": lambda: 10,
            "退出已登录账户": True,
            "retry_cnt": lambda: 3,
            }, outputs=[
            "web_page",
        ], _block=("测试_抖店登录", 2, "调用流程"))
        web_page_attribute = xbot_visual.web.browser.get_details(browser=process_result.web_page, operation="title", _block=("测试_抖店登录", 3, "获取网页信息"))
    finally:
        pass
