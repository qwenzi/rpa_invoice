import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    可见的元素 = None
    if args is None:
        相似元素列表 = []
        网页对象 = None
    else:
        相似元素列表 = args.get("相似元素列表", [])
        网页对象 = args.get("网页对象", None)
    try:
        for loop_item in xbot_visual.workflow.list_iterator(list=相似元素列表, output_with_index=False, _block=("获取一组相似元素中可见的元素", 1, "ForEach列表循环")):
            if xbot_visual.web.browser.element_display(browser=网页对象, content_type="display", selector=loop_item, _block=("获取一组相似元素中可见的元素", 2, "IF 元素可见(web)")):
                可见的元素 = loop_item
                return
            #endif
        #endloop
        raise Exception("未找到可见的元素")
    finally:
        args["可见的元素"] = 可见的元素
