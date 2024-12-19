import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process1", package=__name__, inputs={
            "username": "2477870389@qq.com",
            "password": "Linjj158813",
            "tj_username": "",
            "tj_password": "",
            "web_type": "0",
            }, outputs=[
            "web_page",
        ], _block=("测试巨量登录", 1, "调用流程"))
        # process.run
    finally:
        pass
