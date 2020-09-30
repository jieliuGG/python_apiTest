# —— coding :utf-8 ——
# @time:    2020/9/14 12:35
# @IDE:     Test_HttprequestDemo
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    http_requests.py
import requests


class HttpRequest:
    '''利用requests封装get和post请求'''


    def http_request(self, url, data, method, cookie=None):
        if method.lower() == 'GET':
            res = requests.get(url, data, cookies=cookie, verify=False)  #将https检查设置为False
        else:
            res = requests.post(url,data,cookies=cookie,verify=False)
        return res
if __name__ == '__main__':
    # 登录，同时支持post和get请求
    url = 'http://119.23.241.154.8080/futureloan/mvc/api/member/login'
    data = {"mobilephone":"18593298080","pwd":"123456"}
    res = HttpRequest().http_request(url,data,'get')
