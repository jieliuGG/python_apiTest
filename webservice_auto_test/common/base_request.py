# —— coding :utf-8 ——
# @time:    2020/9/15 0:44
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    base_request.py
from suds.client import Client
class BaseRequest:
    '''发起一个suds库client请求'''
    @staticmethod
    def base_request():
        client = Client(url)
        return client