from .import package
import xbot_visual
from . import select_date
from . import auto_drop_selector

def process1(网页对象,操作目标):
    """
    滚动元素至可视区域
    该指令实现了将网页元素滚动至可视区域
    * @param 网页对象，
    * @param 操作目标，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process1", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process1",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process1", extension_module, activity_func)

def process2(网页对象,操作目标):
    """
    隐藏元素
    该指令实现了将网页中的元素隐藏
    * @param 网页对象，
    * @param 操作目标，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process2", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process2",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process2", extension_module, activity_func)

def process3(网页对象,操作目标):
    """
    显示元素
    该指令实现了将网页中的元素显示
    * @param 网页对象，
    * @param 操作目标，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process3", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process3",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process3", extension_module, activity_func)

def process12(网页对象,操作目标):
    """
    删除元素
    
    * @param 网页对象，
    * @param 操作目标，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process12", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process12",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process12", extension_module, activity_func)

def process14(网页对象,操作目标,保存路径):
    """
    元素长截图
    该指令实现了对元素长截图的操作
    * @param 网页对象，
    * @param 操作目标，
    * @param 保存路径，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"操作目标":操作目标,"保存路径":保存路径}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process14", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process14",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process14", extension_module, activity_func)

def process4(网页对象,操作目标):
    """
    获取元素背景颜色
    该指令实现了获取元素背景颜色操作
    * @param 网页对象，
    * @param 操作目标，
    * @return 背景色，
    """
    outputs = ["背景色"]
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process4", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process4",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process4", extension_module, activity_func)

def process6(网页对象,操作目标):
    """
    获取元素字体颜色
    该指令实现了获取元素字体颜色的操作
    * @param 网页对象，
    * @param 操作目标，
    * @return 字体颜色，
    """
    outputs = ["字体颜色"]
    inputs = {"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process6", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process6",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process6", extension_module, activity_func)

def process7(网页对象,JS库):
    """
    导入常用JS库
    该指令实现了在网页中导入JS库的操作
    * @param 网页对象，
    * @param JS库，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"JS库":JS库}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process7", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process7",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process7", extension_module, activity_func)

def process11(网页对象,JS来源类型,JS来源):
    """
    导入JS库
    该指令实现了在网页中导入JS库的操作
    * @param 网页对象，
    * @param JS来源类型，
    * @param JS来源，
    """
    outputs = []
    inputs = {"网页对象":网页对象,"JS来源类型":JS来源类型,"JS来源":JS来源}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process11", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process11",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process11", extension_module, activity_func)

def process8(网页对象):
    """
    获取当前激活的网页对象
    该指令实现了根据指定网页对象的浏览器类型获取当前激活的网页对象
    * @param 网页对象，
    * @return web_page，
    """
    outputs = ["web_page"]
    inputs = {"网页对象":网页对象}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process8", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process8",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process8", extension_module, activity_func)

def process10(保留网页对象):
    """
    关闭其他网页
    该指令实现了保留当前网页，关闭相同浏览器其他网页的操作
    * @param 保留网页对象，
    """
    outputs = []
    inputs = {"保留网页对象":保留网页对象}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process10", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process10",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process10", extension_module, activity_func)

def process13(禁用图片,指定端口,用户数据,指定用户,最大化,无痕模式,设置UA,隐藏崩溃弹窗):
    """
    浏览器启动配置
    该指令实现了配置浏览器启动命令行的操作
    * @param 禁用图片，
    * @param 指定端口，
    * @param 用户数据，
    * @param 指定用户，
    * @param 最大化，
    * @param 无痕模式，
    * @param 设置UA，
    * @param 隐藏崩溃弹窗，
    * @return 命令行，
    """
    outputs = ["命令行"]
    inputs = {"禁用图片":禁用图片,"指定端口":指定端口,"用户数据":用户数据,"指定用户":指定用户,"最大化":最大化,"无痕模式":无痕模式,"设置UA":设置UA,"隐藏崩溃弹窗":隐藏崩溃弹窗}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process13", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process13",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process13", extension_module, activity_func)

def process15(粗细,样式,颜色,网页对象,操作目标):
    """
    元素增加边框
    该指令实现了给元素增加边框的功能
    * @param 粗细，
    * @param 样式，
    * @param 颜色，
    * @param 网页对象，
    * @param 操作目标，
    """
    outputs = []
    inputs = {"粗细":粗细,"样式":样式,"颜色":颜色,"网页对象":网页对象,"操作目标":操作目标}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process15", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process15",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process15", extension_module, activity_func)

def process18(网页对象):
    """
    取消HTML缩放
    该指令实现了取消网页中HTML缩放的操作
    * @param 网页对象，
    """
    outputs = []
    inputs = {"网页对象":网页对象}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.web_action.process18", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.web_action.process18",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.web_action.process18", extension_module, activity_func)

