import xbot
from xbot import print, sleep
from xbot.web import WebElement, WebBrowser
from xbot.selector import Selector

import xbot_visual
import tempfile

from . import package
from enum import Enum
from .package import variables as glv

import os


print = [lambda *_, **__: None, print][__name__.startswith("xbot_robot.")]

class SrcType(Enum):
    Online = "在线地址"
    String = "字符串"
    Filepath = "文件路径"

def execute_javascript(script: str, web_page: WebBrowser = None, element=None):
    """执行JS脚本"""
    if isinstance(element, WebElement):
        res = element.execute_javascript(script)
    elif isinstance(element, xbot.selector.Selector) or isinstance(element, str):
        assert web_page, "传入的元素不是动态元素时，网页对象不能为空"
        element = web_page.find(element)
        res = element.execute_javascript(script)
    else:
        res = web_page.execute_javascript(script)
    return res


class JSUtility:
    def __init__(self, web_page=None, element=None):
        self.web_page = web_page
        self.element = element
        self.resources_dir = os.path.dirname(package.resources.get_path('tool.js'))
        self.lib_dir = os.path.join(tempfile.gettempdir(), 'YdJSLib')        

    def js_eval(self, code):
        code = '''function (element, input) {%s}''' % code
        execute_javascript(code, self.web_page, self.element)


    def read_http_js(self, url):
        file_name = url.split("/")[-1]
        file_path = os.path.join(self.lib_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='u8') as f:
                return f.read()  # .decode()

        kwargs = {"headers": "", "body": None, "save_to_file": False, "save_folder": None, "save_filename": None,
                  "connect_timeout_seconds": "30", "send_by_web": False, "browser": None}
        http_response = xbot_visual.web_service.rest_request(url=url, method="GET", **kwargs)
        assert http_response.status_code == 200, http_response.content
        with open(file_path, 'w', encoding='u8') as f:
            f.write(http_response.content)  # .encode()
        return http_response.content

    def import_js_lib_by_src(self, src, src_type=SrcType.Online.value):
        if src_type == SrcType.String.value:
            code = src
        elif src_type == SrcType.Filepath.value:
            with open(src, 'w') as f:
                code = f.read()
        else:
            code = self.read_http_js(src)
        self.js_eval(code)

    def import_js_lib(self, lib_name):
        lib_path = os.path.join(self.resources_dir, lib_name)
        with open(lib_path, 'r', encoding='u8') as f:
            code = f.read()
            self.js_eval(code)




def import_js_lib(web_page, element, lib_name):
    '''A0 导入常用JS库'''
    js_utility = JSUtility(web_page=web_page, element=element)
    js_utility.import_js_lib(lib_name)



def import_js_lib_by_src(web_page, element, src, src_type):
    '''A1 导入JS库'''
    js_utility = JSUtility(web_page=web_page, element=element)
    js_utility.import_js_lib_by_src(src=src, src_type=src_type)
