import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_element_list = []
    if args is None:
        iframe_instance = None
        xpath = ""
        全局查找 = False
        超时时间 = "5"
    else:
        iframe_instance = args.get("iframe_instance", None)
        xpath = args.get("xpath", "")
        全局查找 = args.get("全局查找", False)
        超时时间 = args.get("超时时间", "5")
    try:
        web_element_list = xbot_visual.process.invoke_module(module="api", package=__name__, function="find_all_ele", params={
            "iframe_instance": iframe_instance,
            "xpath": xpath,
            "current_global": 全局查找,
            "timeout": 超时时间,
        }, _block=("B2-获取相似元素", 1, "调用模块"))
    finally:
        args["web_element_list"] = web_element_list
