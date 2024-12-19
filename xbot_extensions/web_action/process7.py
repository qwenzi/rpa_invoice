import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        网页对象 = None
        JS库 = ""
    else:
        网页对象 = args.get("网页对象", None)
        JS库 = args.get("JS库", "")
    try:
        invoke_result = xbot_visual.process.invoke_module(module="js_utility", package=__name__, function="import_js_lib", params={
            "web_page": 网页对象,
            "element": "",
            "lib_name": JS库,
        }, _block=("导入常用JS库", 1, "调用模块"))
    finally:
        pass
