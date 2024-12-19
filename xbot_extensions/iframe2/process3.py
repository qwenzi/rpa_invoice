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
        基于当前lFrame全局查找 = False
        超时时间 = "5"
        属性名称 = ""
    else:
        IFrame对象 = args.get("IFrame对象", None)
        XPath = args.get("XPath", "")
        基于当前lFrame全局查找 = args.get("基于当前lFrame全局查找", False)
        超时时间 = args.get("超时时间", "5")
        属性名称 = args.get("属性名称", "")
    try:
        attribute = xbot_visual.process.invoke_module(module="api", package=__name__, function="get_elem_info", params={
            "iframe_instance": IFrame对象,
            "xpath": XPath,
            "op": "获取元素属性",
            "attr_name": 属性名称,
            "current_global": 基于当前lFrame全局查找,
            "timeout": 超时时间,
        }, _block=("D2-获取元素属性", 1, "调用模块"))
    finally:
        args["attribute"] = attribute
