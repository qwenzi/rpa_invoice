import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        移动速度 = "middle"
        偏移距离 = 20
    else:
        移动速度 = args.get("移动速度", "middle")
        偏移距离 = args.get("偏移距离", 20)
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("test", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("test", 1,"获取已打开的网页对象"))
            time.sleep(3)
        _ = xbot_visual.process.run(process="process35", package=__name__, inputs={
            "图块所在背景": package.selector("图片_cpc_img"),
            "目标图块": package.selector("图片_small_img"),
            "拖拽元素": package.selector("图片_move-img"),
            "网页对象": lambda: web_page,
            "缺口or单缺口": "单缺口",
            "图鉴帐号": "",
            "图鉴密码": "",
            "重试次数": lambda: 5,
            "偏移距离": lambda: 0,
            "识别引擎": "影刀引擎",
            "移动速度": "middle",
            }, outputs=[
        ], _block=("test", 2, "调用流程"))
    finally:
        pass
