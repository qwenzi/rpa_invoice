import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        网页对象 = None
        操作目标 = None
        保存路径 = ""
    else:
        网页对象 = args.get("网页对象", None)
        操作目标 = args.get("操作目标", None)
        保存路径 = args.get("保存路径", "")
    try:
        invoke_result = xbot_visual.process.invoke_module(module="element_core", package=__name__, function="long_screenshot", params={
            "filepath": 保存路径,
            "web_page": 网页对象,
            "element": 操作目标,
        }, _block=("元素长截图", 1, "调用模块"))
    finally:
        pass
