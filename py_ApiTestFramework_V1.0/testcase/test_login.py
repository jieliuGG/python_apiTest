# —— coding :utf-8 ——
# @time:    2020/9/23 21:17
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_login.py
import unittest
from common.handle_excel import HandleExcel
from common.get_data import GetData
from common.http_requests import HttpRequest
from common.file_dir import *
from ddt import ddt, data  # 列表嵌套列表：索引方式读取；列表嵌套字典：关键字方式读取

test_data = HandleExcel.get_data(test_data_path,'login')  # 执行登录用例


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_Login(self, item):
        # 登录
        global TestResult
        login_url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        login_data = '{"mobilephone": "18593298797", "pwd": "123456"}'
        res = HttpRequest.http_request(item['url'], eval(item['data']), item['http_method'],
                                       getattr(GetData, 'Cookie'))
        try:
            self.assertEqual(item['excepted'], res.json()['code'])
            TestResult = 'PASS'  # 成功的
        except Exception as  e:
            TestResult = 'failed'  # 失败的
            print("执行用例出错:{0}".format(e))
        finally:
            HandleExcel.write_back(test_data_path,item['sheet_name'], item['test_id']+1, str(res.json()),TestResult)
            print("获取到的结果为:{0}".format(res.json()))
