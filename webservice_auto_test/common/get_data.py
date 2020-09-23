# —— coding :utf-8 ——
# @time:    2020/9/15 0:45
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    get_data.py

import os
from turtle import pd
from common.get_reg_name import GetRegName
from common.get_ip import GetIp
from common.read_config import ReadConfig
class GetData:
    '''专门来读取路径的值'''

    base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]   #G:\python3_code\sublime_text03\14SoftwareTest\APITest\qcd_ApiTest
    # 测试用例路径
    case_path = os.path.join(base_path,'test_case','test_case.xlsx')
    # 测试报告路径
    report_path = os.path.join(base_path,'test_result','report','test_api.html')

    # 配置文件路径
    config_path = os.path.join(base_path,'conf','webservice.conf')

    # 日志文件路径
    log_path = os.path.join(base_path,'test_result','log','test_log.txt')

    # 未注册手机号
    no_reg_tel = pd.read_excel(case_path,sheet_name='init').ix[0,1]
    # 未用过的手机号
    reg_name = GetRegName.get_reg_name()

    #获取ip
    ip = GetIp.get_ip()
    # 接口url地址
    sms_service_url = ReadConfig.read_config(case_config_path,'URL','sms_service')
    finance_user_info_url = ReadConfig.read_config(config_path,'URL','finance_user_info')
if __name__=='__main__':
    print(GetData.no_reg_tel)
    print(GetData.case_path)
    print(GetData.config_path)