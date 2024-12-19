# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package
from .package import variables as glv
import xbot_visual

def sort_file_by_create_time(dir_path):
    return xbot_visual.dir.find_files(path=dir_path, patterns="*.*", find_subdir=False, skip_hidden_file=False, is_sort=True, sort_by="create_time", sort_way="decrease", _block=("__内置指令", 14, "获取文件列表"))

def main(args):
    sort_file_by_create_time(None)
