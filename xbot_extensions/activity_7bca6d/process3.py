import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        distance = "395"
        drag_start_element = None
        web_page = None
    else:
        distance = args.get("distance", "395")
        drag_start_element = args.get("drag_start_element", None)
        web_page = args.get("web_page", None)
    try:
        bound = xbot_visual.web.element.get_bounding(browser=web_page, element=drag_start_element, to96dpi=True, relative_to="screen", timeout="20", _block=("拖动滑块", 1, "获取元素位置(web)"))
        xbot_visual.win32.move_mouse(point_x=bound.center_x, point_y=bound.center_y, relative_to="screen", move_speed="slow", delay_after="1", _block=("拖动滑块", 2, "移动鼠标"))
        point_x, point_y = xbot_visual.win32.get_mouse_position(relative_to="screen", _block=("拖动滑块", 3, "获取鼠标当前位置"))
        xbot_visual.win32.manual_motion_on(motion_move=True, motion_click=True, motion_delay=True, min_time="1", max_time="3", _block=("拖动滑块", 4, "开启模拟真人操作"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="down", hardware_driver_click=False, keys="null", delay_after="1", _block=("拖动滑块", 5, "鼠标点击"))
        xbot_visual.win32.move_mouse(point_x=lambda: point_x+int(distance), point_y=lambda: point_y, relative_to="screen", move_speed="slow", delay_after="1", _block=("拖动滑块", 6, "移动鼠标"))
        xbot_visual.win32.click_mouse(is_move_mouse_before_click=False, point_x="0", point_y="0", relative_to="screen", move_speed="middle", button="left", click_type="up", hardware_driver_click=False, keys="null", delay_after="1", _block=("拖动滑块", 7, "鼠标点击"))
        xbot_visual.win32.manual_motion_off(_block=("拖动滑块", 8, "结束模拟真人操作"))
        #region 滑块拖动算法
        # process.invoke_module
        # programing.variable
        # programing.variable
        # win32.click_mouse
        # workflow.forin
        # programing.variable
        # process.invoke_module
        # programing.variable
        # workflow.if
        # programing.variable
        # workflow.endif
        # win32.move_mouse
        # workflow.endloop
        # win32.click_mouse
        #endregion
    finally:
        pass
