import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time

def main(args):
    try:
        初始化配置信息 = xbot_visual.process.run(process="process8", package=__name__, inputs={
            }, outputs=[
            "开始执行时间",
            "对话框信息",
            "处理总量",
        ], _block=("main", 1, "调用流程"))
        try:
            # 获取对应店铺账号密码
            #region 获取对应店铺账号密码
            if xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.店铺名称, operator="==", operand2="官旗", operator_options="{}", _block=("main", 5, "IF 条件")):
                账号 = "小熊电器官方旗舰店:小熊软糖"
                密码 = "130681Jia"
                
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.店铺名称, operator="==", operand2="生旗", operator_options="{}", _block=("main", 7, "Else IF")):
                账号 = "小熊生活电器旗舰店:小熊软糖"
                密码 = "130681Jia"
                
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.店铺名称, operator="==", operand2="母旗", operator_options="{}", _block=("main", 9, "Else IF")):
                账号 = "小熊母婴旗舰店:小熊软糖"
                密码 = "130681Jia"
                
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.店铺名称, operator="==", operand2="厨旗", operator_options="{}", _block=("main", 11, "Else IF")):
                账号 = "小熊厨房电器旗舰店:小熊软糖"
                密码 = "chufang123"
                
            #endif
            #endregion
            # 登录流程
            _ = xbot_visual.process.run(process="process3", package=__name__, inputs={
                "username": lambda: 账号,
                "password": lambda: 密码,
                }, outputs=[
            ], _block=("main", 16, "调用流程"))
            # programing.comment
            #region 发票流程
            if xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.发票流程, operator="==", operand2="发票1_点同意", operator_options="{}", _block=("main", 19, "IF 条件")):
                package.variables['流程名称'] = xbot_visual.programing.variable(value=lambda: 初始化配置信息.对话框信息.发票流程
                , _block=("main", 20, "设置变量"))
                _ = xbot_visual.process.run(process="process4", package=__name__, inputs={
                    "台账文件": lambda: 初始化配置信息.对话框信息.台账文件,
                    "店铺名称": lambda: 初始化配置信息.对话框信息.店铺名称,
                    }, outputs=[
                ], _block=("main", 21, "调用流程"))
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.发票流程, operator="==", operand2="发票2_首次上传", operator_options="{}", _block=("main", 22, "Else IF")):
                package.variables['流程名称'] = xbot_visual.programing.variable(value=lambda: 初始化配置信息.对话框信息.发票流程
                , _block=("main", 23, "设置变量"))
                _ = xbot_visual.process.run(process="process1", package=__name__, inputs={
                    "台账文件": lambda: 初始化配置信息.对话框信息.台账文件,
                    "发票文件夹": lambda: 初始化配置信息.对话框信息.发票文件夹,
                    "店铺名称": lambda: 初始化配置信息.对话框信息.店铺名称,
                    }, outputs=[
                ], _block=("main", 24, "调用流程"))
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.发票流程, operator="==", operand2="发票3_点冲红", operator_options="{}", _block=("main", 25, "Else IF")):
                package.variables['流程名称'] = xbot_visual.programing.variable(value=lambda: 初始化配置信息.对话框信息.发票流程
                , _block=("main", 26, "设置变量"))
                _ = xbot_visual.process.run(process="process6", package=__name__, inputs={
                    "台账文件": lambda: 初始化配置信息.对话框信息.台账文件,
                    "店铺名称": lambda: 初始化配置信息.对话框信息.店铺名称,
                    }, outputs=[
                ], _block=("main", 27, "调用流程"))
            elif xbot_visual.workflow.test(operand1=lambda: 初始化配置信息.对话框信息.发票流程, operator="==", operand2="发票4_重新上传", operator_options="{}", _block=("main", 28, "Else IF")):
                package.variables['流程名称'] = xbot_visual.programing.variable(value=lambda: 初始化配置信息.对话框信息.发票流程
                , _block=("main", 29, "设置变量"))
                _ = xbot_visual.process.run(process="process2", package=__name__, inputs={
                    "台账文件": lambda: 初始化配置信息.对话框信息.台账文件,
                    "发票文件夹": lambda: 初始化配置信息.对话框信息.发票文件夹,
                    "店铺名称": lambda: 初始化配置信息.对话框信息.店铺名称,
                    }, outputs=[
                ], _block=("main", 30, "调用流程"))
            #endif
            #endregion
            # 写入日志
            import json
            run_result ={"deal_sum":初始化配置信息.处理总量,"deal_num":glv['处理单量'],"status":"SUCCESS!","exception":"None"}       
            description = json.dumps(run_result,ensure_ascii=False)
            
            执行结果 = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_state", params={
                "app_name": glv['应用名称'].strip(),
                "start_time": lambda: 初始化配置信息.开始执行时间,
                "shop": lambda: 初始化配置信息.对话框信息.店铺名称,
                "creator": glv['创建人'].strip(),
                "description": lambda: description ,
                "remark": "END",
            }, _block=("main", 35, "调用模块"))
        except Exception as exception:
            exception = xbot_visual.trace(exception)
            import json
            run_result ={"deal_sum":初始化配置信息.处理总量,"deal_num":glv['处理单量'],"status":"FAIL!","exception":exception.strip()}       
            description = json.dumps(run_result,ensure_ascii=False)
            
            执行结果 = xbot_visual.process.invoke_module(module="ZRPA_Log", package=__name__, function="log_rpa_app_state", params={
                "app_name": glv['应用名称'].strip(),
                "start_time": lambda: 初始化配置信息.开始执行时间,
                "shop": lambda: 初始化配置信息.对话框信息.店铺名称,
                "creator": glv['创建人'].strip(),
                "description": lambda: description ,
                "remark": "EXCEPTION",
            }, _block=("main", 38, "调用模块"))
        #endtry
    finally:
        pass
