# —— coding :utf-8 ——
# @time:    2020/9/23 21:12
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    get_data.py
import pandas as pd
from common.read_config import ReadConfig
from common import file_dir
class GetData:
    Cookie = None
    loan_id = None
    # 检查金额数量
    check_id = eval(ReadConfig().read_config(file_dir.case_config_path,'CHECKLEAVEAMOUNT','check_list'))
    # 未注册手机号
    No_register = pd.read_excel(file_dir.test_data_path,sheet_name='init').iloc[0,0]  # iloc[行,列]
    # 正常手机号
    normal_tel = pd.read_excel(file_dir.test_data_path,sheet_name='init').iloc[1,0]
    #管理账户加标
    admin_tel = pd.read_excel(file_dir.test_data_path,sheet_name='init').iloc[2,0]
    # 借钱用户id
    loan_member_id = pd.read_excel(file_dir.test_data_path,sheet_name='init').iloc[3,0]
    # 充值投资账户id
    memberID = pd.read_excel(file_dir.test_data_path,sheet_name='init').iloc[4,0]

# setattr(GetCookie,'Cookie','123456') # 设置属性值
# print(hasattr(GetCookie,'Cookie')) # 判断是否有这个属性
# delattr(GetCookie,'Cookie') #删除这个属性
# print(getattr(GetCookie,'Cookie')) # 获取属性值
# getattr(object,name) //setattr(x,y,z)     x.y = z
if __name__ == '__main__':
    print(GetData().memberID)
