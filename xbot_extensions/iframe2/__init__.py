from .import package
import xbot_visual

def init_iframe(web_page):
    """
    初始化IFrame
    初始化IFrame，获取IFrame对象，帮助实现跨域操作
    * @param web_page，
    * @return iframe_instance，
    """
    outputs = ["iframe_instance"]
    inputs = {"web_page":web_page}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.init_iframe", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.init_iframe",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.init_iframe", extension_module, activity_func)

def to_iframe(iframe_instance,iframe_xpath,全局查找,超时时间):
    """
    切换IFrame
    根据XPath切换IFrame
    * @param iframe_instance，
    * @param iframe_xpath，
    * @param 全局查找，
    * @param 超时时间，
    * @return new_iframe_instance，
    """
    outputs = ["new_iframe_instance"]
    inputs = {"iframe_instance":iframe_instance,"iframe_xpath":iframe_xpath,"全局查找":全局查找,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.to_iframe", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.to_iframe",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.to_iframe", extension_module, activity_func)

def find_ele(iframe_instance,xpath,全局查找,超时时间):
    """
    获取元素对象-XPath跨域
    获取元素对象-XPath跨域
    * @param iframe_instance，
    * @param xpath，
    * @param 全局查找，
    * @param 超时时间，
    * @return web_element，
    """
    outputs = ["web_element"]
    inputs = {"iframe_instance":iframe_instance,"xpath":xpath,"全局查找":全局查找,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.find_ele", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.find_ele",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.find_ele", extension_module, activity_func)

def find_all_ele(iframe_instance,xpath,全局查找,超时时间):
    """
    获取相似元素列表-XPath跨域
    获取相似元素列表-XPath跨域
    * @param iframe_instance，
    * @param xpath，
    * @param 全局查找，
    * @param 超时时间，
    * @return web_element_list，
    """
    outputs = ["web_element_list"]
    inputs = {"iframe_instance":iframe_instance,"xpath":xpath,"全局查找":全局查找,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.find_all_ele", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.find_all_ele",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.find_all_ele", extension_module, activity_func)

def click_by_xpath(iframe对象,Xpath,全局查找,模拟人工点击,显示鼠标移动轨迹,鼠标按键,辅助按键,执行后延迟,点击方式,超时时间):
    """
    点击元素-XPath跨域
    通过XPath，跨域查找元素并点击
    * @param iframe对象，
    * @param Xpath，
    * @param 全局查找，
    * @param 模拟人工点击，
    * @param 显示鼠标移动轨迹，
    * @param 鼠标按键，
    * @param 辅助按键，
    * @param 执行后延迟，
    * @param 点击方式，
    * @param 超时时间，
    """
    outputs = []
    inputs = {"iframe对象":iframe对象,"Xpath":Xpath,"全局查找":全局查找,"模拟人工点击":模拟人工点击,"显示鼠标移动轨迹":显示鼠标移动轨迹,"鼠标按键":鼠标按键,"辅助按键":辅助按键,"执行后延迟":执行后延迟,"点击方式":点击方式,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.click_by_xpath", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.click_by_xpath",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.click_by_xpath", extension_module, activity_func)

def input_by_xpath(iframe对象,Xpath,输入内容,追加输入,输入方式,输入内容包含快捷键,强制加载美式键盘,按键输入间隔,焦点超时时间,执行后延迟,输入前点击元素,全局查找,超时时间):
    """
    填写输入框-XPath跨域
    XPath跨域查找元素并输入
    * @param iframe对象，
    * @param Xpath，
    * @param 输入内容，
    * @param 追加输入，
    * @param 输入方式，
    * @param 输入内容包含快捷键，
    * @param 强制加载美式键盘，
    * @param 按键输入间隔，
    * @param 焦点超时时间，
    * @param 执行后延迟，
    * @param 输入前点击元素，
    * @param 全局查找，
    * @param 超时时间，
    """
    outputs = []
    inputs = {"iframe对象":iframe对象,"Xpath":Xpath,"输入内容":输入内容,"追加输入":追加输入,"输入方式":输入方式,"输入内容包含快捷键":输入内容包含快捷键,"强制加载美式键盘":强制加载美式键盘,"按键输入间隔":按键输入间隔,"焦点超时时间":焦点超时时间,"执行后延迟":执行后延迟,"输入前点击元素":输入前点击元素,"全局查找":全局查找,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.input_by_xpath", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.input_by_xpath",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.input_by_xpath", extension_module, activity_func)

def wait_by_xpath(iframe对象,XPath,等待状态,超时时间,current_global):
    """
    等待元素-XPath跨域
    跨域等待元素
    * @param iframe对象，
    * @param XPath，
    * @param 等待状态，
    * @param 超时时间，
    * @param current_global，
    * @return wait_result，
    """
    outputs = ["wait_result"]
    inputs = {"iframe对象":iframe对象,"XPath":XPath,"等待状态":等待状态,"超时时间":超时时间,"current_global":current_global}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.wait_by_xpath", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.wait_by_xpath",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.wait_by_xpath", extension_module, activity_func)

def process2(IFrame对象,XPath,操作,基于当前lFrame全局查找,超时时间):
    """
    获取元素信息-XPath跨域
    通过XPath，跨域查找元素并获取元素信息
    * @param IFrame对象，
    * @param XPath，
    * @param 操作，
    * @param 基于当前lFrame全局查找，
    * @param 超时时间，
    * @return attribute，
    """
    outputs = ["attribute"]
    inputs = {"IFrame对象":IFrame对象,"XPath":XPath,"操作":操作,"基于当前lFrame全局查找":基于当前lFrame全局查找,"超时时间":超时时间}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.process2", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.process2",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.process2", extension_module, activity_func)

def process3(IFrame对象,XPath,基于当前lFrame全局查找,超时时间,属性名称):
    """
    获取元素属性-XPath跨域
    通过XPath，跨域查找元素并获取元素属性
    * @param IFrame对象，
    * @param XPath，
    * @param 基于当前lFrame全局查找，
    * @param 超时时间，
    * @param 属性名称，
    * @return attribute，
    """
    outputs = ["attribute"]
    inputs = {"IFrame对象":IFrame对象,"XPath":XPath,"基于当前lFrame全局查找":基于当前lFrame全局查找,"超时时间":超时时间,"属性名称":属性名称}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.iframe2.process3", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.iframe2.process3",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.iframe2.process3", extension_module, activity_func)

