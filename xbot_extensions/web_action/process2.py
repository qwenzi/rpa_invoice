import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        网页对象 = None
        操作目标 = None
    else:
        网页对象 = args.get("网页对象", None)
        操作目标 = args.get("操作目标", None)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="element_core", package=__name__, function="hide_element", params={
            "web_page": 网页对象,
            "element": 操作目标,
        }, _block=("隐藏元素", 1, "调用模块"))
    finally:
        pass
