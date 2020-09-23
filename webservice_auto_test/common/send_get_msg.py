# —— coding :utf-8 ——
# @time:    2020/9/15 0:47
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    send_get_msg.py
from common.get_data import GetData
from common.base_request import BaseRequest
from common.handle_mysql import HandleMysql
class SendGetMsg:
    @staticmethod
    def send_get_msg(mobile): # 发送并获取验证码
        # 数据是固定的，只需更改手机号
        data = {'client_ip':getattr(GetData,'ip'),'tmpl_ip':'1','mobile':mobile}

        client = BaseRequest.base_request(getattr(GetData,'sms_service_url'))
        client.service.SendMCode(data)

        # 查询验证码
        query_sql = 'select Fverify_code from t_mvcode_info_{0} where Fmobile_no={1}'.format(mobile[-3],mobile)
        db_name = 'sms_db_{0}'.format(mobile[-2])
        res = HandleMysql.handle_mysql(query_sql,db_name)
        return res[0]

if __name__ == '__main__':
    print(SendGetMsg.send_get_msg('15096090552'))