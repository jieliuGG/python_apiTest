# —— coding :utf-8 ——
# @time:    2020/9/23 21:12
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    handle_regx.py
from common.get_data import GetData
# s = {"mobilephone":"${normal_tel}","pwd":"${pwd}"}
import re
class Regx:
    @staticmethod
    def handle_regx(s):
        while re.search('\$\{(.*?)]\}',s):
            key = re.search('\$\{(.*?)]\}',s).group(0)
            value = re.search('\$\{(.*?)]\}',s).group(1)
            s = s.replace(key,str(getattr(GetData,value)))
            return s
if __name__ == '__main__':
    s = '{"mobilephone": "${admin_tel}", "pwd": "${pwd}"}'
    res = Regx().handle_regx(s)
    print(res)