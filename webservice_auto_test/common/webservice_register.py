# —— coding :utf-8 ——
# @time:    2020/9/15 0:48
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    webservice_register.py
from common.base_request import BaseRequest
from common.get_data import GetData
from common.send_get_msg import SendGetMsg


class WebServiceRegister:
    @staticmethod
    def webservice_register(data): # 这里传输的data只需要给定user_id以及密码mobile即可chanel_id
        client = BaseRequest.base_request(getattr(GetData,'finance_user_info_url'))
        # 发送并获取手机号
        verify_code =SendGetMsg.send_get_msg(data['mobile'])

        # 再次拼接
        res = client.service.userRegister(data)

        # 返回结果
        return res

if __name__ == '__main__':
    data = {'user_id':'summer06','channel_id':'3','pwd':'123456','mobile':'15096085200'}
    res = WebServiceRegister.webservice_register(data)
    print('注册返回的结果是:{0}'.format(res))