import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    attribute = ""
    if args is None:
        IFrame对象 = None
        XPath = ""
        操作 = ""
        基于当前lFrame全局查找 = False
        超时时间 = "5"
    else:
        IFrame对象 = args.get("IFrame对象", None)
        XPath = args.get("XPath", "")
        操作 = args.get("操作", "")
        基于当前lFrame全局查找 = args.get("基于当前lFrame全局查找", False)
        超时时间 = args.get("超时时间", "5")
    try:
        attribute = xbot_visual.process.invoke_module(module="api", package=__name__, function="get_elem_info", params={
            "iframe_instance": IFrame对象,
            "xpath": XPath,
            "op": 操作,
            "attr_name": "",
            "current_global": 基于当前lFrame全局查找,
            "timeout": 超时时间,
        }, _block=("D1-获取元素信息", 1, "调用模块"))
    finally:
        args["attribute"] = attribute
