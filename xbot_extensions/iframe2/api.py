from ._core import *


def init_iframe(web_page):
    """A0-初始化iframe"""
    return IframePage(web_page)


@check_obj
def to_iframe(*, iframe_instance, iframe_xpath, current_global, timeout):
    """A1-切换iframe"""
    return iframe_instance.to_iframe(iframe_xpath, current_global, timeout=timeout)


@check_obj
def parent(iframe_instance):
    """A2-切换至父iframe"""
    return iframe_instance.parent()


@check_obj
def find_ele(*, iframe_instance, xpath, current_global, timeout):
    """B1-获取元素对象"""
    return iframe_instance.find_ele(xpath, is_iframe=False, current_global=current_global, timeout=timeout)


@check_obj
def find_all_ele(*, iframe_instance, xpath, current_global=False, timeout=10):
    """B2-获取相似元素"""
    return iframe_instance.find_all_ele(xpath, is_iframe=False, current_global=current_global, timeout=timeout)


@check_obj
def click_by_xpath(*, iframe_instance, xpath, current_global=False,button='left',simulative=True,keys="none",move_mouse=False,clicks="单击",delay_after=1, timeout=5):
    """C1-点击元素"""
    iframe_instance.click_by_xpath(xpath=xpath, current_global=current_global,button=button,simulative=simulative,keys=keys, move_mouse=move_mouse,clicks=clicks,delay_after=delay_after,timeout=timeout)


@check_obj
def input_by_xpath(*, iframe_instance, xpath, text, current_global=False, simulative=True, append=False, contains_hotkey=False, force_ime_ENG=False, send_key_delay=50, focus_timeout=1000, delay_after=1, click_before_input=True,timeout=5):
    """C2-填写输入框"""
    iframe_instance.input_by_xpath(xpath, text, current_global=current_global, append=append, simulative=simulative, contains_hotkey=contains_hotkey,force_ime_ENG=force_ime_ENG, focus_timeout=focus_timeout, delay_after=delay_after, send_key_delay=send_key_delay, click_before_input=click_before_input,timeout=timeout)


@check_obj
def wait(*, iframe_instance, xpath, state="appear", current_global=False, timeout=20):
    return iframe_instance.wait(xpath, state=state, current_global=current_global, timeout=timeout)

@check_obj
def get_elem_info(*, iframe_instance, xpath, op, attr_name=None, current_global=False, timeout=20):
    elem = iframe_instance.find_ele(xpath, is_iframe=False, current_global=current_global, timeout=timeout)

    func_map = {
        "获取元素文本内容": "get_text",
        "获取元素源代码": "get_html",
        "获取元素值": "get_value",
        # "获取网页链接地址": "",
        "获取元素位置": "get_bounding",
        "获取元素属性": "get_attribute",
    }
    func_name = func_map.get(op)
    if not func_name: raise Exception(f"传入的操作 [{op}] 有误")
    if attr_name: return getattr(elem, func_name)(attr_name)
    return getattr(elem, func_name)()
    


def test_get_elem_info():
    web_page = xbot.web.get_active(mode="chrome")
    value = get_elem_info(iframe_instance=web_page, xpath='//*[@data-placeholder="邮箱账号或手机号码"]', op="获取元素信息", attr_name="data-placeholder", current_global=True)
    print(value)




def _test1():
    # 聚水潭
    xpaths = '''//li[@class="ant-pagination-item ant-pagination-item-1 ant-pagination-item-active" and @title="1"]'''
    web_page = xbot.web.get(url="https://www.erp321.com/epaas*", mode='edge', use_wildcard=True)
    # eles = find_all_ele(iframe_instance=web_page, xpath=xpaths, current_global=False, timeout=5)
    # print(eles)
    eles = wait(iframe_instance=web_page, xpath=xpaths, current_global=True, timeout=2, state='appear')
    print(eles)
    # print(eles.get_text())
    # to_iframe(iframe_instance=web_page, iframe_xpath=xpaths[:-1], current_global=True)
    # web_page = to_iframe(iframe_instance=web_page, iframe_xpath='//iframe[@class="_dialog_frame"]', current_global=True)
    

def _test_wait():
    web_page = xbot.web.get_active('chrome', load_timeout=0)
    web_page.navigate(url="https://www.google.com/search?q=uiautomator2", load_timeout=0)
    # web_page.fin
    # res = wait(iframe_instance=web_page, xpath='//qwe', state='appear', timeout=5)
    res = find_all_ele(iframe_instance=web_page, xpath='//body', timeout=1, current_global=False)
    print(res)
    # web_page = to_iframe(iframe_instance=web_page, iframe_xpath='//*[@id="1iframe-after_sales"]', current_global=False, timeout=5)
    # print(wait(iframe_instance=web_page, xpath="/html1", state="appear", timeout=""))


def _test_to_iframe():
    web_page = xbot.web.get_active('edge')
    # web_page.
    web_page = to_iframe(iframe_instance=web_page, iframe_xpath='//*[@allow="camera"]', current_global=True, timeout=2)    


def main(args):
    # _test_to_iframe()
    test_get_elem_info()

    pass