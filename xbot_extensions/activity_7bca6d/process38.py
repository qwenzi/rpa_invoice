import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process21", package=__name__, inputs={
            "浏览器类型": "chrome",
            "账号": "1111111",
            "密码": "2111111111",
            "识别引擎": "影刀引擎(付费增值服务)",
            }, outputs=[
            "网页对象",
        ], _block=("测试_拼多多登录", 1, "调用流程"))
        # web.create
    finally:
        pass
