# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot

import xbot_visual
from xbot_visual.process import run
from xbot import print, sleep
from . import package
from .package import variables as glv
import importlib

import json
import os
import re


file_pattern = re.compile(r"(.+\\apps\\[^\\]+\\(xbot_robot|xbot_extensions\\[^\\]+))")


def find_process_name(source_folder, flowname):

    with open(os.path.join(source_folder, 'package.json'),
              'r',
              encoding='utf-8') as f:
        json_obj = json.loads(f.read())
        flows = json_obj['flows']
        for flow in flows:
            if flow['name'] == flowname:
                filename = flow['filename']
                if filename == 'main':
                    raise ValueError('无法调用主流程')
                return filename
    raise ValueError(f'未找到名为【{flowname}】的流程，请检查！')


def invoke_process(flowname, inputs, file_path):
    """
    调用流程
    """
    if inputs is None or input == "":
        inputs = {}
    source_folder, prefix_path = file_pattern.findall(file_path)[0]
    prefix = prefix_path.replace("\\", ".") + "."
    invoke_process = find_process_name(source_folder, flowname)

    with open(os.path.join(source_folder, invoke_process + ".py"),"r",encoding="u8") as f:
        file_content = f.read()

    res = re.search(r'''(?<=finally:)(?:\n +args\["(.+?)"] = \1)+$''',
                    file_content)
    outputs = []
    if res is not None:
        outputs = re.findall(r'''args\["(.+?)"] = \1''', res.group())

    process_result = run(process=invoke_process, package=prefix + "main", inputs=inputs, outputs=outputs)
    return process_result


def invoke_module(module, func_name, inputs, file_path):
    """
    调用模块
    """
    if inputs is None or input == "":
        inputs = {}    
    source_folder, prefix_path = file_pattern.findall(file_path)[0]
    prefix = prefix_path.replace("\\", ".") + "."
    invoke_result = xbot_visual.process.invoke_module(module=module, package=prefix + "main", function=func_name, params=inputs)
    return invoke_result






def main(args):
    pass

