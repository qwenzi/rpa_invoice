import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process12", package=__name__, inputs={
            "username": "songpengfei1210@outlook.com",
            "password": "1qaz@WSX3edc",
            "tj_username": "",
            "tj_password": "",
            "web_type": "0",
            }, outputs=[
            "web_page",
        ], _block=("测试巨量纵横登录", 1, "调用流程"))
    finally:
        pass
