# —— coding :utf-8 ——
# @time:    2020/9/14 13:36
# @IDE:     Test_HttprequestDemo
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_suite.py

import unittest
from test_http_request import TestHttpRequest  # 模块名
import test_http_request
import HTMLTestRunner

suite = unittest.TestSuite()
# 加载方式1：
suite.addTest(TestHttpRequest("test_login_normal"))
suite.addTest(TestHttpRequest("test_login_Nopwd"))
# 加载方式2：
# 通过loader方式加载用例
loader = unittest.TestLoader()
# 一次性加载某个测试类的所有测试用例
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
# 一次性加载某个模块下所有测试用例，模块下有多个测试类
suite.addTest(loader.loadTestsFromModule(test_http_request))

# 执行用例
with open('test_summer.html', 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title=None, description=None)
    runner.run(suite)

# runner = unittest.TextTestRunner()
# runner.run()
