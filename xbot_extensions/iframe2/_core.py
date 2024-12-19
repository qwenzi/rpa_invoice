# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package
from .package import variables as glv

from .js_code import getElementByXpath, getElementsByXpath, getShadowRootByJsPath, getShadowRootByXpath
import os, re
import time


print = [lambda *_, **__: None, print][__package__ == "xbot_robot" or hasattr(xbot, "__log")]


def check_obj(func):
    def wrapper(*args, **kwargs):
        iframe_instance = kwargs['iframe_instance']
        if not isinstance(iframe_instance, IframePage):
            kwargs['iframe_instance'] = IframePage(iframe_instance)
        res = func(*args, **kwargs)
        return res
    return wrapper


def timeout(func):

    def wrapper(*args, **kwargs):
        if 'timeout' not in kwargs.keys():
            return func(*args, **kwargs)
        self = args[0]
        timeout_ = kwargs['timeout']
        if timeout_ is None: timeout_ = 1

        timeout_ = int(timeout_)
        start = time.time()
        is_first = True
        result = None
        while True:
            is_first = False
            try:
                # 执行被装饰的函数
                self.web_page.wait_load_completed(timeout=timeout_)
                result = func(*args, **kwargs)
                if isinstance(result, list) and len(result) == 0: raise Exception("未找到元素")
                return result
            except Exception as e:
                if "未加载完成" in str(e) or "加载超时" in str(e) or "加载失败" in str(e):
                    if time.time() - start >= timeout_:
                        if func.__name__ == "find_all_ele": return []
                        raise
                    continue
                if e.args[0] in ["在多个iframe中找到元素，无法唯一确定", "找到多个元素，无法唯一确定", "找到多个iframe，无法唯一确定", "未找到元素", "未找到指定ID的元素"]:
                    if time.time() - start >= timeout_:
                        if isinstance(result, list): return result
                        raise
                    continue
                raise
    return wrapper





