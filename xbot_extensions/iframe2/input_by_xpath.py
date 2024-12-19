import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        iframe对象 = None
        Xpath = ""
        输入内容 = ""
        追加输入 = False
        输入方式 = ""
        输入内容包含快捷键 = False
        强制加载美式键盘 = False
        按键输入间隔 = "50"
        焦点超时时间 = "1000"
        执行后延迟 = "1"
        输入前点击元素 = True
        全局查找 = False
        超时时间 = "5"
    else:
        iframe对象 = args.get("iframe对象", None)
        Xpath = args.get("Xpath", "")
        输入内容 = args.get("输入内容", "")
        追加输入 = args.get("追加输入", False)
        输入方式 = args.get("输入方式", "")
        输入内容包含快捷键 = args.get("输入内容包含快捷键", False)
        强制加载美式键盘 = args.get("强制加载美式键盘", False)
        按键输入间隔 = args.get("按键输入间隔", "50")
        焦点超时时间 = args.get("焦点超时时间", "1000")
        执行后延迟 = args.get("执行后延迟", "1")
        输入前点击元素 = args.get("输入前点击元素", True)
        全局查找 = args.get("全局查找", False)
        超时时间 = args.get("超时时间", "5")
    try:
        _ = xbot_visual.process.invoke_module(module="api", package=__name__, function="input_by_xpath", params={
            "iframe_instance": iframe对象,
            "xpath": Xpath,
            "text": 输入内容,
            "current_global": 全局查找,
            "simulative": 输入方式,
            "append": 追加输入,
            "contains_hotkey": 输入内容包含快捷键,
            "force_ime_ENG": 强制加载美式键盘,
            "send_key_delay": 按键输入间隔,
            "focus_timeout": 焦点超时时间,
            "delay_after": 执行后延迟,
            "click_before_input": 输入前点击元素,
            "timeout": 超时时间,
        }, _block=("C2-填写输入框", 1, "调用模块"))
    finally:
        pass
