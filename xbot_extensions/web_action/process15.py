import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        粗细 = "2"
        样式 = ""
        颜色 = ""
        网页对象 = None
        操作目标 = None
    else:
        粗细 = args.get("粗细", "2")
        样式 = args.get("样式", "")
        颜色 = args.get("颜色", "")
        网页对象 = args.get("网页对象", None)
        操作目标 = args.get("操作目标", None)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="element_core", package=__name__, function="add_border", params={
            "web_page": 网页对象,
            "element": 操作目标,
            "width": 粗细,
            "style": 样式,
            "color": 颜色,
        }, _block=("元素增加边框", 1, "调用模块"))
    finally:
        pass
