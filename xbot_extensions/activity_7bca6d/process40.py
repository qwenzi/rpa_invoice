import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        登录用户名 = ""
        登录密码 = ""
        子平台 = ""
        退出已登录账户 = True
        短信验证码获取接口 = ""
        识别引擎 = ""
    else:
        登录用户名 = args.get("登录用户名", "")
        登录密码 = args.get("登录密码", "")
        子平台 = args.get("子平台", "")
        退出已登录账户 = args.get("退出已登录账户", True)
        短信验证码获取接口 = args.get("短信验证码获取接口", "")
        识别引擎 = args.get("识别引擎", "")
    try:
        web_page = xbot_visual.web.create(web_type="chrome", value="https://jzt.jd.com/gw/index", silent_running=False, wait_load_completed=True, load_timeout="120", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("京准通登录", 1, "打开网页"))
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("京准通登录", 2, "等待"))
        # --------已登录状态是否需要退出登录--------
        try:
            立即投放_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="//button[contains(string(),'立即投放')]", is_related_parent=False, parent="", timeout="5", _block=("京准通登录", 4, "获取元素对象(web)"))
        except Exception as e:
            pass
            立即投放_元素对象 = None
        if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 立即投放_元素对象,"operand2": "","operator": "not none"},{"operand1": 退出已登录账户,"operand2": "","operator": "is true"}], _block=("京准通登录", 5, "IF 多条件")):
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpathSelector": "//a[contains(text(),\"退出登录\")]",
                "获取元素超时": lambda: 5,
                "执行成功后等待": lambda: 1,
                "是否模拟人工": False,
                "按钮": "left",
                "retry_count": lambda: 1,
                "refresh": False,
                "是否为iframe对象": False,
                }, outputs=[
            ], _block=("京准通登录", 6, "点击Xpath元素"))
        elif xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 立即投放_元素对象,"operand2": "","operator": "not none"},{"operand1": 退出已登录账户,"operand2": "","operator": "is false"}], _block=("京准通登录", 7, "Else IF 多条件")):
            xbot_visual.programing.log(type="info", text="已登录， 退出登录流程", _block=("京准通登录", 8, "打印日志"))
            return
        #endif
        # --------登录操作
        for idx in xbot_visual.workflow.range_iterator(start="1", stop="10", step="1", _block=("京准通登录", 12, "For次数循环")):
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("登录京东账号_登录框"), _block=("京准通登录", 13, "IF 元素可见(web)")):
                break
            #endif
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpathSelector": "//*[text()=\" 登录 \"]",
                "获取元素超时": lambda: 5,
                "执行成功后等待": lambda: 3,
                "是否模拟人工": False,
                "按钮": "left",
                "retry_count": lambda: 1,
                "refresh": False,
                "是否为iframe对象": False,
                }, outputs=[
            ], _block=("京准通登录", 16, "点击Xpath元素"))
        #endloop
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//*[@id=\"loginname\"]",
            "输入内容": 登录用户名,
            "iframe跨域元素": True,
            "输入方式": "剪切板",
            "追加按键": "",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 1,
            "追加输入": False,
            }, outputs=[
        ], _block=("京准通登录", 18, "输入内容ByXpath"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//*[@id=\"nloginpwd\"]",
            "输入内容": 登录密码,
            "iframe跨域元素": True,
            "输入方式": "剪切板",
            "追加按键": "",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 1,
            "追加输入": False,
            }, outputs=[
        ], _block=("京准通登录", 19, "输入内容ByXpath"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpathSelector": "//*[@id=\"paipaiLoginSubmit\"]",
            "获取元素超时": lambda: 5,
            "执行成功后等待": lambda: 3,
            "是否模拟人工": False,
            "按钮": "left",
            "retry_count": lambda: 1,
            "refresh": False,
            "是否为iframe对象": True,
            }, outputs=[
        ], _block=("京准通登录", 20, "点击Xpath元素"))
        # --------滑块验证------------重试次数 --- 10
        for idx in xbot_visual.workflow.range_iterator(start="1", stop="5", step="1", _block=("京准通登录", 22, "For次数循环")):
            xbot_visual.programing.log(type="info", text="滑块验证尝试 >> " + xbot_visual.sh_str(idx), _block=("京准通登录", 23, "打印日志"))
            # xbot_extensions.activity_ea8fd401.iframeElement
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京准通登录", 25, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("京准通登录", 25,"获取已打开的网页对象"))
                time.sleep(3)
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("jzt背景元素"), _block=("京准通登录", 26, "IF 元素可见(web)")):
                xbot_visual.programing.log(type="info", text="滑块验证成功", _block=("京准通登录", 27, "打印日志"))
                break
            else:
                # xbot_extensions.activity_ea8fd401.iframeElement
                # xbot_extensions.activity_ea8fd401.iframeElement
                xbot_visual.process.run(process="xbot_extensions.activity_jfbym.std_slider_captcha", package=__name__, inputs={
                    "web_page": web_page,
                    "engine": "xbot",
                    "background_ele": package.selector("jzt背景元素"),
                    "slider_ele": package.selector("jzt滑块"),
                    "ym_token": "",
                    "retry_count": lambda: 5,
                    "offset": lambda: 0,
                    "speed": lambda: 1,
                    }, outputs=[
                ], _block=("京准通登录", 32, "通用单图滑块验证"))
            #endif
            # workflow.if
            # xbot_extensions.activity_ea8fd401.iframeElement
            # xbot_extensions.activity_ea8fd401.iframeElement
        #endloop
        # -------判断是否需要短信验证
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("京准通登录", 39, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("京准通登录", 39,"获取已打开的网页对象"))
            time.sleep(3)
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("账号名与密码不匹配，请重新输入_1"), _block=("京准通登录", 40, "IF 元素可见(web)")):
            web_element_attribute = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("账号名与密码不匹配，请重新输入_1"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("京准通登录", 41, "获取元素信息(web)"))
            raise Exception(web_element_attribute)
        #endif
        try:
            短信验证_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="//*[text()=\"使用 手机短信验证码\"]", is_related_parent=False, parent=None, timeout="5", _block=("京准通登录", 44, "获取元素对象(web)"))
        except Exception as e:
            pass
            短信验证_元素对象 = None
        if xbot_visual.workflow.test(operand1=短信验证_元素对象, operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("京准通登录", 45, "IF 条件")):
            # ------是否短信验证
            if xbot_visual.workflow.test(operand1=短信验证码获取接口, operator="empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("京准通登录", 47, "IF 条件")):
                raise Exception("需要进行短信验证码，请手动通过！")
            #endif
            xbot_visual.web.element.click(browser=web_page, element=短信验证_元素对象, simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("京准通登录", 50, "点击元素(web)"))
            # ------todo: 短信接收指令
            # ------todo: 获取验证码
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpathSelector": "//button[contains(string(), \"获取短信验证\")]",
                "获取元素超时": lambda: 5,
                "执行成功后等待": lambda: 0,
                "是否模拟人工": False,
                "按钮": "left",
                "retry_count": lambda: 1,
                "refresh": False,
                "是否为iframe对象": False,
                }, outputs=[
            ], _block=("京准通登录", 53, "点击Xpath元素"))
            验证码 = xbot_visual.programing.variable(value=""
            , _block=("京准通登录", 54, "设置变量"))
            # ------ 输入验证码
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpath": "//input[@placeholder=\"请输入手机验证码\"]",
                "输入内容": 验证码,
                "iframe跨域元素": False,
                "输入方式": "剪切板",
                "追加按键": "{ENTER}",
                "等待元素存在": lambda: 20,
                "操作完成后等待": lambda: 2,
                "追加输入": False,
                }, outputs=[
            ], _block=("京准通登录", 56, "输入内容ByXpath"))
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpathSelector": "//button[text()=\"提交认证\"]",
                "获取元素超时": lambda: 5,
                "执行成功后等待": lambda: 0,
                "是否模拟人工": True,
                "按钮": "left",
                "retry_count": lambda: 1,
                "refresh": False,
                "是否为iframe对象": False,
                }, outputs=[
            ], _block=("京准通登录", 57, "点击Xpath元素"))
        #endif
        # -------判断是否登录成功
        try:
            立即投放_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="//button[contains(string(),'立即投放')]", is_related_parent=False, parent=None, timeout="5", _block=("京准通登录", 60, "获取元素对象(web)"))
        except Exception as e:
            pass
            立即投放_元素对象 = None
        if xbot_visual.workflow.test(operand1=立即投放_元素对象, operator="empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("京准通登录", 61, "IF 条件")):
            raise Exception("登录失败，请联系运维人员进行维护。")
        #endif
        xbot_visual.programing.log(type="info", text="登录成功，跳转至目标平台  > " + xbot_visual.sh_str(子平台), _block=("京准通登录", 64, "打印日志"))
        # -------跳转到目标平台
        _ = xbot_visual.process.run(process="process41", package=__name__, inputs={
            "平台名称": 子平台,
            }, outputs=[
        ], _block=("京准通登录", 66, "调用流程"))
    finally:
        pass
