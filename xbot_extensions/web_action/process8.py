import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        网页对象 = None
    else:
        网页对象 = args.get("网页对象", None)
    try:
        web_page = xbot_visual.process.invoke_module(module="web_page_core", package=__name__, function="get_active_by_web_page", params={
            "web_page": 网页对象,
        }, _block=("获取当前激活的网页对象", 1, "调用模块"))
    finally:
        args["web_page"] = web_page
