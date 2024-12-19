import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("main", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("main", 1,"获取已打开的网页对象"))
            time.sleep(3)
        _ = xbot_visual.process.run(process="module1", package=__name__, inputs={
            "web_page": lambda: web_page,
            "down_elem": package.selector("wew_test"),
            }, outputs=[
        ], _block=("main", 2, "调用流程"))
    finally:
        pass
