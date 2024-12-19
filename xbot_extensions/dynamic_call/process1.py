import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    process_result = None
    if args is None:
        流程名 = ""
        流程参数 = {}
        file_path = __file__
    else:
        流程名 = args.get("流程名", "")
        流程参数 = args.get("流程参数", {})
        file_path = args.get("file_path", __file__)
    try:
        pass
        process_result = xbot_visual.process.invoke_module(module="invoke", package=__name__, function="invoke_process", params={
            "flowname": 流程名,
            "inputs": 流程参数,
            "file_path": file_path,
        }, _block=("动态调用子流程", 1, "调用模块"))
    finally:
        args["process_result"] = process_result