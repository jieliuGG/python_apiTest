# —— coding :utf-8 ——
# @time:    2020/9/23 21:20
# @IDE:     py_ApiTestFramework_V1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    test_loan.py
import unittest
from common.handle_excel import HandleExcel
from common.get_data import GetData
from common.http_requests import HttpRequest
from common.file_dir import *
from ddt import ddt, data  # 列表嵌套列表：索引方式读取；列表嵌套字典：关键字方式读取
from common.my_logger import MyLogger
from common.handle_mysql import HandleMysql
from common.get_data import GetData

logger = MyLogger()
test_data = HandleExcel.get_data(test_data_path)  # 执行登录用例


@ddt
class TestInvest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_invest(self, item):
        global check_sql_result
        logger.info('开始执行的用例{0}:{1}'.format(item['test_id'], item['title']))
        # 请求之前完成loan_id替换
        if item['data'].find('${loan_id}')  !=-1:
            if getattr(GetData,'loan_id') ==None:   # 还没有通过反射把值改了
                sql = 'select max(Id) from loan where MemberID={0}'.format(getattr(GetData, 'loan_admin_tel')) # memberID投资充值ID
                loan_id = HandleMysql().handle_mysql(sql)[0][0]
                item['data'] = item['data'].replace('${loan_id}', str(loan_id))
                setattr(GetData, 'loan_id', loan_id)  # 利用这个反射存储结果
                logger.info(loan_id)
            else:   # 通过反射已经设置了值
                logger.info(getattr(GetData, 'loan_id'))
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData, 'loan_id')))


        # 登录
        logger.info('获取到的请求数据是:{0}'.format(item['data']))
        if item['check_sql'] != None:
            logger.info('数据库检验{0}'.format(item['title']))
            sql = eval(item['check_sql']['sql'])
            Before_Amount = HandleMysql().handle_mysql(sql, 1)[0]
            logger.info('用例:{0}请求之前余额:{1}'.format(item['title'], Before_Amount))
            logger.info('开始http接口请求...')
            res = HttpRequest.http_request(item['url'],
                                           eval(item['data']),
                                           item['http_method'],
                                           getattr(GetData, 'Cookie')
                                           )
            logger.info('完成http请求')
            After_Amount = HandleMysql().handle_mysql(sql, 1)[0]
            logger.info('用例:{0}请求之后余额:{1}'.format(item['title'], After_Amount))
            # 检查结果
            if eval(item['data']['amount']) == abs(After_Amount - Before_Amount):
                logger.info('数据库余额检验通过')
                logger.info('数据库检查通过')
                HandleExcel.write_back(test_data_path, item['sheet_name'], item['test_id'] + 1,
                               10, check_sql_result)
            else:
                logger.info('数据库余额检验不通过')
                check_sql_result = logger.info('数据库检查不通过')
            # 重新改写 HandleExcel write_back方法
            HandleExcel.write_back(test_data_path, item['sheet_name'], item['test_id'] + 1,
                               10, check_sql_result)

        else:
            logger.info('此条用例不需数据库校验:{0}'.format(item['title']))
            res = HttpRequest.http_request(item['url'],
                                       eval(item['data']),
                                       item['http_method'],
                                   getattr(GetData, 'Cookie')
                                   )

        if res.cookies:
            setattr(GetData, 'Cookie', res.cookies)
        try:
            self.assertEqual(item['excepted'], res.json()['code'])
            TestResult = 'PASS'  # 成功的
        except Exception as  e:
            TestResult = 'failed'  # 失败的
            logger.info("执行用例出错:{0}".format(e))
        finally:
            HandleExcel.write_back(test_data_path, item['sheet_name'], item['test_id'] + 1, 8,str(res.json()))
            HandleExcel.write_back(test_data_path, item['sheet_name'], item['test_id'] + 1, 9, str(res.json()))
            logger.error("获取到的结果为:{0}".format(res.json()))
