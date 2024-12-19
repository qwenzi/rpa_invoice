import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process20", package=__name__, inputs={
            "浏览器类型": "chrome",
            "登录账号": "17756164521",
            "登录密码": "3Aa@",
            "百度OCR账号": "",
            "百度OCR密码": "",
            "重试次数": lambda: 5,
            }, outputs=[
            "web_page",
        ], _block=("测试_支付宝登录", 1, "调用流程"))
    finally:
        pass
