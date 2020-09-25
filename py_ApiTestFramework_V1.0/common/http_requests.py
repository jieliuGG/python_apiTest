# —— coding :utf-8 ——
# @time:    2020/9/23 21:13
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    http_requests.py
import requests
from common.my_logger import MyLogger
logger = MyLogger()
class HttpRequest:
    def http_request(self,url,data,method,cookies=None):
        global res
        try:
            if method.upper() =="GET":
                res = requests.get(url,data,cookies=cookies)
            elif method.upper()=="POST":
                res = requests.post(url,data,cookies=cookies)
            else:
                logger.info("输入请求方式不对")
        except Exception as e:
            logger.error("请求方式报错：{}".format(e))
            raise e
        return res
if __name__ == '__main__':
    # 注册
    register_url = 'http://169.254.160.239:8080/futureloan/mvc/api/member/register'
    register_data = '{"mobilephone": "185932987970", "pwd": "123456", "regname": "jsonLiu"}'

    # 登录
    login_url = 'http://169.254.160.239:8080/futureloan/mvc/api/member/login'
    login_data = '{"mobilephone": "18593298797", "pwd": "123456"}'

    # 充值
    recharge_url = 'http://169.254.160.239:8080/futureloan/mvc/api/member/recharge'
    recharge_data = '{"mobilephone": "18593298797", "amount": "1000"}'

    login_res = HttpRequest().http_request(login_url, login_data, 'get')
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, 'post')
    print('充值结果是:{}'.format(recharge_res.json()))
