import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        iframe对象 = None
        Xpath = ""
        全局查找 = False
        模拟人工点击 = True
        显示鼠标移动轨迹 = False
        鼠标按键 = "left"
        辅助按键 = "none"
        执行后延迟 = "1"
        点击方式 = ""
        超时时间 = "5"
    else:
        iframe对象 = args.get("iframe对象", None)
        Xpath = args.get("Xpath", "")
        全局查找 = args.get("全局查找", False)
        模拟人工点击 = args.get("模拟人工点击", True)
        显示鼠标移动轨迹 = args.get("显示鼠标移动轨迹", False)
        鼠标按键 = args.get("鼠标按键", "left")
        辅助按键 = args.get("辅助按键", "none")
        执行后延迟 = args.get("执行后延迟", "1")
        点击方式 = args.get("点击方式", "")
        超时时间 = args.get("超时时间", "5")
    try:
        _ = xbot_visual.process.invoke_module(module="api", package=__name__, function="click_by_xpath", params={
            "iframe_instance": iframe对象,
            "xpath": Xpath,
            "current_global": 全局查找,
            "button": 鼠标按键,
            "simulative": 模拟人工点击,
            "keys": 辅助按键,
            "move_mouse": 显示鼠标移动轨迹,
            "clicks": 点击方式,
            "delay_after": 执行后延迟,
            "timeout": 超时时间,
        }, _block=("C1-点击元素", 1, "调用模块"))
    finally:
        pass
