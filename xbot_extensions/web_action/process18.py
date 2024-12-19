import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        网页对象 = None
    else:
        网页对象 = args.get("网页对象", None)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="element_core", package=__name__, function="remove_zoom", params={
            "web_page": 网页对象,
        }, _block=("取消HTML缩放", 1, "调用模块"))
    finally:
        pass
