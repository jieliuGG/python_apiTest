# —— coding :utf-8 ——
# @time:    2020/9/23 21:12
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    handle_mysql.py
import pymysql
from common.file_dir import case_config_path
from common.read_config import ReadConfig
class HandleMysql:
    @staticmethod
    def handle_mysql(sql,state="all"):
        #1. 连接数据库
        db_config = eval(ReadConfig().read_config(case_config_path,'DB','db_config'))
        #利用这个类从配置文件中读取info
        conn = pymysql.connect(**db_config)
        #2. 获取游标
        cursor = conn.cursor()
        #3. 定义要执行的SQL语句
        #4. 执行SQL语句
        cursor.execute(sql)
        #5. 获取结果
        if state=="1":
            cursor.fetchone()
        else:
            cursor.fetchall()
        #6. 关闭游标
        cursor.close()
        #7. 关闭数据库连接
        conn.close()
        return db_config
if __name__ == '__main__':
    sql = 'select * from member where MobielPhone like "150%"'
    res = HandleMysql().handle_mysql(sql)
    print(res[0][0])

