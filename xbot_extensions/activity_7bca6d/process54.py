import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process5", package=__name__, inputs={
            "username": "13967575592",
            "password": "970305xx",
            "tj_username": "",
            "tj_password": "",
            "web_type": "0",
            }, outputs=[
            "web_page",
        ], _block=("测试_有赞登录", 1, "调用流程"))
    finally:
        pass
