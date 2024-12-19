import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    invoke_result = None
    if args is None:
        module = ""
        func_name = ""
        inputs = {}
        file_path = __file__
    else:
        module = args.get("module", "")
        func_name = args.get("func_name", "")
        inputs = args.get("inputs", {})
        file_path = args.get("file_path", __file__)
    try:
        pass
        invoke_result = xbot_visual.process.invoke_module(module="invoke", package=__name__, function="invoke_module", params={
            "module": module,
            "func_name": func_name,
            "inputs": inputs,
            "file_path": file_path,
        }, _block=("动态调用模块", 1, "调用模块"))
    finally:
        args["invoke_result"] = invoke_result