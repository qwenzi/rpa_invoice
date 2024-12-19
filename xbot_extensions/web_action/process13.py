import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    命令行 = ""
    if args is None:
        禁用图片 = False
        指定端口 = ""
        用户数据 = ""
        指定用户 = ""
        最大化 = False
        无痕模式 = False
        设置UA = ""
        隐藏崩溃弹窗 = False
    else:
        禁用图片 = args.get("禁用图片", False)
        指定端口 = args.get("指定端口", "")
        用户数据 = args.get("用户数据", "")
        指定用户 = args.get("指定用户", "")
        最大化 = args.get("最大化", False)
        无痕模式 = args.get("无痕模式", False)
        设置UA = args.get("设置UA", "")
        隐藏崩溃弹窗 = args.get("隐藏崩溃弹窗", False)
    try:
        命令行 = xbot_visual.process.invoke_module(module="web_page_core", package=__name__, function="chromium_options", params={
            "images_enabled": 禁用图片,
            "port": 指定端口,
            "user_data_dir": 用户数据,
            "profile": 指定用户,
            "hide_crash_restore_bubble": 隐藏崩溃弹窗,
            "user_agent": 设置UA,
            "maximized": 最大化,
            "incognito": 无痕模式,
        }, _block=("浏览器启动配置", 1, "调用模块"))
    finally:
        args["命令行"] = 命令行
