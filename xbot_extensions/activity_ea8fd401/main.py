import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        process_result = xbot_visual.process.run(process="iframeElement", package=__name__, inputs={
            "web_page": lambda: None,
            "xpathSelector": "//*[text()=\"业绩分析\"]",
            }, outputs=[
            "元素对象",
        ], _block=("main", 1, "调用流程"))
        xbot_visual.programing.log(type="info", text=process_result.元素对象, _block=("main", 2, "打印日志"))
        xbot_visual.programing.log(type="info", text=lambda: process_result.element.get_text(), _block=("main", 3, "打印日志"))
    finally:
        pass
