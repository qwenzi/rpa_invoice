import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        网页对象 = None
        JS来源类型 = ""
        JS来源 = ""
    else:
        网页对象 = args.get("网页对象", None)
        JS来源类型 = args.get("JS来源类型", "")
        JS来源 = args.get("JS来源", "")
    try:
        invoke_result = xbot_visual.process.invoke_module(module="js_utility", package=__name__, function="import_js_lib_by_src", params={
            "web_page": 网页对象,
            "element": "",
            "src": JS来源,
            "src_type": JS来源类型,
        }, _block=("导入JS库", 1, "调用模块"))
    finally:
        pass
