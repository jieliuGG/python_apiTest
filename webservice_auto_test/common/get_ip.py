# —— coding :utf-8 ——
# @time:    2020/9/15 0:45
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    get_ip.py
import socket
class GetIp:
    '''获取本机ip地址'''
    @staticmethod
    def get_ip():
        # 获取本机计算机名称
        hostname = socket.gethostname()
        # 获取本机ip
        ip = socket.gethostbyname(hostname)
        return ip

if __name__ == '__main__':
    print(GetIp.get_ip())