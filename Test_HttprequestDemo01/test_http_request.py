# —— coding :utf-8 ——
# @time:    2020/9/14 12:35
# @IDE:     Test_HttprequestDemo
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_http_request.py
import unittest
from http_requests import HttpRequest
from get_data import GetDate
test_data = []
class TestHttpRequest(unittest.TestCase):
    def setUP(self):
        self.login_url = 'http://119.23.241.154.8080/futureloan/mvc/api/member/login'
        self.recharge_url = 'http://119.23.241.154.8080/futureloan/mvc/api/member/recharge'
    def test_login_normal(self):
        '''正常登录'''
        data = {"mobilephone": "18593298080", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, data, 'get')
        if res.cookies:
            setattr(GetDate,'Cookie')
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as  e:
            print("test_login_normal's error is {}".format(e))
            raise e
    def test_login_Nopwd(self):
        '''不输入密码'''
        data = {"mobilephone": "18593298080", "pwd": ""}
        res = HttpRequest().http_request(self.login_url, data, 'get')
        try:
            self.assertEqual('20103', res.json()['code'])
        except AssertionError as  e:
            print("test_login_Nopwd's error is {}".format(e))
            raise e
    def test_login_noID(self):
        '''不输入账号'''
        data = {"mobilephone": "", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, data, 'get')
        try:
            self.assertEqual('20103', res.json()['code'])
        except AssertionError as  e:
            print("test_login_noID's error is {}".format(e))
            raise e
    def test_login_wrong_pwd(self):
        '''输入错误的密码'''
        data = {"mobilephone": "18593298080", "pwd": "12345678"}
        res = HttpRequest().http_request(self.login_url, data, 'get')
        try:
            self.assertEqual('20111', res.json()['code'])
        except AssertionError as  e:
            print("test_login_wrong_pwd's error is {}".format(e))
            raise e
    def test_login_wrong_ID(self):
        '''输入错误的账号'''
        data = {"mobilephone": "185932980", "pwd": "123456"}
        res = HttpRequest().http_request(self.login_url, data, 'get')
        try:
            self.assertEqual('20111', res.json()['code'])
        except AssertionError as  e:
            print("test_login_wrong_ID's error is {}".format(e))


    def test_recharge_normal(self):
        '''正常充值'''
        data = {"mobilephone": "18593298080", "amount": "1100"}
        res = HttpRequest().http_request(self.recharge_url, data, 'post',cookie=self.cookies)
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print("test_recharge_normal's error is {}".format(e))
            raise e
    def test_recharge_noID(self):
        '''不输入账号'''
        data = {"mobilephone": "", "amount": "1100"}
        res = HttpRequest().http_request(self.recharge_url, data, 'post', cookie=self.cookies)
        try:
            self.assertEqual('10001', res.json()['code'])
        except AssertionError as e:
            print("test_recharge_normal's error is {}".format(e))
            raise e
    def test_recharge_noMoney(self):
        '''不输入金额'''
        data = {"mobilephone": "18593298080", "amount": ""}
        res = HttpRequest().http_request(self.recharge_url, data, 'post',cookie=self.cookies)
        try:
            self.assertEqual('20115', res.json()['code'])
        except AssertionError as e:
            print("test_recharge_noMoney's error is {}".format(e))
            raise e
    def test_recharge_negative(self):
        '''充值为负数'''
        data = {"mobilephone": "18593298080", "amount": "-1100"}
        res = HttpRequest().http_request(self.recharge_url, data, 'post', cookie=self.cookies)
        try:
            self.assertEqual('20117', res.json()['code'])
        except AssertionError as e:
            print("test_recharge_noMoney's error is {}".format(e))
            raise e
    def teaDown(self):
        pass
class TestMath(unittest.TestCase):
    def test_add(self):
        print('a+b=',100)
    def test_sub(self):
        print('a-b=',80)
