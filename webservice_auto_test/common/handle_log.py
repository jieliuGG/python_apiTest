# —— coding :utf-8 ——
# @time:    2020/9/15 0:46
# @IDE:     webservice_auto_test
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    handle_log.py

import logging


class MyLog:
    def mylog(self, msg, level):
        # 1. 定义一个日志收集器 logger
        logger = logging.getLogger('my_logger')

        # 2. 设置级别
        logger.setLevel('DEBUG')

        # 3. 设置输出格式
        formater = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(massage)s')

        # 4. 创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formater)  # 输出格式

        fh = logging.FileHandler('logging_review.txt', encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formater)

        # 5. 两者对接----指定输出渠道
        logger.addHandler(ch)
        logger.addHandler(fh)

        # 6. 收集日志
        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'IFNO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)
        # 关闭渠道
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog(msg, 'DEBUG')

    def info(self, msg):
        self.mylog(msg, 'INGO')

    def warning(self, msg):
        self.mylog(msg, 'WARNING')

    def error(self, msg):
        self.mylog(msg, 'ERROR')

    def critical(self, msg):
        self.mylog(msg, 'CRITICAL')


if __name__ == '__main__':
    pass
   #my_logger = MyLog('aaaa','ERROR')
