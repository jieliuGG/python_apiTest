# —— coding :utf-8 ——
# @time:    2020/9/15 0:44
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    handle_regx.py
from  common.get_data import GetData
import re

# s = '{"mobilephone":"${normal_tel}","pwd":"123456"}'

class HandleRegx:
    @staticmethod
    def handle_Reg(self,file_name):
        while re.search('\$\{(.*?)]\}',s):
            key = re.search('\$\{(.*?)]\}',s).group(0)
            value = re.search('\$\{(.*?)]\}',s).group(1)
            s = s.replace(key,str(getattr(GetData,value)))
            if value=='no_reg_tel':
                setattr(GetData,value,getattr(GetData,value)+1)
                self.update_tel(file_name,getattr(GetData,value))
        return s
    def update_tel(self,file_name,tel):
        pass
if __name__ == '__main__':
    s = '{"mobilephone":"${admin_tel}","pwd":"${pwd}"'
    res = Regx.handle_Reg(s)
    print(res)