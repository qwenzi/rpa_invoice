import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process42", package=__name__, inputs={
            "账户": "17756164521",
            "密码": "320753691Love..",
            "短信验证码接口": "",
            "退出已登录账户": False,
            "浏览器类型": "chrome",
            }, outputs=[
            "web_page",
        ], _block=("测试_数智登录", 1, "调用流程"))
    finally:
        pass
