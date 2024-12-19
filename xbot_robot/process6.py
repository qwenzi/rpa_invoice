import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        台账文件 = ""
        店铺名称 = ""
    else:
        台账文件 = args.get("台账文件", "")
        店铺名称 = args.get("店铺名称", "")
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("E发票3_点冲红", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("E发票3_点冲红", 1,"获取已打开的网页对象"))
            time.sleep(3)
        xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_全部申请"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 2, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="5", start_number="1", stop_number="5", _block=("E发票3_点冲红", 3, "等待"))
        台账文件对象 = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=台账文件, save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("E发票3_点冲红", 4, "打开/新建Excel"))
        for loop_excel, loop_item_rownum, _ in xbot_visual.excel.loop_data_from_workbook_with_return_item_location(workbook=台账文件对象, loop_way="loop_row", range=None, begin_row_num="2", end_row_num="-1", begin_column_name=None, end_column_name=None, has_header_row=False, range_begin_row_num=None, range_begin_column_name=None, range_end_row_num=None, range_end_column_name=None, sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("E发票3_点冲红", 5, "循环Excel内容")):
            开始操作时间 = xbot_visual.datetime.now(_block=("E发票3_点冲红", 6, "获取当前日期时间"))
            # 判断操作结果列是否为空
            if xbot_visual.workflow.test(operand1=loop_excel[1], operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("E发票3_点冲红", 8, "IF 条件")):
                continue
            #endif
            for _xbot_retry_time in range(4):
                try:
                    web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("E发票3_点冲红", 11, "获取已打开的网页对象"))
                    break
                except Exception as e:
                    if _xbot_retry_time == 3:
                        raise e
                    else:
                        xbot_visual.programing.log(type='info',text=e,_block=("E发票3_点冲红", 11,"获取已打开的网页对象"))
                time.sleep(3)
            xbot_visual.web.element.input(browser=web_page, element=package.selector("给买家开票_全部申请_订单编号输入框"), text=loop_excel[0], append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 12, "填写输入框(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_全部申请_搜索按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 13, "点击元素(web)"))
            发票状态 = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("发票状态_相似元素组"), css_selector="", xpath_selector="", is_related_parent=False, parent=None, operation="text", absolute_url=False, attribute_name=None, timeout="20", output_with_element_count=True, _block=("E发票3_点冲红", 14, "获取相似元素列表(web)"))
            发票状态的数量 = len(发票状态)
            xbot_visual.programing.log(type="info", text="订单号" + xbot_visual.sh_str(loop_excel[0]) + "，共" + xbot_visual.sh_str(发票状态的数量) + "条，" + xbot_visual.sh_str(发票状态), _block=("E发票3_点冲红", 15, "打印日志"))
            if xbot_visual.workflow.test(operand1=发票状态的数量, operator="!=", operand2="1", operator_options="{}", _block=("E发票3_点冲红", 16, "IF 条件")):
                import json
                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态,"ART_reason":"该订单号存在多张发票","extra_remark":""}
                description = json.dumps(key_info,ensure_ascii=False)
                glv['处理单量']+=1
                remark="人工-状态异常"
                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("E发票3_点冲红", 18, "写入内容至Excel工作表"))
                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                    "app_name": glv['应用名称'].strip(),
                    "flow_name": glv['流程名称'].strip(),
                    "start_time": 开始操作时间,
                    "action_method": "ART",
                    "action_result": "FAIL",
                    "action_status": "EXCEPTION",
                    "creator": glv['创建人'].strip(),
                    "description": lambda: description,
                    "remark": lambda: remark,
                }, _block=("E发票3_点冲红", 19, "调用模块"))
                continue
            #endif
            发票状态的文本 = xbot_visual.programing.variable(value=发票状态[0]
            , _block=("E发票3_点冲红", 22, "设置变量"))
            if xbot_visual.workflow.test(operand1=发票状态的文本, operator="in", operand2="蓝票", operator_options="{\"ignoreCase\":\"False\"}", _block=("E发票3_点冲红", 23, "IF 条件")):
                xbot_visual.programing.log(type="info", text="订单号" + xbot_visual.sh_str(loop_excel[0]) + "，发票状态" + xbot_visual.sh_str(发票状态的文本) + "，符合冲红", _block=("E发票3_点冲红", 24, "打印日志"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("详情_相似元素组"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 25, "点击元素(web)"))
                发票内订单号 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("发票申请详情_订单号"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("E发票3_点冲红", 26, "获取元素信息(web)"))
                if xbot_visual.workflow.test(operand1=发票内订单号, operator="!=", operand2=loop_excel[0], operator_options="{}", _block=("E发票3_点冲红", 27, "IF 条件")):
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 28, "点击元素(web)"))
                    import json
                    key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态,"ART_reason":"网页订单号与Excel订单号不一致","extra_remark":""} 
                    description = json.dumps(key_info,ensure_ascii=False)
                    glv['处理单量']+=1
                    remark="人工-检验不通过"
                    xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("E发票3_点冲红", 30, "写入内容至Excel工作表"))
                    invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                        "app_name": glv['应用名称'].strip(),
                        "flow_name": glv['流程名称'].strip(),
                        "start_time": 开始操作时间,
                        "action_method": "ART",
                        "action_result": "FAIL",
                        "action_status": "EXCEPTION",
                        "creator": glv['创建人'].strip(),
                        "description": lambda: description,
                        "remark": lambda: remark,
                    }, _block=("E发票3_点冲红", 31, "调用模块"))
                    continue
                #endif
                xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_冲红按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 34, "点击元素(web)"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("E发票3_点冲红", 35, "点击元素(web)"))
                import json
                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态,"ART_reason":"","extra_remark":""} 
                description = json.dumps(key_info,ensure_ascii=False)
                glv['处理单量']+=1
                remark="RPA-处理完成"
                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("E发票3_点冲红", 37, "写入内容至Excel工作表"))
                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                    "app_name": glv['应用名称'].strip(),
                    "flow_name": glv['流程名称'].strip(),
                    "start_time": 开始操作时间,
                    "action_method": "RPA",
                    "action_result": "SUCCESS",
                    "action_status": "NORMAL",
                    "creator": glv['创建人'].strip(),
                    "description": lambda: description,
                    "remark": lambda: remark,
                }, _block=("E发票3_点冲红", 38, "调用模块"))
            else:
                import json
                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态,"ART_reason":"发票状态不是蓝票","extra_remark":""}    
                description = json.dumps(key_info,ensure_ascii=False)
                glv['处理单量']+=1
                remark="人工-已处理"
                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("E发票3_点冲红", 41, "写入内容至Excel工作表"))
                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                    "app_name": glv['应用名称'].strip(),
                    "flow_name": glv['流程名称'].strip(),
                    "start_time": 开始操作时间,
                    "action_method": "RPA",
                    "action_result": "PASS",
                    "action_status": "NORMAL",
                    "creator": glv['创建人'].strip(),
                    "description": lambda: description,
                    "remark": lambda: remark,
                }, _block=("E发票3_点冲红", 42, "调用模块"))
                continue
            #endif
        #endloop
        xbot_visual.excel.close(operation="close_specified", excel_instance=台账文件对象, close_way="save", filename=None, overwrite_file=True, close_process="office", task_kill=True, _block=("E发票3_点冲红", 46, "关闭Excel"))
    finally:
        pass
