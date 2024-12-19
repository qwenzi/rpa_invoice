import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("测试-元素可见", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info', text=f'第1条指令: {e}')
            time.sleep(3)
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("抖店_邮箱登录"), _block=("测试-元素可见", 2, "IF 元素可见(web)")):
            xbot_visual.programing.log(type="info", text="11111", _block=("测试-元素可见", 3, "打印日志"))
        #endif
    finally:
        pass
