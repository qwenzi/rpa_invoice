import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        # process.run
        # programing.log
        # process.run
        # process.run
        # process.invoke_module
        # process.run
        # process.run
        # -------------------------
        # web.get
        # web.element.get_element
        # workflow.if
        # web.element.get_details
        # programing.variable
        # web.element.set_attribute
        # workflow.endif
        _ = xbot_visual.process.run(process="HoverByXpath", package=__name__, inputs={
            "web_page": "",
            "xpathSelector": "//*[text()=\"自定义\"]",
            "iframe跨域元素": False,
            "模拟人工": False,
            "等待元素存在": lambda: 5,
            }, outputs=[
        ], _block=("main", 16, "调用流程"))
    finally:
        pass
