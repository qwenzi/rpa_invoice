import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    web_page = None
    if args is None:
        username = ""
        password = ""
        验证邮箱 = ""
        邮箱授权码 = ""
        获取授权码间隔时长 = 20
        验证码失败最大重试次数 = 10
        退出已登录账户 = False
        retry_cnt = 3
    else:
        username = args.get("username", "")
        password = args.get("password", "")
        验证邮箱 = args.get("验证邮箱", "")
        邮箱授权码 = args.get("邮箱授权码", "")
        获取授权码间隔时长 = args.get("获取授权码间隔时长", 20)
        验证码失败最大重试次数 = args.get("验证码失败最大重试次数", 10)
        退出已登录账户 = args.get("退出已登录账户", False)
        retry_cnt = args.get("retry_cnt", 3)
    try:
        # 抖店邮箱登录----邮箱验证
        登录页url = xbot_visual.programing.variable(value="https://fxg.jinritemai.com/login/common"
        , _block=("抖店登录", 2, "设置变量"))
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.create(web_type="chrome", value=登录页url, silent_running=False, wait_load_completed=True, load_timeout="120", stop_load_if_load_timeout="handleExcept", chrome_file_name=None, edge_file_name=None, ie_file_name=None, bro360_file_name=None, firefox_file_name=None, arguments=None, _block=("抖店登录", 3, "打开网页"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("抖店登录", 3,"打开网页"))
            time.sleep(20)
        # 如果已经登录, 会重定向到新网页
        xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("抖店登录", 5, "等待"))
        # 二维码
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=True, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("抖店登录", 7, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("抖店登录", 7,"获取已打开的网页对象"))
            time.sleep(3)
        web_page_url = xbot_visual.web.browser.get_details(browser=web_page, operation="url", _block=("抖店登录", 8, "获取网页信息"))
        if xbot_visual.workflow.test(operand1=web_page_url, operator="not in", operand2="/login", operator_options="{\"ignoreCase\":\"False\"}", _block=("抖店登录", 9, "IF 条件")):
            # ----------已登录状态，退出登录
            if xbot_visual.workflow.test(operand1=退出已登录账户, operator="is true", operand2="", operator_options="{}", _block=("抖店登录", 11, "IF 条件")):
                xbot_visual.programing.log(type="info", text="账户已登录， 退出已登录账户。", _block=("抖店登录", 12, "打印日志"))
                头像_元素对象 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="//*[contains(@class, \"headerShopName\")]", is_related_parent=False, parent=None, timeout="20", _block=("抖店登录", 13, "获取元素对象(web)"))
                xbot_visual.web.element.hover(browser=web_page, element=头像_元素对象, simulate=False, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("抖店登录", 14, "鼠标悬停在元素上(web)"))
                xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                    "web_page": web_page,
                    "xpathSelector": "//*[contains(@class, \"index_logout\")]",
                    "获取元素超时": lambda: 5,
                    "执行成功后等待": lambda: 1,
                    "是否模拟人工": False,
                    "按钮": "left",
                    "retry_count": lambda: 1,
                    "refresh": False,
                    "是否为iframe对象": False,
                    }, outputs=[
                ], _block=("抖店登录", 15, "点击Xpath元素"))
                xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("抖店登录", 16, "等待"))
                xbot_visual.web.browser.navigate(browser=web_page, mode="url", url="https://fxg.jinritemai.com/login", ignore_cache=False, load_timeout="120", _block=("抖店登录", 17, "跳转至新网址"))
                xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("抖店登录", 18, "等待"))
            else:
                xbot_visual.programing.log(type="info", text="账户已登录，不退出账户。", _block=("抖店登录", 20, "打印日志"))
                return
            #endif
        #endif
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("抖店登录_请选择店铺_返回按钮"), text="", _block=("抖店登录", 24, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("抖店登录_请选择店铺_返回按钮"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="10", _block=("抖店登录", 25, "点击元素(web)"))
        #endif
        web_wait_result = xbot_visual.web.element.wait(browser=web_page, element=package.selector("抖店登錄界面"), state="appear", iswait=True, timeout="20", _block=("抖店登录", 27, "等待元素(web)"))
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("抖店_邮箱登录"), _block=("抖店登录", 28, "IF 元素可见(web)")):
            xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
                "web_page": web_page,
                "xpathSelector": "//*[@class=\"login-switcher--qr\" or @class=\"login-switcher--cell\" ]",
                "获取元素超时": lambda: 5,
                "执行成功后等待": lambda: 1,
                "是否模拟人工": False,
                "按钮": "left",
                "retry_count": lambda: 1,
                "refresh": False,
                "是否为iframe对象": False,
                }, outputs=[
            ], _block=("抖店登录", 29, "点击Xpath元素"))
        #endif
        # 结束
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.ClickByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpathSelector": "//div[contains(text(), \"邮箱登录\")]/span/..",
            "获取元素超时": lambda: 5,
            "执行成功后等待": lambda: 1,
            "是否模拟人工": False,
            "按钮": "left",
            "retry_count": lambda: 1,
            "refresh": False,
            "是否为iframe对象": False,
            }, outputs=[
        ], _block=("抖店登录", 32, "点击Xpath元素"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//input[@placeholder='请输入邮箱']",
            "输入内容": username,
            "iframe跨域元素": False,
            "输入方式": "剪切板",
            "追加按键": "",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 1,
            "追加输入": False,
            }, outputs=[
        ], _block=("抖店登录", 33, "输入内容ByXpath"))
        xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.InputByXpath", package=__name__, inputs={
            "web_page": web_page,
            "xpath": "//input[@placeholder='密码']",
            "输入内容": password,
            "iframe跨域元素": False,
            "输入方式": "剪切板",
            "追加按键": "{ENTER}",
            "等待元素存在": lambda: 20,
            "操作完成后等待": lambda: 2,
            "追加输入": False,
            }, outputs=[
        ], _block=("抖店登录", 34, "输入内容ByXpath"))
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("抖店_多店铺登录_同意用户协议复选框"), text="", _block=("抖店登录", 35, "IF 网页包含")):
            xbot_visual.web.element.check(browser=web_page, element=package.selector("抖店_多店铺登录_同意用户协议复选框"), mode="check", delay_after="1", timeout="20", _block=("抖店登录", 36, "设置复选框(web)"))
        #endif
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="url", value=xbot_visual.sh_str(登录页url) + "*", use_wildcard=True, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="stopLoad", open_page=False, url=None, _block=("抖店登录", 38, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("抖店登录", 38,"获取已打开的网页对象"))
            time.sleep(3)
        xbot_visual.web.element.click(browser=web_page, element=package.selector("登录_1"), simulate=False, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("抖店登录", 39, "点击元素(web)"))
        # xbot_extensions.activity_fe2a1069.ClickByXpath
        # 验证码验证【滑块验证或文字点选验证】
        _ = xbot_visual.process.run(process="process48", package=__name__, inputs={
            "web_page": web_page,
            "验证码失败最大重试次数": 验证码失败最大重试次数,
            }, outputs=[
        ], _block=("抖店登录", 42, "调用流程"))
        # --------------检查是否需要邮箱验证-邮箱授权码获取
        _ = xbot_visual.process.run(process="process49", package=__name__, inputs={
            "web_page": web_page,
            "验证邮箱": 验证邮箱,
            "邮箱授权码": 邮箱授权码,
            "获取授权码间隔时长": 获取授权码间隔时长,
            "验证码失败最大重试次数": 验证码失败最大重试次数,
            }, outputs=[
        ], _block=("抖店登录", 44, "调用流程"))
        # ------登录成功判断
        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("抖店工作台"), _block=("抖店登录", 46, "IF 元素可见(web)")):
            web_element_list = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("抖店工作台"), css_selector="", xpath_selector="", is_related_parent=False, parent=None, operation="element", absolute_url=False, attribute_name=None, timeout="20", output_with_element_count=True, _block=("抖店登录", 47, "获取相似元素列表(web)"))
            web_element_count = len(web_element_list)
            if xbot_visual.workflow.test(operand1=web_element_count, operator="==", operand2=lambda: 1, operator_options="{}", _block=("抖店登录", 48, "IF 条件")):
                xbot_visual.web.element.click(browser=web_page, element=package.selector("抖店工作台"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("抖店登录", 49, "点击元素(web)"))
            #endif
        #endif
        if xbot_visual.web.browser.contains_element_or_text(browser=web_page, content_type="contains_element", selector=package.selector("抖店登录_请选择店铺_第一家店铺"), text="", _block=("抖店登录", 52, "IF 网页包含")):
            xbot_visual.web.element.click(browser=web_page, element=package.selector("抖店登录_请选择店铺_第一家店铺"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="3", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("抖店登录", 53, "点击元素(web)"))
        #endif
        try:
            店铺名 = xbot_visual.process.run(process="xbot_extensions.activity_fe2a1069.GetShopName", package=__name__, inputs={
                "平台名称": "抖店/电商罗盘",
                "web_page": web_page,
                }, outputs=[
                "店铺名",
            ], _block=("抖店登录", 55, "获取店铺名"))
        except Exception as e:
            pass
            店铺名 = None
        if xbot_visual.workflow.test(operand1=店铺名, operator="empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("抖店登录", 56, "IF 条件")):
            # ------登录失败处理
            if xbot_visual.workflow.test(operand1=retry_cnt, operator=">=", operand2=lambda: 0, operator_options="{}", _block=("抖店登录", 58, "IF 条件")):
                raise Exception("登录流程失败！")
            #endif
            xbot_visual.web.browser.close(operation="close_specified", browser=web_page, web_type="cef", task_kill=False, _block=("抖店登录", 61, "关闭网页"))
            retry_cnt = xbot_visual.programing.variable(value=lambda: retry_cnt - 1
            , _block=("抖店登录", 62, "设置变量"))
            登录结果 = xbot_visual.process.run(process="xbot_extensions.dynamic_call.process1", package=__name__, inputs={
                "流程名": "抖店登录",
                "流程参数": lambda: {"username": username, "password":password, "验证邮箱": 验证邮箱, "邮箱授权码": 邮箱授权码, "获取授权码间隔时长": 获取授权码间隔时长, "验证码失败最大重试次数": 验证码失败最大重试次数, "退出已登录账户": 退出已登录账户, "retry_cnt": retry_cnt},
                "file_path": lambda: __file__,
                }, outputs=[
                "process_result",
            ], _block=("抖店登录", 63, "动态调用子流程"))
            web_page = xbot_visual.programing.variable(value=lambda: 登录结果["web_page"]
            , _block=("抖店登录", 64, "设置变量"))
            return
        #endif
        xbot_visual.programing.log(type="info", text="登录完成。  欢迎： " + xbot_visual.sh_str(店铺名), _block=("抖店登录", 67, "打印日志"))
        # --多店铺进入第一家店铺
        try:
            进入店铺 = xbot_visual.web.element.get_element(browser=web_page, select_type="xpath_selector", selector=None, css_selector="", xpath_selector="(//div[text()=\"进入店铺\"])[1]", is_related_parent=False, parent=None, timeout="3", _block=("抖店登录", 69, "获取元素对象(web)"))
        except Exception as e:
            pass
            进入店铺 = 1
        if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 进入店铺,"operand2": "1","operator": "!="}], _block=("抖店登录", 70, "IF 多条件")):
            xbot_visual.web.element.click(browser=web_page, element=进入店铺, simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="3", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("抖店登录", 71, "点击元素(web)"))
        #endif
    finally:
        args["web_page"] = web_page
