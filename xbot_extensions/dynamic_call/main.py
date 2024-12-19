import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        invoke_result = xbot_visual.process.invoke_module(module="invoke", package=__name__, function="invoke_module", params={
            "module": "",
            "func_name": "",
            "inputs": "",
            "file_path": "",
        }, _block=("main", 1, "调用模块"))
    finally:
        pass
