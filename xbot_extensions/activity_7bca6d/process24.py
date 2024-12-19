import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process7", package=__name__, inputs={
            "userid": "长缨数码通讯:退款",
            "password": "Tk123456",
            "mode": "chrome",
            "path_to_chrome_exe": "",
            "加载超时时间": "20",
            "ym_token": "",
            "是否退出已登录": True,
            "重试次数": lambda: 5,
            }, outputs=[
            "web_page",
        ], _block=("测试淘宝登录", 1, "调用流程"))
        # process.run
    finally:
        pass
