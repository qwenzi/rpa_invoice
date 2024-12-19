import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="process56", package=__name__, inputs={
            "京麦账号": "广州酒家-钟绮梦",
            "京麦密码": "gzjj123456",
            "图鉴账号": "",
            "图鉴密码": "",
            "重试次数": "5",
            "识别引擎": "",
            }, outputs=[
            "保存网页对象",
        ], _block=("测试京麦", 1, "调用流程"))
        # web.get
        # xbot_extensions.activity_ea8fd401.iframeElement
        # workflow.if
        # xbot_extensions.activity_4db973e3.滑动拼图验证（去除界面 bug）
        # programing.log
        # workflow.endif
        # web.get
        # web.element.click
    finally:
        pass
