import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    字体颜色 = ""
    if args is None:
        网页对象 = None
        操作目标 = None
    else:
        网页对象 = args.get("网页对象", None)
        操作目标 = args.get("操作目标", None)
    try:
        字体颜色 = xbot_visual.process.invoke_module(module="element_core", package=__name__, function="get_font_color", params={
            "web_page": 网页对象,
            "element": 操作目标,
        }, _block=("获取元素字体颜色", 1, "调用模块"))
    finally:
        args["字体颜色"] = 字体颜色
