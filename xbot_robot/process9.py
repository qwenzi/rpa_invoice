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
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("C发票1_同意申请v1", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("C发票1_同意申请v1", 1,"获取已打开的网页对象"))
            time.sleep(3)
        xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_全部申请"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 2, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="5", start_number="1", stop_number="5", _block=("C发票1_同意申请v1", 3, "等待"))
        台账文件对象 = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=台账文件, save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("C发票1_同意申请v1", 4, "打开/新建Excel"))
        for loop_excel, loop_item_rownum, _ in xbot_visual.excel.loop_data_from_workbook_with_return_item_location(workbook=台账文件对象, loop_way="loop_row", range=None, begin_row_num="2", end_row_num="-1", begin_column_name=None, end_column_name=None, has_header_row=False, range_begin_row_num="2", range_begin_column_name=None, range_end_row_num="-1", range_end_column_name=None, sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("C发票1_同意申请v1", 5, "循环Excel内容")):
            # 获取开始操作时间
            开始操作时间 = xbot_visual.datetime.now(_block=("C发票1_同意申请v1", 7, "获取当前日期时间"))
            # 判断操作结果列是否为空
            if xbot_visual.workflow.test(operand1=loop_excel[7], operator="not empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("C发票1_同意申请v1", 9, "IF 条件")):
                continue
            #endif
            xbot_visual.web.element.input(browser=web_page, element=package.selector("给买家开票_全部申请_订单编号输入框"), text=loop_excel[0], append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 12, "填写输入框(web)"))
            xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_全部申请_搜索按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 13, "点击元素(web)"))
            if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("搜索后没有数据"), _block=("C发票1_同意申请v1", 14, "IF 元素可见(web)")):
                import json
                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":"","ART_reason":"网页搜索不出该订单号内容","extra_remark":""}
                description = json.dumps(key_info,ensure_ascii=False) 
                glv['处理单量']+=1
                remark="人工-状态异常"
                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("C发票1_同意申请v1", 16, "写入内容至Excel工作表"))
                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                    "app_name": glv['应用名称'].strip(),
                    "flow_name": glv['流程名称'].strip(),
                    "start_time": lambda: 开始操作时间,
                    "action_method": "ART",
                    "action_result": "FAIL",
                    "action_status": "EXCEPTION",
                    "creator": glv['创建人'].strip(),
                    "description": lambda: description,
                    "remark": lambda: remark,
                }, _block=("C发票1_同意申请v1", 17, "调用模块"))
                continue
            #endif
            发票申请状态列表 = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("发票申请状态_相似元素组"), css_selector="", xpath_selector="", is_related_parent=False, parent=None, operation="text", absolute_url=False, attribute_name=None, timeout="20", output_with_element_count=False, _block=("C发票1_同意申请v1", 20, "获取相似元素列表(web)"))
            if xbot_visual.workflow.test(operand1=发票申请状态列表, operator="not in", operand2="待处理申请", operator_options="{\"ignoreCase\":\"False\"}", _block=("C发票1_同意申请v1", 21, "IF 条件")):
                import json
                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票申请状态列表,"ART_reason":"不是待处理申请状态","extra_remark":""} 
                description = json.dumps(key_info,ensure_ascii=False)
                glv['处理单量']+=1
                remark = "人工-处理完成"
                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("C发票1_同意申请v1", 23, "写入内容至Excel工作表"))
                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                    "app_name": glv['应用名称'].strip(),
                    "flow_name": glv['流程名称'].strip(),
                    "start_time": 开始操作时间,
                    "action_method": "RPA",
                    "action_result": "PASS",
                    "action_status": "NROMAL",
                    "creator": glv['创建人'].strip(),
                    "description": lambda: description,
                    "remark": lambda: remark,
                }, _block=("C发票1_同意申请v1", 24, "调用模块"))
                continue
            #endif
            for 当前父元素 in xbot_visual.web.element.iter_all_elements(browser=web_page, selector=package.selector("全部申请_表格"), operation="element", absolute_url=False, attribute_name=None, timeout="20", loop_start_index="0", loop_end_index="-1", output_with_index=False, _block=("C发票1_同意申请v1", 27, "循环相似元素(web)")):
                当前子元素_发票申请状态 = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("全部申请_发票申请状态_相似元素组"), css_selector="", xpath_selector="", is_related_parent=True, parent=当前父元素, timeout="20", _block=("C发票1_同意申请v1", 28, "获取元素对象(web)"))
                当前子元素_详情按钮 = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("详情_相似元素组"), css_selector="", xpath_selector="", is_related_parent=True, parent=当前父元素, timeout="20", _block=("C发票1_同意申请v1", 29, "获取元素对象(web)"))
                if xbot_visual.workflow.test(operand1=当前子元素_发票申请状态.get_text(), operator="in", operand2="待处理申请", operator_options="{\"ignoreCase\":\"False\"}", _block=("C发票1_同意申请v1", 30, "IF 条件")):
                    xbot_visual.web.element.click(browser=web_page, element=当前子元素_详情按钮, simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 31, "点击元素(web)"))
                    发票详情订单号 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("发票申请详情_订单号"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("C发票1_同意申请v1", 32, "获取元素信息(web)"))
                    if xbot_visual.workflow.test(operand1=发票详情订单号, operator="!=", operand2=loop_excel[0], operator_options="{}", _block=("C发票1_同意申请v1", 33, "IF 条件")):
                        import json
                        key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票申请状态列表,"ART_reason":"网页订单号与Excel订单号不一致","extra_remark":""} 
                        description = json.dumps(key_info,ensure_ascii=False)
                        glv['处理单量']+=1
                        remark="人工-检验不通过"
                        xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("C发票1_同意申请v1", 35, "写入内容至Excel工作表"))
                        invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                            "app_name": glv['应用名称'].strip(),
                            "flow_name": glv['流程名称'].strip(),
                            "start_time": 开始操作时间,
                            "action_method": "ART",
                            "action_result": "FAIL",
                            "action_status": "INVALID",
                            "creator": glv['创建人'].strip(),
                            "description": lambda: description,
                            "remark": lambda: remark,
                        }, _block=("C发票1_同意申请v1", 36, "调用模块"))
                        xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 37, "点击元素(web)"))
                        continue
                    #endif
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_同意"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 40, "点击元素(web)"))
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("手动上传发票选项"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 41, "点击元素(web)"))
                    xbot_visual.web.element.click(browser=web_page, element=package.selector("请选择开票方式_确定按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("C发票1_同意申请v1", 42, "点击元素(web)"))
                    import json
                    key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票申请状态列表,"ART_reason":"","extra_remark":""} 
                    description = json.dumps(key_info,ensure_ascii=False)
                    glv['处理单量']+=1
                    remark="RPA-处理完成"
                    xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("C发票1_同意申请v1", 44, "写入内容至Excel工作表"))
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
                    }, _block=("C发票1_同意申请v1", 45, "调用模块"))
                #endif
            #endloop
        #endloop
        xbot_visual.excel.close(operation="close_specified", excel_instance=台账文件对象, close_way="save", filename=None, overwrite_file=True, close_process="office", task_kill=True, _block=("C发票1_同意申请v1", 49, "关闭Excel"))
    finally:
        pass
