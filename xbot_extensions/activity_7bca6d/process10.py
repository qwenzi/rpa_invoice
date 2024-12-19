import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        xbot_visual.image.hover(window_kind="currentactivatewindow", window=None, template_images=[package.image_selector("3-1"),package.image_selector("1-1"),package.image_selector("2-1")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="5", delay_after="1", _block=("拖动滑块京东", 1, "鼠标悬停在图像上"))
        for loop_index in xbot_visual.workflow.range_iterator(start="1", stop="3", step="1", _block=("拖动滑块京东", 2, "For次数循环")):
            X, Y = xbot_visual.win32.get_mouse_position(relative_to="screen", _block=("拖动滑块京东", 3, "获取鼠标当前位置"))
            bound = xbot_visual.web.element.get_bounding(browser=web_page, element=package.selector("京东_滑动条"), to96dpi=True, relative_to="screen", _block=("拖动滑块京东", 4, "获取元素位置(web)"))
            xbot_visual.web.element.hover(browser=web_page, element=package.selector("京东_滑动条"), simulate=True, delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", _block=("拖动滑块京东", 5, "鼠标悬停在元素上(web)"))
            xbot_visual.win32.move_mouse(point_x=bound.center_x, point_y=bound.center_y, relative_to="screen", move_speed="slow", delay_after="1", _block=("拖动滑块京东", 6, "移动鼠标"))
            X1, Y1 = xbot_visual.win32.get_mouse_position(relative_to="screen", _block=("拖动滑块京东", 7, "获取鼠标当前位置"))
            xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="down", hardware_driver_click=False, keys="null", delay_after="1", _block=("拖动滑块京东", 8, "鼠标点击"))
            xbot_visual.win32.move_mouse(point_x=lambda: X+3, point_y=Y1, relative_to="screen", move_speed="slow", delay_after="1", _block=("拖动滑块京东", 9, "移动鼠标"))
            xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="up", hardware_driver_click=False, keys="null", delay_after="1", _block=("拖动滑块京东", 10, "鼠标点击"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="undisplay", selector=package.selector("完成拼图验证"), _block=("拖动滑块京东", 11, "IF 元素可见(web)")):
                break
            else:
                xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("拖动滑块京东", 14, "延迟执行"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("换一张"), simulate=True, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", _block=("拖动滑块京东", 15, "点击元素(web)"))
            #endif
        #endloop
    finally:
        pass
