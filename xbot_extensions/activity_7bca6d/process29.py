import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        # programing.variable
        # workflow.forin
        # process.run
        # workflow.endloop
        _ = xbot_visual.process.run(process="process40", package=__name__, inputs={
            "登录用户名": "1212121212",
            "登录密码": "1212121212",
            "子平台": "",
            "退出已登录账户": True,
            "短信验证码获取接口": "",
            "识别引擎": "",
            }, outputs=[
        ], _block=("测试_京东登录", 5, "调用流程"))
    finally:
        pass
