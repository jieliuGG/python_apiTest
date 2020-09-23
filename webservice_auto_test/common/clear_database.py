# —— coding :utf-8 ——
# @time:    2020/9/15 0:45
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    clear_database.py
from common.handle_mysql import HandleMysql
class ClearDataBase:
    @staticmethod
    def clear_alone_base():
        # 清空单独的库
        db_table={'ct_db':['t_account','t_user_info'],
                  'sms_db':['t_ip_limeit','t_mobile_limit'],
                  'user_db':['t_user_auto_info','t_user_info']
                  }
        for db in db_table:
            for table in db_table[db]:
                print('正在清空{}库{}表'.format(db,table))
                query_sql = 'delete from {}'.format(table)
                HandleMysql.handle_mysql(query_sql,db,'update')
                print('清空完毕')

    @staticmethod
    def clear_most_base():
        '''清空分表分库'''
        db_names ={'sms_db':['t_mvcode_info','t_send_info'],
                   'user_db':['t_bind_card','t_user_risk']
                   }
        for db in db_names:
            for num in range(100):
                if num<10:
                    for no in range(10):
                        pass

