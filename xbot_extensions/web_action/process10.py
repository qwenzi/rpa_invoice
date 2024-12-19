import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        保留网页对象 = None
    else:
        保留网页对象 = args.get("保留网页对象", None)
    try:
        invoke_result = xbot_visual.process.invoke_module(module="web_page_core", package=__name__, function="close_other_web_page", params={
            "web_page": 保留网页对象,
        }, _block=("关闭其他网页", 1, "调用模块"))
    finally:
        pass
