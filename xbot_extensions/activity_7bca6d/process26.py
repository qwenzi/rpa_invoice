import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        账号 = "2477870389@qq.com"
        密码 = "Linjj158813"
        process_result = xbot_visual.process.run(process="process4", package=__name__, inputs={
            "username": 账号,
            "password": 密码,
            }, outputs=[
            "web_page",
        ], _block=("测试抖店登录", 3, "调用流程"))
    finally:
        pass
