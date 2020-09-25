# —— coding :utf-8 ——
# @time:    2020/9/23 21:14
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    read_config.py
import configparser # 配置解析器
class ReadConfig:
    @staticmethod
    def read_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf[section][option]
if __name__ == '__main__':
    from common.file_dir import case_config_path
    print(ReadConfig().read_config(case_config_path,'MODE','mode'))
