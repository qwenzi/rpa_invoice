import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    new_iframe_instance = None
    if args is None:
        iframe_instance = None
        iframe_xpath = ""
        全局查找 = False
        超时时间 = "5"
    else:
        iframe_instance = args.get("iframe_instance", None)
        iframe_xpath = args.get("iframe_xpath", "")
        全局查找 = args.get("全局查找", False)
        超时时间 = args.get("超时时间", "5")
    try:
        new_iframe_instance = xbot_visual.process.invoke_module(module="api", package=__name__, function="to_iframe", params={
            "iframe_instance": iframe_instance,
            "iframe_xpath": iframe_xpath,
            "current_global": 全局查找,
            "timeout": 超时时间,
        }, _block=("A1-切换iframe", 1, "调用模块"))
    finally:
        args["new_iframe_instance"] = new_iframe_instance
