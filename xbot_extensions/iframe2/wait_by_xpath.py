import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    wait_result = False
    if args is None:
        iframe对象 = None
        XPath = ""
        等待状态 = ""
        超时时间 = ""
        current_global = False
    else:
        iframe对象 = args.get("iframe对象", None)
        XPath = args.get("XPath", "")
        等待状态 = args.get("等待状态", "")
        超时时间 = args.get("超时时间", "")
        current_global = args.get("current_global", False)
    try:
        wait_result = xbot_visual.process.invoke_module(module="api", package=__name__, function="wait", params={
            "iframe_instance": iframe对象,
            "xpath": XPath,
            "state": 等待状态,
            "current_global": current_global,
            "timeout": 超时时间,
        }, _block=("C3-等待元素", 1, "调用模块"))
    finally:
        args["wait_result"] = wait_result
