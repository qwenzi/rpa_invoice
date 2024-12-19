import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        账号 = ""
        密码 = ""
        短信验证码接口 = ""
        是否退出已登录账户 = False
    else:
        账号 = args.get("账号", "")
        密码 = args.get("密码", "")
        短信验证码接口 = args.get("短信验证码接口", "")
        是否退出已登录账户 = args.get("是否退出已登录账户", False)
    try:
        _ = xbot_visual.process.invoke_module(module="utils", package=__name__, function="validate_input_content", params={
            "username": 账号,
            "password": 密码,
        }, _block=("拼多多商家后台登录", 1, "调用模块"))
        url = "https://mms.pinduoduo.com/home/"
        web_page = xbot_visual.web.create(web_type="chrome", value=url, silent_running=False, wait_load_completed=True, load_timeout="120", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("拼多多商家后台登录", 3, "打开网页"))
        # ------------检查是否已登录
        try:
            登录账号_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="(//*[@class=\"user-name-text\"])[last()]", is_related_parent=False, parent="", timeout="5", _block=("拼多多商家后台登录", 5, "获取元素对象(web)"))
        except Exception as e:
            pass
            登录账号_元素对象 = None
        if xbot_visual.workflow.test(operand1=登录账号_元素对象, operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("拼多多商家后台登录", 6, "IF 条件")):
            已登录账号 = xbot_visual.web.element.get_details(browser=web_page, element=登录账号_元素对象, operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("拼多多商家后台登录", 7, "获取元素信息(web)"))
            xbot_visual.programing.log(type="info", text="已登录账号: " + xbot_visual.sh_str(已登录账号), _block=("拼多多商家后台登录", 8, "打印日志"))
            if xbot_visual.workflow.test(operand1=是否退出已登录账户, operator="is true", operand2="", operator_options="{}", _block=("拼多多商家后台登录", 9, "IF 条件")):
                # ------------直接调用退出接口退出登录状态。
                xbot_visual.web.browser.navigate(browser=web_page, mode="url", url="https://mms.pinduoduo.com/janus/api/logout", ignore_cache=False, load_timeout="20", _block=("拼多多商家后台登录", 11, "跳转至新网址"))
                xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多商家后台登录", 12, "等待"))
            else:
                xbot_visual.programing.log(type="info", text="不退出已登录账户，登录流程结束。", _block=("拼多多商家后台登录", 14, "打印日志"))
                return
            #endif
        #endif
        xbot_visual.web.browser.navigate(browser=web_page, mode="url", url=url, ignore_cache=False, load_timeout="20", _block=("拼多多商家后台登录", 18, "跳转至新网址"))
        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拼多多商家后台登录", 19, "等待"))
        # ------------登录
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpathSelector": "//*[text()=\"账号登录\"]",
            "获取元素超时": lambda: 5,
            "执行成功后等待": lambda: 1,
            "是否模拟人工": False,
            "按钮": "left",
            "retry_count": lambda: 1,
            "refresh": False,
            "是否为iframe对象": False,
            }, outputs=[
        ], _block=("拼多多商家后台登录", 21, "点击Xpath元素"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//*[@id=\"usernameId\"]",
            "输入内容": 账号,
            "iframe跨域元素": False,
            "输入方式": "剪切板",
            "追加按键": "",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 1,
            "追加输入": False,
            }, outputs=[
        ], _block=("拼多多商家后台登录", 22, "输入内容ByXpath"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//*[@id=\"passwordId\"]",
            "输入内容": 密码,
            "iframe跨域元素": False,
            "输入方式": "剪切板",
            "追加按键": "",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 1,
            "追加输入": False,
            }, outputs=[
        ], _block=("拼多多商家后台登录", 23, "输入内容ByXpath"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpathSelector": "//*[text()=\"登录\"]",
            "获取元素超时": lambda: 5,
            "执行成功后等待": lambda: 1,
            "是否模拟人工": False,
            "按钮": "left",
            "retry_count": lambda: 1,
            "refresh": False,
            "是否为iframe对象": False,
            }, outputs=[
        ], _block=("拼多多商家后台登录", 24, "点击Xpath元素"))
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("拼多多商家后台登录", 25, "等待"))
        # ------------检查是否登录完成
        # 添加验证码检查
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("拼多多-点选验证码-提示词"), _block=("拼多多商家后台登录", 28, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_4db973e3.process21", package=__name__, inputs={
                "网页对象": web_page,
                "识别模式": "点选1个坐标",
                "验证码图片": package.selector("拼多多-点选验证码背景图"),
                "点选提示": package.selector("拼多多-点选验证码-提示词"),
                "图鉴账号": "",
                "图鉴密码": "",
                }, outputs=[
            ], _block=("拼多多商家后台登录", 29, "坐标点选验证"))
        #endif
        try:
            店铺名_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="(//*[@class=\"user-name-text\"])[1]", is_related_parent=False, parent="", timeout="5", _block=("拼多多商家后台登录", 31, "获取元素对象(web)"))
        except Exception as e:
            pass
            店铺名_元素对象 = None
        if xbot_visual.workflow.test(operand1=店铺名_元素对象, operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("拼多多商家后台登录", 32, "IF 条件")):
            # -----------------------登录成功
            店铺名 = xbot_visual.web.element.get_details(browser=web_page, element=店铺名_元素对象, operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("拼多多商家后台登录", 34, "获取元素信息(web)"))
            xbot_visual.programing.log(type="info", text="登录成功：", _block=("拼多多商家后台登录", 35, "打印日志"))
            return
        else:
            raise Exception("登录失败，请先手动通过验证。")
            # ----------------------需要验证
            # ------------todo: 补全短信验证，验证码验证
        #endif
    finally:
        args["web_page"] = web_page
