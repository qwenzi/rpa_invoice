
import base64
from io import BytesIO
from PIL import Image
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

from .js_utility import execute_javascript, JSUtility


print = [lambda *_, **__: None, print][__name__.startswith("xbot_robot.")]


def hide_element(web_page: WebBrowser = None, element=None) -> None:
    """
    隐藏元素
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
           element.style.display = "none"; 
        }
    """
    execute_javascript(script, web_page, element)


def show_element(web_page: WebBrowser = None, element=None) -> None:
    """
    显示元素
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
           element.style.display = "block"; 
        }
    """
    execute_javascript(script, web_page, element)


def remove_element(web_page: WebBrowser = None, element=None) -> None:
    script = """
        function (element, input) {
           element.remove();
        }
    """
    execute_javascript(script, web_page, element)    


def scroll_into_view(web_page: WebBrowser = None, element=None) -> None:
    """
    滚动元素至可视区域
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
           element.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center'});
        }
    """
    execute_javascript(script, web_page, element)


def get_style(attr: str, web_page: WebBrowser = None, element=None) -> str:
    """
    获取元素样式
    :param attr:
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
          let styles = window.getComputedStyle(element);
          return styles.%s;
        }
    """ % attr
    return execute_javascript(script, web_page, element)

def set_style(attr: str, value: str, web_page: WebBrowser = None, element=None) -> str:
    """
    设置元素样式
    :param attr:
    :param value:
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
          element.style.%s = `%s`
        }
    """ % (attr, value)
    return execute_javascript(script, web_page, element)


def get_background_color(web_page: WebBrowser = None, element=None) -> str:
    return get_style("backgroundColor", web_page, element)


def get_font_color(web_page: WebBrowser = None, element=None) -> str:
    return get_style("color", web_page, element)


def add_border(width, style, color, web_page: WebBrowser = None, element=None):
    style_map = {"虚线": "dotted", "直线": "solid"}
    style = style_map.get(style, "solid")
    s = " ".join([f"{width}px", style, color])
    set_style("border", s, web_page, element)


def long_screenshot(filepath: str, web_page: WebBrowser = None, element=None):
    """元素长截图"""
    JSUtility(web_page=web_page, element=element).import_js_lib("html2canvas.min.js")    

    script = """
    async function (element, input) {
        imageUrl = null;
        function get_image() {
            return html2canvas(element, {
                useCORS: true, 
            }).then(function (canvas) {
                return canvas.toDataURL('image/png', 1);
            });
        }

        imageUrl = await get_image();
        console.log("imageUrl", imageUrl)
        return imageUrl;
    }
    """
    execute_javascript(script, web_page, element)
    script = '''
    function (element) {
        // console.log(imageUrl)
        return imageUrl;
    }
    '''
    for _ in range(8):
        image_url = execute_javascript(script, web_page, element)
        if image_url:
            break
        sleep(1)

    if not image_url:
        raise Exception("截图失败")

    def base64_to_image(base64_str, save_path):
        """
        将base64字符串转换为图片
        """
        header, data = base64_str.split(',')
        image_data = base64.b64decode(data)
        image = Image.open(BytesIO(image_data))
        image.save(save_path)
    
    base64_to_image(image_url, filepath)


def get_pseudo_element_style(_type: str, attr: str, web_page: WebBrowser = None, element=None) -> str:
    """
    获取伪元素样式
    :param attr:
    :param web_page:
    :param element:
    :return:
    """
    script = """
        function (element, input) {
          let styles = window.getComputedStyle(element, `%s`);
          return styles.%s;
        }
    """ % (_type, attr)
    return execute_javascript(script, web_page, element)


def get_pseudo_element_value(_type: str, web_page: WebBrowser = None, element=None):
    return get_pseudo_element_style(_type, "content", web_page, element)


def remove_zoom(web_page):
    script = """
        function (element, input) {
            document.body.parentElement.style.zoom = null;
        }
    """
    execute_javascript(script, web_page)
    

def main(args):
    web_page = xbot.web.get_active(mode="chrome")
    remove_zoom(web_page)
    # ele = web_page.find_by_xpath('//*[@id="textareasContainer"]/div[3]/section/div[1]/d-textarea/div')
    # res = get_pseudo_element_value("::before", web_page, ele)
    # print(res)
    # long_screenshot(r"D:\post\image\123.png", web_page, package.selector('账号登录'))
    pass
