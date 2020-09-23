# —— coding :utf-8 ——
# @time:    2020/9/15 0:47
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_register.py
import unittest

import ddt

from common.handle_excel import HandleExcel
from common.get_data import GetData
from common.handle_log import MyLog
from common.webservice_register import WebServiceRegister, data

test_data = HandleExcel().handle_excel(getattr(GetData, 'case_path'), 'register')
my_logger = MyLog()


@ddt
class TestRegister(unittest.testCase):
    def setUP(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_register(self,item):
        my_logger.info('目前正在执行的第{}条测试用例：{}'.format(item['case_id'], item['title']))
        my_logger.info('开始执行测试用例')
        res = WebServiceRegister.webservice_register(eval(item['param']))
        my_logger.info('完成测试用例执行')
        try:
            self.assertEqual(item['expected'], int(res['retCode']))
            TestReslt = 'PASS'
        except AssertionError as  e:
            TestReslt = 'FAILED'
            my_logger.error('断言出错:{}'.format(e))
            raise  e
        finally:# 最终写回结果
            HandleExcel.write_back(getattr(GetData,'case_path'),'register',item['case_id']+1,5,str(res))
            HandleExcel.write_back(getattr(GetData,'case_path'),'register',item['case_id']+1,6,TestReslt)