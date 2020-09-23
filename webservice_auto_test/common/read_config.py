# —— coding :utf-8 ——
# @time:    2020/9/15 0:47
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    read_config.py
import configparser
class ReadConfig:
    @staticmethod
    def read_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf[section][option]