class IframePage:
    def __init__(self, web_page, html=None, path=[]):
        self.web_page = web_page
        
        self.html = web_page if html is None else html
        # self.iframe_id = self.get_iframe_id()
        self.path = path
        self.is_shadow_root = True
        if len(path) == 0:
            self.is_shadow_root = False
        
        elif path[-1]['name'].lower() == "iframe" or path[-1]['name'].lower() == "frame":
            self.is_shadow_root = False

        # 反射网页对象方法
        for attr in dir(self.web_page):
            if hasattr(self, attr): continue
            setattr(self, attr, getattr(self.web_page, attr))

    
    def get_iframe_id(self):
        if self.html == self.web_page: return 0
        return self.html.get_attribute('uia-uid').split("|")[0]


    def find_all_iframe(self, result=[]):
        if len(result) == 0: result.append(self)
        iframe_page_list = self.find_all_ele("//iframe|//frame", True)
        for iframe_page in iframe_page_list:
            result.append(iframe_page)
            iframe_page.find_all_iframe(result)
    
    def to_iframe(self, xpath, current_global=False, timeout=5):
        return self.find_ele(xpath, True, current_global, timeout=timeout)


    def to_shadow_root(self, js_path):
        iframe_page = self      
        if isinstance(js_path, list):
            for xpath_path in js_path:
                if not iframe_page.is_iframe:
                    xpath_path = ".." + xpath_path
                result = iframe_page.html.execute_javascript(getShadowRootByXpath, xpath_path)
                if isinstance(result, str):
                    raise Exception(result, xpath_path)

                path, tagName = result
                path[0]['attributes'] = []
                path.append({'name': 'xbotShadowRoot', 'type': 'web', 'attributes': []})
                path.append({'name': tagName, 'type': 'web', 'attributes': []})
                path = iframe_page.path + path
                value = {"name":"iframe", "type":"simple", "path": path}   
                ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
                path = path[:-1]
                iframe_page = IframePage(self.web_page, ele, path)
            return iframe_page



        js_paths = re.split(r'(?=\.shadowRoot\.query)', js_path)
        
        if len(js_paths) == 1:
            return self

        tag_path = ""
        paths = iframe_page.path
        for i, temp_path in enumerate(js_paths[:-1]):
            tag_path += temp_path
            temp_code = getShadowRootByJsPath % tag_path
            result = iframe_page.html.execute_javascript(temp_code)
            if isinstance(result, str):
                raise Exception(result, temp_path)

            path, tagName = result
            path[0]['attributes'] = []
            paths = paths + path
            paths.append({'name': 'xbotShadowRoot', 'type': 'web', 'attributes': []})
            paths.append({'name': tagName, 'type': 'web', 'attributes': []})
            value = {"name":"iframe", "type":"simple", "path": paths}
            ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
            paths = paths[:-1]
        iframe_page = IframePage(self.web_page, ele, paths)
        return iframe_page


    @timeout
    def find_ele(self, xpath, is_iframe=False, current_global=False, timeout=5):
        if isinstance(xpath, list):
            iframe_page = self
            for x in xpath[:-1]:
                iframe_page = iframe_page.find_ele(x, True, False)
            
            return iframe_page.find_ele(xpath[-1], is_iframe, False)


        if current_global:
            # 全局查找
            iframe_page_list = []
            self.find_all_iframe(iframe_page_list)
            print(iframe_page_list)
            total, ele = 0, None
            for iframe_page in iframe_page_list:
                try:
                    print(iframe_page.html)
                    ele = iframe_page.find_ele(xpath, is_iframe)
                    total += 1
                    if total > 1:
                        raise Exception("在多个iframe中找到元素，无法唯一确定", xpath)
                except Exception as e:
                    if e.args[0] == "找到多个元素，无法唯一确定" or e.args[0] == "在多个iframe中找到元素，无法唯一确定":
                        if is_iframe:
                            raise Exception("找到多个iframe，无法唯一确定", xpath)
                        raise
            if total == 1:
                return ele
            if total == 0:
                raise Exception("未找到元素", xpath)


        if self.is_shadow_root:
            xpath = ".." + xpath
        path = self.html.execute_javascript(getElementByXpath, xpath)
        if isinstance(path, str):
            raise Exception(path, xpath)

        if self.is_shadow_root:
            path[0]['attributes'][0]['required'] = False              
        path = self.path + path



        if is_iframe:
            path.append({"name":"html","type":"web","attributes": []})
            value = {"name":"iframe", "type":"simple", "path": path}
            ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
            path = path[:-1]
            return IframePage(self.web_page, ele, path)
        
        value = {"name":"iframe", "type":"simple", "path": path}
        ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
        return ele
    
    @timeout
    def find_all_ele(self, xpath, is_iframe=False, current_global=False, timeout=timeout):

        if isinstance(xpath, list):
            iframe_page = self
            for x in xpath[:-1]:
                iframe_page = iframe_page.find_ele(x, True, False)
            
            return iframe_page.find_all_ele(xpath[-1], is_iframe, False)        

        if current_global:
            total = 0
            eles2 = []
            list_iframe_page = []
            self.find_all_iframe(list_iframe_page) 
         
            for iframe_page in list_iframe_page:
                temp_eles = iframe_page.find_all_ele(xpath, is_iframe)
                if len(temp_eles) != 0:
                    total += 1
                    eles2 = temp_eles
                if total > 1:
                    raise Exception("在多个iframe中找到相似元素，无法唯一确定", xpath)
            return eles2

        paths = self.html.execute_javascript(getElementsByXpath, xpath)
        eles = []
        for path in paths:
            if self.is_shadow_root:
                path[0]['attributes'][0]['required'] = False            
            path = self.path + path

            if is_iframe:
                path.append({"name":"html","type":"web","attributes": []})
                value = {"name":"iframe", "type":"simple", "path": path}
                ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
                path = path[:-1]
                eles.append(IframePage(self.web_page, ele, path))
            else:
                value = {"name":"iframe", "type":"simple", "path": path}
                ele = self.web_page.find(xbot.selector.Selector(value), timeout=0)
                eles.append(ele)
        return eles


    def click_by_xpath(self, xpath, current_global,*,button,simulative,move_mouse,clicks, keys, delay_after,timeout):
        delay_after=float(delay_after)
        ele = self.find_ele(xpath, False, current_global,timeout=timeout)
        if clicks != "双击":
            ele.click(button=button, simulative=simulative, keys=keys, move_mouse=move_mouse, delay_after=delay_after)
        else:
            ele.dblclick(simulative=simulative, move_mouse=move_mouse, delay_after=delay_after)
        
    def input_by_xpath(self, xpath, text, *,current_global=False, simulative=True, append=False, contains_hotkey=False, force_ime_ENG=False, send_key_delay=50, focus_timeout=1000, delay_after=1, click_before_input=True,timeout=5):
        focus_timeout=float(focus_timeout)
        delay_after=float(delay_after)
        send_key_delay=float(send_key_delay)
        ele = self.find_ele(xpath, False, current_global,timeout=timeout)
        if simulative == "剪贴板输入":
            ele.clipboard_input(text, append=append, focus_timeout=focus_timeout, delay_after=delay_after, send_key_delay=send_key_delay, click_before_input=click_before_input)
        else:
            simulative = False if simulative == "自动化接口输入" else True
            ele.input(text, simulative=simulative, append=append, contains_hotkey=contains_hotkey, force_ime_ENG=force_ime_ENG,send_key_delay=send_key_delay,focus_timeout=focus_timeout,delay_after=delay_after,click_before_input=click_before_input)
            code = """
            function a(ele, _) {
                ele.dispatchEvent(new InputEvent('input', {
                    bubbles: true,
                    cancelable: true,
                }));
            }  
            """
            try:
                ele.execute_javascript(code)
            except:
                pass


    def execute_javascript(self, code, argument=None, execution_world="ISOLATED"):
        """跨域执行JS脚本"""
        return self.html.execute_javascript(code, argument, execution_world=execution_world)

    def wait(self, xpath, state="appear", current_global=False, timeout=20):
        """等待元素"""
        if timeout is None or timeout == "":
            timeout = -1
        timeout = int(timeout)
        if state != "appear":
            # 等待元素消失
            start = time.time()
            while True:
                try:
                    eles = self.find_all_ele(xpath=xpath, current_global=current_global, timeout=0.5)
                    if len(eles) == 0:
                        return True
                    if timeout == -1:
                        continue                    
                    if time.time() - start >= timeout:
                        return False
                except Exception as e:
                    if '未找到元素' not in str(e):
                        raise
                    
                    if time.time() - start >= timeout:
                        return False


        # 等待元素出现
        while True:
            eles = self.find_all_ele(xpath=xpath, current_global=current_global, timeout=timeout)
            if len(eles) == 0 and timeout == -1: continue
            return len(eles) != 0