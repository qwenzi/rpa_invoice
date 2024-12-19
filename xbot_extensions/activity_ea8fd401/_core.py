# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from . import package



from .package import _selector_store, selector, resources
from .package import variables as glv

from xbot.selector import SelectorStore, ImageSelectorStore
from xbot.primitives import VariableDict, ResourceReader, _sdmodules
import xml.etree.ElementTree as ET

import os, re
import time


print = lambda *_, **__: None 

def get_uid(uids=[]):
    uid = str(int(time.time() * 1000))
    if uid in uids:
        uid = str(int(time.time() * 1000))  
    return uid    


class IframePage:
    def __init__(self, web_page, iframe=None, uids=[], iframe_page_list=[]):
        self.web_page = web_page
        self.iframe = web_page if iframe is None else iframe
        self.iframe_page_list = iframe_page_list
        self.uids = uids
        self.resources_path = os.path.join(os.path.dirname(__file__), "resources")
        self.selectors_path = os.path.join(self.resources_path, "selectorsV2.xml")
        self.init_resources()
        SelectorStore(self.resources_path)

    def init_resources(self):
        """初始化资源文件"""
        images_path = os.path.join(self.resources_path, "imagesV2.xml")
        images_xml_str = """
        <?xml version="1.0" encoding="utf-8"?>
        <repository xmlns:x="rpa://imageselector/core">
        </repository>
        """
        selectors_xml_str = """
        <?xml version="1.0" encoding="utf-8"?>
        <repository xmlns:x="rpa://selector/core" xmlns:regex="rpa://selector/operator/regex" xmlns:wildcard="rpa://selector/operator/wildcard">
        </repository>  
        """
        with open(images_path, "w", encoding="u8") as f:
            f.write(images_xml_str.strip())

        with open(self.selectors_path, "w", encoding="u8") as f:
            f.write(selectors_xml_str.strip())



    def create_ele_libs(self, tag_name, uids, new_uid=None):
        """创建元素库"""
        root = ET.Element("repository")
        root.set("xmlns:x", "rpa://selector/core")
        root.set("xmlns:regex", "rpa://selector/operator/regex")
        root.set("xmlns:wildcard", "rpa://selector/operator/wildcard")

        group_attrib = {"id": "驿站", "name": "iframe", "type": "Web"}
        group_node = ET.SubElement(root, "group", group_attrib)
        selector_node_attrib = {"name": "list-iframe", "type": "simple"}
        selector_node = ET.SubElement(group_node, "selector", selector_node_attrib)
        for uid in uids:
            ET.SubElement(selector_node, "web", {
                "x:name": "iframe",
                "diy-uid": uid
            })
        if new_uid is None:
            web_attrib = {"x:name": tag_name}
        else:
            web_attrib = {"x:name": tag_name, "diy-uid": new_uid}
        ET.SubElement(selector_node, "web", web_attrib)
        tree = ET.ElementTree(root)
        tree.write(self.selectors_path, encoding="utf-8", xml_declaration=True)

    def read_ele(self, single=True):
        """读取元素"""
        _selector = SelectorStore(self.resources_path)("list-iframe")
        if single:
            return self.web_page.find(_selector, timeout=0)
        return self.web_page.find_all(_selector, timeout=0)


    def to_iframe(self, xpath, find_descendant_iframe=False):
        """
        通过xpath切换到iframe
        """
        
        if find_descendant_iframe:
            total = 0
            list_iframe_page = self.find_all_iframe()
            new_iframe_page = None
            for iframe_page in list_iframe_page:
                try:
                    new_iframe_page = iframe_page.to_iframe(xpath)
                    if total != 0:
                        raise Exception("找到多个iframe元素，无法唯一定位")
                    total += 1
                except Exception as e:
                    msg = e.args[0]
                    if msg == "找到多个元素，无法唯一定位" or msg == "找到多个iframe元素，无法唯一定位":
                        raise
            
            if new_iframe_page is None:
                raise Exception("未找到元素")
            
            return new_iframe_page

        iframe_ele = self.find_ele(xpath, True)
        uids = self.uids.copy()
        return IframePage(self.web_page, iframe_ele, uids)


    def find_ele(self, xpath, is_iframe=False):
        """
        获取元素对象
        """
        uid = None
        if self.iframe != self.web_page:
            self.create_ele_libs("html", self.uids)
            html_ele = self.read_ele()
            code = """
            function (element, xpath) {
                
                $x = (xpath) => {
                    try {
                        let xpathResult = document.evaluate(xpath, element, null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); 
                        let nodes = []
                        let node = null               
                        while (node = xpathResult.iterateNext()) {
                            nodes.push(node)
                        }
                        return nodes
                    } catch (error) {
                        return []
                    }

                }                
                eles = $x(xpath)
                
                if (eles.length > 1) {
                    return ["", "", "找到多个元素，无法唯一定位"]
                }
                if (eles.length == 0) {
                    return ["", "", "未找到元素"]
                }
                ele = eles[0]
                
                uid = ele.getAttribute("diy-uid")
                if (uid == null || uid == "") {
                    uid = new Date().getTime().toString()
                    ele.setAttribute("diy-uid", uid)
                }
                return [uid, ele.tagName, "成功"]
            }
            """
            uid, tag_name, msg = html_ele.execute_javascript(code, xpath)
            if msg != "成功":
                raise Exception(msg)
            self.create_ele_libs(tag_name, self.uids, uid)
            ele = self.read_ele()
        else:
            ele = self.web_page.find_by_xpath(xpath, timeout=1)
            uid = get_uid()
            ele.set_attribute("diy-uid", uid)
        
        if is_iframe:
            self.uids.append(uid)

        return ele


    def find_ele2(self, xpath):
        """
        获取元素对象-跨多层iframe
        """
        print(xpath)

        iframe_page_list = self.find_all_iframe()
        eles = []
        for iframe_page in iframe_page_list:
            try:
                ele = iframe_page.find_ele(xpath)
                eles.append(ele)
            except:
                pass

        if len(eles) == 1:
            return eles[0]
        if len(eles) == 0:
            raise Exception("未找到元素")
        raise Exception("找到多个元素，无法唯一定位")


    def find_all_iframe(self):
        """基于当前iframe 查找所有后代 iframe (包含自身)"""
        uids = self.uids.copy()
        if len(self.uids) == 0:
            iframe_eles = self.web_page.find_all_by_xpath("//iframe", timeout=0.1)
        else:
            # uid = get_uid()
            self.create_ele_libs("iframe", uids)
            # uids.append(uid)           
            iframe_eles = self.read_ele(False)
        
        iframe_page_list = [self]
        self._find_all_iframe(iframe_eles, uids, iframe_page_list)
        print("iframe_page_list", len(iframe_page_list))
        return iframe_page_list     


    def _find_all_iframe(self, iframe_eles, uids, iframe_page_list):
        if len(iframe_eles) == 0:
            return
        for iframe_ele in iframe_eles:
            uid = iframe_ele.get_attribute("diy-uid")
            print("id", iframe_ele.get_attribute("id"))
            if uid is None or uid == "":
                uid = get_uid()
                iframe_ele.set_attribute("diy-uid", uid)
            uids.append(uid) 
            iframe_page = IframePage(self.web_page, iframe_ele, uids.copy())
            iframe_page_list.append(iframe_page)


            self.create_ele_libs("iframe", uids)
            iframe_eles = self.read_ele(False)
            
            self._find_all_iframe(iframe_eles, uids, iframe_page_list)
            uids.pop(-1)


    def find_all_ele(self, xpath, find_descendant_iframe=False):
        """
        获取相似元素列表
        """ 
        eles = []
        code = """
        function (element, xpath) {
            function $x(xpath) {
                let xpathResult = document.evaluate(xpath, element, null, XPathResult.ORDERED_NODE_ITERATOR_TYPE, null); 
                let nodes = []
                let node = null               
                while (node = xpathResult.iterateNext()) {
                    nodes.push(node)
                }
                return nodes     
            }

            function get_uid(uids) {
                let uid = new Date().getTime().toString()
                while (uids.includes(uid)) {
                    uid += "0"
                }
                return uid
            }         
            let uids = []
            ele_info = []                
            eles = $x(xpath)
            for (let i = 0; i < eles.length; i++) {
                let ele = eles[i]
                let uid = ele.getAttribute("diy-uid")
                if (uid == null || uid == "") {
                    uid = get_uid(uids)
                    ele.setAttribute("diy-uid", uid)
                }
                uids.push(uid)
                ele_info.push([uid, ele.tagName])
            }
            return ele_info
        }
        """

        if find_descendant_iframe:
            total = 0
            eles = []
            list_iframe_page = self.find_all_iframe()            
            for iframe_page in list_iframe_page:
                temp_eles = iframe_page.find_all_ele(xpath)
                if len(temp_eles) != 0:
                    total += 1
                    eles = temp_eles
                if total > 1:
                    raise Exception("在多个iframe中找到相似元素，无法唯一定位")
            return eles


        if self.iframe != self.web_page:
            uids = self.uids.copy()
            self.create_ele_libs("html", uids)
            html_ele = self.read_ele()
            ele_info = html_ele.execute_javascript(code, xpath)
            for uid, tag_name in ele_info:
                self.create_ele_libs(tag_name, uids, uid)
                ele = self.read_ele()
                eles.append(ele)
        else:
            eles = self.web_page.find_all_by_xpath(xpath, timeout=3)
        return eles



