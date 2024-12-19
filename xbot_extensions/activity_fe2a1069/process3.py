import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="GetShopName", package=__name__, inputs={
            "平台名称": "万相台",
            "web_page": lambda: None,
            }, outputs=[
            "店铺名",
        ], _block=("测试", 1, "调用流程"))
        xbot_visual.programing.log(type="info", text=process_result, _block=("测试", 2, "打印日志"))
    finally:
        pass
