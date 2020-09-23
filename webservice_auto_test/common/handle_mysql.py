# —— coding :utf-8 ——
# @time:    2020/9/15 0:44
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    handle_mysql.py

from common.read_config import ReadConfig
# 导入pymysql模块
import pymysql
from common.get_data import GetData
class HandleMysql:

    @staticmethod
    def handle_mysql(query_sql, db_name,flag=None,state=1):
        # 1.连接database
        db_config = eval(ReadConfig().read_config(getattr(GetData,'config_path), 'DB', 'db_config'))
        # 利用这个类从配置文件中读取 info
        db_config['database'] =  db_name
        conn = pymysql.connect(**db_config)
        # 2.获取游标
        cursor = conn.cursor()
        # 3.定义要执行的SQL语句
        # 4.执行SQL语句
        cursor.execute(sql)
        # 5. 获取结果
        if state == 1:
            res = cursor.fetchone()  # 元组 针对一条
        else:
            res = cursor.fetchall()  # 列表，针对多条，列表嵌套元组
        # 5.关闭光标对象
        cursor.close()
        # 6.关闭数据库连接
        conn.close()
        return res


if __name__ == '__main__':
    sql = 'select * from member where MobilePhone like"138%"'
    res = HandleMysql().handle_mysql(sql)
    print(res[0][0])
