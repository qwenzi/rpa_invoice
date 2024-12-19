import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    new_iframe_instance = None
    if args is None:
        iframe对象 = None
    else:
        iframe对象 = args.get("iframe对象", None)
    try:
        new_iframe_instance = xbot_visual.process.invoke_module(module="api", package=__name__, function="parent", params={
            "iframe_instance": iframe对象,
        }, _block=("A2-切换至父iframe", 1, "调用模块"))
    finally:
        args["new_iframe_instance"] = new_iframe_instance
