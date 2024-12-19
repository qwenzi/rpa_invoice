import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    开始执行时间 = None
    对话框信息 = None
    处理总量 = 0
    try:
        对话框信息 = xbot_visual.dialog.show_custom_dialog(settings="{\"dialogTitle\":null,\"height\":0,\"width\":0,\"timeout\":0,\"autoCloseButton\":null,\"use_wait_timeout\":false,\"canRememberContent\":false,\"settings\":{\"editors\":[{\"type\":\"Select\",\"label\":\"选择流程\",\"VariableName\":\"发票流程\",\"value\":\"发票1_点同意\",\"nullText\":null,\"isTextEditable\":false,\"options\":[\"发票1_点同意\",\"发票2_首次上传\",\"发票3_点冲红\",\"发票4_重新上传\"],\"autoCloseOnSelected\":false},{\"type\":\"Select\",\"label\":\"选择店铺\",\"VariableName\":\"店铺名称\",\"value\":\"官旗\",\"nullText\":null,\"isTextEditable\":false,\"options\":[\"官旗\",\"生旗\",\"母旗\",\"厨旗\"],\"autoCloseOnSelected\":false},{\"type\":\"File\",\"label\":\"选择台账表格\",\"VariableName\":\"台账文件\",\"kind\":0,\"filter\":\"所有文件|*.*\",\"value\":null,\"nullText\":\"请选择路径\"},{\"type\":\"File\",\"label\":\"选择发票文件夹\",\"VariableName\":\"发票文件夹\",\"kind\":2,\"filter\":\"所有文件|*.*\",\"value\":null,\"nullText\":\"请选择路径\"}],\"buttons\":[{\"type\":\"Button\",\"label\":\"确定\",\"theme\":\"white\",\"hotKey\":\"Return\"},{\"type\":\"Button\",\"label\":\"取消\",\"theme\":\"white\",\"hotKey\":\"Escape\"}]}}", dialog_title="", default_btn="确定", is_auto_click=False, timeout=None, globals=globals(), locals=locals(), storage_key="8048acdd-dc9d-4a5b-b6fe-f32a2740a31c", _block=("A初始化配置", 1, "打开自定义对话框"))
        # 获取流程开始执行时间
        开始执行时间 = xbot_visual.datetime.now(_block=("A初始化配置", 3, "获取当前日期时间"))
        # 获取台账总条数
        excel_instance = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=lambda: 对话框信息.台账文件, save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("A初始化配置", 5, "打开/新建Excel"))
        处理总量 = xbot_visual.excel.get_row_count(workbook=excel_instance, sheet_name="", _block=("A初始化配置", 6, "读取Excel总行数"))
        package.variables['处理单量'] = xbot_visual.excel.get_first_free_row_on_column(workbook=excel_instance, column_name="H", sheet_name="", _block=("A初始化配置", 7, "获取列上第一个可用行"))
        package.variables['处理单量'] = xbot_visual.programing.variable(value=lambda: glv['处理单量']-1
        , _block=("A初始化配置", 8, "设置变量"))
        xbot_visual.excel.close(operation="close_specified", excel_instance=excel_instance, close_way="save", filename=None, overwrite_file=True, close_process="office", task_kill=True, _block=("A初始化配置", 9, "关闭Excel"))
        # 初始化
        import platform
        import json
        run_result ={"deal_sum":处理总量,"deal_num":glv['处理单量'],"status":"SUCCESS!","exception":"None"}       
        description = json.dumps(run_result,ensure_ascii=False)
        glv['创建人'] = platform.node()
        
        invoke_result = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_state", params={
            "app_name": glv['应用名称'],
            "start_time": 开始执行时间,
            "shop": lambda: 对话框信息.店铺名称,
            "creator": glv['创建人'].strip(),
            "description": lambda: description,
            "remark": "START",
        }, _block=("A初始化配置", 12, "调用模块"))
    finally:
        args["开始执行时间"] = 开始执行时间
        args["对话框信息"] = 对话框信息
        args["处理总量"] = 处理总量