def main(args):
    web_page = xbot.web.get("*", mode='edge', use_wildcard=True)

    iframe_page = IframePage(web_page)
    # //*[@id="s_filter_frame"]
    # iframe_page = iframe_page.to_iframe('//*[@id="form1"]/div[7]/div[2]/table/tbody/tr/td[1]/iframe', find_descendant_iframe=True)
    # iframe_page.find_ele('//*[@id="as_id"]')


    # ###### 示例一
    # # 初始化iframe处理器
    # iframe_page = IframePage(web_page)

    # # 切换iframe
    # iframe_page = iframe_page.to_iframe('//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')
    # iframe_page = iframe_page.to_iframe('//*[@id="ptlogin_iframe"]')

    # # 查找元素
    # name_ele = iframe_page.find_ele('//*[@id="u"]')
    # name_ele.input("23124325")


    # ###### 示例二
    # # 初始化iframe处理器
    # iframe_page = IframePage(web_page)

    # # 跨层级切换iframe
    # iframe_page = iframe_page.to_iframe('//*[@id="ptlogin_iframe"]', find_descendant_iframe=True)

    # # 查找元素
    # name_ele = iframe_page.find_ele('//*[@id="u"]')


    # ###### 示例三
    # # 初始化iframe处理器
    # iframe_page = IframePage(web_page)

    # # 跨层级查找元素
    name_ele = iframe_page.find_ele2('//*[@id="po_id"]').click()

