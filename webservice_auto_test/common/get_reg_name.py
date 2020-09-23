# —— coding :utf-8 ——
# @time:    2020/9/15 0:45
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    get_reg_name.py
import random
class GetRegName:
    '''生成随机用户名，防止名字重复，也不需要做参数化'''

    @staticmethod
    def get_reg_name():
        name_prefix = 'wbsat_'
        name_stem = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',3))
        name_suffix = random.randint(1,10000)
        return name_prefix+name_stem+str(name_suffix)
if __name__ == '__main__':
    print(GetRegName.get_reg_name())