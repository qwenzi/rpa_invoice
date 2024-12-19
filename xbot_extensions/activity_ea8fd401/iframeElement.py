# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep, web
from .import package
from .package import variables as glv

from ._core import IframePage


def main(args):
    try:
        page = args.get("web_page") or web.get_active(mode="chrome")
        xpath = args.get("xpathSelector")

        frame = IframePage(page)
        element = frame.find_ele2(xpath)
        args["元素对象"] = element
        return element
    except Exception as e:
        if args.get("异常处理") == "停止运行":
            raise e 
        else:
            args["元素对象"] = args.get("失败返回值")
            return args.get("失败返回值")
            
