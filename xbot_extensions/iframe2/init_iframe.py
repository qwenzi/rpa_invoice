import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    iframe_instance = None
    if args is None:
        web_page = None
    else:
        web_page = args.get("web_page", None)
    try:
        iframe_instance = xbot_visual.process.invoke_module(module="api", package=__name__, function="init_iframe", params={
            "web_page": web_page,
        }, _block=("A0-初始化iframe", 1, "调用模块"))
    finally:
        args["iframe_instance"] = iframe_instance
