1)登录url = 'http://119.23.241.154.8080/futureloan/mvc/api/member/login'
2)充值url: url =  'http://119.23.241.154.8080/futureloan/mvc/api/member/recharge'
3)针对登录接口写四个用例：正常登录、不输入密码、不输入账号、输入错误的密码
充值接口：正常充值、不输入账号、不输入金额、输入错误的金额负数
4） 实现用例加载并执行
5）生成html类型测试报告

## 1.
cookie 处理：
    法1：全局变量： 关联性较强
    法2：反射
## 2.   
第二条用例请求用到第一条用例返回结果某些值解决方案：
1. 全局变量cookie
2. 写到setUP里，重新请求第一条用例
3. 反射
## 3.
读取数据方式：
1.一次性读取所有数据，对内存要求高点
2. 需要用到时候读取所有数据，对磁盘读写要求高点

## 4.
ddt:ddt+unittest 数据处理第三方库
装饰器：在函数运行之前运行

## 5. 配置文件
properties  config ini log4j
section option value  

## 6. 静态方法、类方法、实例方法
静态方法、类方法：通过类名.方法名调用，也可以通过实例调用
实例方法： 必须要创建实例调用 类名()

类方法cls、静态方法：不能调用类属性值
实例方法self：只有实例方法才可以调用类属性值 self





Test_HttprequestDemo第一次上传失误，重新上传，更名为Test_HttprequestDemo02