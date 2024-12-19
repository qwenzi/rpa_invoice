from .import package
import xbot_visual

def process1(流程名,流程参数,file_path):
    """
    动态调用子流程
    根据传入的流程名动态执行流程
    * @param 流程名，
    * @param 流程参数，
    * @param file_path，
    * @return process_result，
    """
    outputs = ["process_result"]
    inputs = {"流程名":流程名,"流程参数":流程参数,"file_path":file_path}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.dynamic_call.process1", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.dynamic_call.process1",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.dynamic_call.process1", extension_module, activity_func)

def process2(module,func_name,inputs,file_path):
    """
    动态调用模块
    动态调用应用内其他模块
    * @param module，
    * @param func_name，
    * @param inputs，
    * @param file_path，
    * @return invoke_result，
    """
    outputs = ["invoke_result"]
    inputs = {"module":module,"func_name":func_name,"inputs":inputs,"file_path":file_path}
    extension_module, activity_func = xbot_visual.process.activity_entry("xbot_extensions.dynamic_call.process2", __name__)
    try:
        return xbot_visual.process.run(process="xbot_extensions.dynamic_call.process2",package=__name__,inputs=inputs, outputs=outputs)
    finally:
        xbot_visual.process.replace_activity_module_to_entry_method("xbot_extensions.dynamic_call.process2", extension_module, activity_func)

