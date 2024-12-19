import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("测试", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("测试", 1,"获取已打开的网页对象"))
            time.sleep(3)
        # process.run
        # process.run
        # process.run
        process_result3 = xbot_visual.process.run(process="wait_by_xpath", package=__name__, inputs={
            "iframe对象": web_page,
            "XPath": "//*[@posasa]",
            "等待状态": "appear",
            "超时时间": "10",
            "current_global": False,
            }, outputs=[
            "wait_result",
        ], _block=("测试", 5, "调用流程"))
        # process.run
    finally:
        pass
