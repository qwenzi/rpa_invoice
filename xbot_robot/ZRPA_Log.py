# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep
from .import package
from .package import variables as glv
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
import time

def main(args):
    pass

# 日志类
class RPALog():
    def __init__(self):
        # 创建数据库连接
        self.conn = create_engine('mysql+pymysql://fantianwen:QE2AR7stw4$@10.1.12.194:3306/rpadb').connect()
        self.now_date = datetime.now()
    # RPA应用运行记录表
    def log_app_state(self,app_name, start_time, shop, creator, description, remark):
        app_name = app_name
        start_time =start_time
        end_time = self.now_date
        shop = shop
        creator = creator
        updater = creator
        runtime = end_time - start_time
        description = description
        remark = remark
        # 插入数据sql
        insert_log_sql = text("INSERT INTO BEARCSC_RPA_APPLICATION_LOG(app_name, start_time, end_time, shop, creator, updater, runtime, description, remark)"
                           " values(:app_name, :start_time, :end_time, :shop, :creator, :updater, :runtime, :description, :remark)")
        # print(insert_log_sql)                   
        # 执行删除操作
        self.conn.execute(insert_log_sql,{'app_name':app_name,'start_time':str(start_time),'end_time':str(end_time),'shop':shop
                            ,'creator':creator,'updater':updater,'runtime':runtime,'description':description,'remark':remark})
        self.conn.commit()
        return True


    # 发票自动上传明细日志
    def log_app_detail (self, app_name, flow_name, start_time
                        , action_method, action_result, action_status, creator, description, remark):
        strat_time = start_time
        end_time = self.now_date
        runtime = end_time - start_time
        action_type = action_method 
        action_result = action_result
        action_status = action_status
        creator = creator
        updater = creator
        description = description
        remark = remark
        # 插入数据sql
        insert_log_sql = text("INSERT INTO BEARCSC_RPA_APPLICATION_DETAIL_LOG(app_name, flow_name, start_time, end_time, runtime, action_method, action_result, action_status, creator, updater, description, remark)"
                        "values(:app_name, :flow_name, :start_time,:end_time, :runtime, :action_method, :action_result, :action_status, :creator, :updater, :description, :remark)")
        # print(insert_log_sql)                   
        # 执行删除操作
        self.conn.execute(insert_log_sql,{'app_name':app_name,'flow_name':flow_name,'start_time':str(start_time),'end_time':str(end_time),'runtime':runtime,'action_method':action_method,
        'action_result':action_result,'action_status':action_status,'creator':creator,'updater':updater,'description':description,'remark':remark})
        self.conn.commit()
        return True




# RPA流程启停情况日志
def log_rpa_app_state(app_name, start_time, shop, creator, description, remark):
    RPALog().log_app_state(app_name, start_time, shop, creator, description, remark)
    return 'INSERT SUCCESS'


# 发票录入明细日志
def log_rpa_app_detail(app_name, flow_name, start_time
                        , action_method, action_result, action_status, creator, description, remark):
    RPALog().log_app_detail(app_name, flow_name, start_time
                        , action_method, action_result, action_status, creator, description, remark)

    return 'INSERT SUCCESS'

