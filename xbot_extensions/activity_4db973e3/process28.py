import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        # 暂时无测试网址
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("测试-图片旋转验证", 2, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info', text=f'第2条指令: {e}')
            time.sleep(3)
        _ = xbot_visual.process.run(process="process15", package=__name__, inputs={
            "验证码图片": package.selector("图片_passmod_spin-background"),
            "滑块元素": package.selector("块元素_passmod_slide-btn"),
            "网页对象": web_page,
            "滑动条": package.selector("拖动左侧滑块使图片为正"),
            "图鉴账号": "",
            "图鉴密码": "",
            "偏移": lambda: 0,
            "是否模拟人工": False,
            }, outputs=[
        ], _block=("测试-图片旋转验证", 3, "调用流程"))
    finally:
        pass
