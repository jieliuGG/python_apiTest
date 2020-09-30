# —— coding :utf-8 ——
# @time:    2020/9/23 15:55
# @IDE:     Test_HttprequestDemo
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    logging.py
import logging

# 1. 定义一个日志收集器 logger
logger = logging.getLogger('logging_review')

# 2. 设置级别
logger.setLevel('DEBUG')

# 3. 设置输出格式
formater = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(massage)s')

# 4. 创建一个输出渠道
ch = logging.StreamHandler()
ch.setLevel('ERROR')
ch.setFormatter(formater)

fh = logging.FileHandler('logging_review.txt', encoding='utf-8')
fh.setLevel('DEBUG')
fh.setFormatter(formater)

# 5. 两者对接
logger.addHandler(ch)
logger.addHandler(fh)

# 6. 收集日志
logger.debug('i am debug profile')
logger.error('aaaaa')
