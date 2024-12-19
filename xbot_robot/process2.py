import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    if args is None:
        台账文件 = ""
        发票文件夹 = None
        店铺名称 = ""
    else:
        台账文件 = args.get("台账文件", "")
        发票文件夹 = args.get("发票文件夹", None)
        店铺名称 = args.get("店铺名称", "")
    try:
        for _xbot_retry_time in range(4):
            try:
                web_page = xbot_visual.web.get(web_type="chrome", mode="activated", value="", use_wildcard=False, silent_running=False, wait_load_completed=True, load_timeout="20", stop_load_if_load_timeout="handleExcept", open_page=False, url=None, _block=("F发票4_重新上传", 1, "获取已打开的网页对象"))
                break
            except Exception as e:
                if _xbot_retry_time == 3:
                    raise e
                else:
                    xbot_visual.programing.log(type='info',text=e,_block=("F发票4_重新上传", 1,"获取已打开的网页对象"))
            time.sleep(3)
        xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_开票成功"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 2, "点击元素(web)"))
        xbot_visual.programing.sleep(random_number=False, seconds="5", start_number="1", stop_number="5", _block=("F发票4_重新上传", 3, "等待"))
        # 打开读取台账文件
        台账文件对象 = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=台账文件, save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("F发票4_重新上传", 5, "打开/新建Excel"))
        xbot_visual.excel.active(workbook=台账文件对象, mode="name", value=店铺名称.value, _block=("F发票4_重新上传", 6, "激活Sheet页"))
        for loop_excel, loop_item_rownum, _ in xbot_visual.excel.loop_data_from_workbook_with_return_item_location(workbook=台账文件对象, loop_way="loop_row", range=None, begin_row_num="2", end_row_num="-1", begin_column_name=None, end_column_name=None, has_header_row=False, range_begin_row_num=None, range_begin_column_name=None, range_end_row_num=None, range_end_column_name=None, sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("F发票4_重新上传", 7, "循环Excel内容")):
            # 开始处理，判断操作结果列是否为空
            if xbot_visual.workflow.test(operand1=loop_excel[7], operator="empty value", operand2="", operator_options="{\"values\":\"None,Empty,Blank\"}", _block=("F发票4_重新上传", 9, "IF 条件")):
                开始操作时间 = xbot_visual.datetime.now(_block=("F发票4_重新上传", 10, "获取当前日期时间"))
                file_paths = xbot_visual.dir.find_files(path=发票文件夹.folder, patterns="dzfp_" + xbot_visual.sh_str(loop_excel[2]) + "*", find_subdir=False, skip_hidden_file=False, is_sort=False, sort_by="name", sort_way="increase", _block=("F发票4_重新上传", 11, "获取文件列表"))
                # 判断是否有发票文件
                if xbot_visual.workflow.test(operand1=len(file_paths), operator="==", operand2="0", operator_options="{}", _block=("F发票4_重新上传", 13, "IF 条件")):
                    import json
                    key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":"","ART_reason":"找不到发票文件","extra_remark":""}    
                    description = json.dumps(key_info,ensure_ascii=False)
                    glv['处理单量']+=1
                    remark="人工-找不到发票文件"
                    xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 15, "写入内容至Excel工作表"))
                    invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                        "app_name": glv['应用名称'].strip(),
                        "flow_name": glv['流程名称'].strip(),
                        "start_time": 开始操作时间,
                        "action_method": "ART",
                        "action_result": "FAIL",
                        "action_status": "EXCEPTION",
                        "creator": glv['创建人'].strip(),
                        "description": lambda: description ,
                        "remark": lambda: remark,
                    }, _block=("F发票4_重新上传", 16, "调用模块"))
                    continue
                #endif
                xbot_visual.web.element.input(browser=web_page, element=package.selector("给买家开票_全部申请_订单编号输入框"), text=loop_excel[0], append=False, simulate=False, driver_input=False, save_to_clipboard=True, input_type="clipboard", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 19, "填写输入框(web)"))
                xbot_visual.web.element.click(browser=web_page, element=package.selector("给买家开票_全部申请_搜索按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 20, "点击元素(web)"))
                if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("搜索后没有数据"), _block=("F发票4_重新上传", 21, "IF 元素可见(web)")):
                    import json
                    key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":"","ART_reason":"网页搜索不出该订单号内容","extra_remark":""}    
                    description = json.dumps(key_info,ensure_ascii=False)
                    glv['处理单量']+=1
                    remark="人工-状态异常"
                    xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 23, "写入内容至Excel工作表"))
                    invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                        "app_name": glv['应用名称'].strip(),
                        "flow_name": glv['流程名称'].strip(),
                        "start_time": 开始操作时间,
                        "action_method": "ART",
                        "action_result": "FAIL",
                        "action_status": "EXCEPTION",
                        "creator": glv['创建人'].strip(),
                        "description": lambda: description ,
                        "remark": lambda: remark,
                    }, _block=("F发票4_重新上传", 24, "调用模块"))
                    continue
                #endif
                发票状态列表 = xbot_visual.web.element.get_all_elements(browser=web_page, select_type="selector", selector=package.selector("全部申请_发票申请状态_相似元素组"), css_selector="", xpath_selector="", is_related_parent=False, parent=None, operation="text", absolute_url=False, attribute_name=None, timeout="20", output_with_element_count=False, _block=("F发票4_重新上传", 27, "获取相似元素列表(web)"))
                if xbot_visual.workflow.test(operand1=发票状态列表, operator="in", operand2="蓝票", operator_options="{\"ignoreCase\":\"False\"}", _block=("F发票4_重新上传", 28, "IF 条件")):
                    import json
                    key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态列表,"ART_reason":"列表中发票包含蓝票","extra_remark":""}    
                    description = json.dumps(key_info,ensure_ascii=False)
                    glv['处理单量']+=1
                    remark="人工-已处理"
                    xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 30, "写入内容至Excel工作表"))
                    invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                        "app_name": glv['应用名称'].strip(),
                        "flow_name": glv['流程名称'].strip(),
                        "start_time": 开始操作时间,
                        "action_method": "RPA",
                        "action_result": "PASS",
                        "action_status": "NORMAL",
                        "creator": glv['创建人'].strip(),
                        "description": lambda: description ,
                        "remark": lambda: remark,
                    }, _block=("F发票4_重新上传", 31, "调用模块"))
                    continue
                #endif
                # 循环搜索结果
                for 当前循环位置index, 当前父元素 in enumerate(xbot_visual.web.element.iter_all_elements(browser=web_page, selector=package.selector("全部申请_表格"), operation="element", absolute_url=False, attribute_name=None, timeout="20", loop_start_index="0", loop_end_index="-1", output_with_index=True, _block=("F发票4_重新上传", 35, "循环相似元素(web)"))):
                    # 获取当前循环行的子元素对象
                    当前子元素_发票类型 = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("发票类型_相似元素组"), css_selector="", xpath_selector="", is_related_parent=True, parent=当前父元素, timeout="20", _block=("F发票4_重新上传", 37, "获取元素对象(web)"))
                    当前子元素_详情按钮 = xbot_visual.web.element.get_element(browser=web_page, select_type="selector", selector=package.selector("详情_相似元素组"), css_selector="", xpath_selector="", is_related_parent=True, parent=当前父元素, timeout="20", _block=("F发票4_重新上传", 38, "获取元素对象(web)"))
                    if xbot_visual.workflow.test(operand1=当前子元素_发票类型, operator="in", operand2="已冲红", operator_options="{\"ignoreCase\":\"False\"}", _block=("F发票4_重新上传", 39, "IF 条件")):
                        xbot_visual.web.element.click(browser=web_page, element=当前子元素_详情按钮, simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 40, "点击元素(web)"))
                        xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_录入发票"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 41, "点击元素(web)"))
                        网页订单号 = xbot_visual.web.element.get_details(browser=web_page, element=package.selector("发票申请详情_订单号"), operation="text", absolute_url=False, attribute_name=None, relative_to="screen", to96dpi=True, timeout="20", _block=("F发票4_重新上传", 42, "获取元素信息(web)"))
                        xbot_visual.web.element.click(browser=web_page, element=package.selector("录入发票信息_全电普通发票"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 43, "点击元素(web)"))
                        xbot_visual.web.element.click(browser=web_page, element=package.selector("录入发票信息_上传发票PDF/OFD"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 44, "点击元素(web)"))
                        xbot_visual.web.handle_upload_dialog(web_type="chrome", dialog_result="OK", filename=lambda: file_paths[0], simulate=False, clipboard_input=False, input_type="automatic", wait_appear_timeout="20", force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", _block=("F发票4_重新上传", 45, "处理上传对话框"))
                        xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("F发票4_重新上传", 46, "等待"))
                        # 如果出现不支持自动识别发票，自动填入信息
                        if xbot_visual.web.browser.element_display(browser=web_page, content_type="display", selector=package.selector("录入发票信息_无法识别发票提示"), _block=("F发票4_重新上传", 48, "IF 元素可见(web)")):
                            xbot_visual.web.element.input(browser=web_page, element=package.selector("录入发票信息_发票号码"), text=loop_excel[2], append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 49, "填写输入框(web)"))
                            xbot_visual.web.element.input(browser=web_page, element=package.selector("录入发票信息_开票日期"), text=loop_excel[3], append=False, simulate=True, driver_input=False, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 50, "填写输入框(web)"))
                            xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("F发票4_重新上传", 51, "键盘输入"))
                            # 提交校验
                            if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 网页订单号.strip(),"operand2": loop_excel[0],"operator": "=="}], _block=("F发票4_重新上传", 53, "IF 多条件")):
                                xbot_visual.web.element.click(browser=web_page, element=package.selector("录入发票信息_完成开票"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 54, "点击元素(web)"))
                                import json
                                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态列表,"ART_reason":"","extra_remark":"该发票无法自动识别"}    
                                description = json.dumps(key_info,ensure_ascii=False)
                                glv['处理单量']+=1
                                remark="RPA-处理完成"
                                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 56, "写入内容至Excel工作表"))
                                invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                                    "app_name": glv['应用名称'].strip(),
                                    "flow_name": glv['流程名称'].strip(),
                                    "start_time": 开始操作时间,
                                    "action_method": "RPA",
                                    "action_result": "SUCCESS",
                                    "action_status": "NORNAL",
                                    "creator": glv['创建人'].strip(),
                                    "description": lambda: description,
                                    "remark": lambda: remark,
                                }, _block=("F发票4_重新上传", 57, "调用模块"))
                                break
                            else:
                                import json
                                key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态列表,"ART_reason":"网页订单号与Excel订单号不一致","extra_remark":""}    
                                description = json.dumps(key_info,ensure_ascii=False)
                                glv['处理单量']+=1
                                remark="人工-检验不通过"
                                xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 61, "写入内容至Excel工作表"))
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
                                }, _block=("F发票4_重新上传", 62, "调用模块"))
                                xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 63, "点击元素(web)"))
                                break
                            #endif
                        #endif
                        # 网页订单号和表格订单号一致才提交
                        if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": 网页订单号.strip(),"operand2": loop_excel[0],"operator": "=="}], _block=("F发票4_重新上传", 68, "IF 多条件")):
                            xbot_visual.web.element.click(browser=web_page, element=package.selector("录入发票信息_完成开票"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 69, "点击元素(web)"))
                            import json
                            key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态列表,"ART_reason":"","extra_remark":""}    
                            description = json.dumps(key_info,ensure_ascii=False)
                            glv['处理单量']+=1
                            remark="RPA-处理完成"
                            xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 71, "写入内容至Excel工作表"))
                            invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_detail", params={
                                "app_name": glv['应用名称'].strip(),
                                "flow_name": glv['流程名称'].strip(),
                                "start_time": 开始操作时间,
                                "action_method": "RPA",
                                "action_result": "SUCCESS",
                                "action_status": "NORNAL",
                                "creator": glv['创建人'].strip(),
                                "description": lambda: description,
                                "remark": lambda: remark,
                            }, _block=("F发票4_重新上传", 72, "调用模块"))
                        else:
                            import json
                            key_info ={"order_id":loop_excel[0],"invoices_name":loop_excel[1],"invoices_code":loop_excel[2],"invoices_status":发票状态列表,"ART_reason":"网页订单号与Excel订单号不一致","extra_remark":""}    
                            description = json.dumps(key_info,ensure_ascii=False)
                            glv['处理单量']+=1
                            remark="人工-检验不通过"
                            xbot_visual.excel.write_data_to_workbook(workbook=台账文件对象, write_range="area", write_way="append", write_column_way="override", row_num=loop_item_rownum, column_name="H", begin_row_num="1", begin_column_name="", content=lambda: remark, sheet_name="", write_as_text_cols=None, _block=("F发票4_重新上传", 75, "写入内容至Excel工作表"))
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
                            }, _block=("F发票4_重新上传", 76, "调用模块"))
                            xbot_visual.web.element.click(browser=web_page, element=package.selector("发票申请详情_关闭按钮"), simulate=True, move_mouse=False, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("F发票4_重新上传", 77, "点击元素(web)"))
                        #endif
                    #endif
                #endloop
            #endif
        #endloop
        xbot_visual.excel.close(operation="close_specified", excel_instance=台账文件对象, close_way="save", filename=None, overwrite_file=True, close_process="office", task_kill=True, _block=("F发票4_重新上传", 83, "关闭Excel"))
    finally:
        pass
