# —— coding :utf-8 ——
# @time:    2020/9/15 13:43
# @IDE:     Test_HttprequestDemo
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    fileUp.py
# pip install pypiwin32
import win32gui
import win32con

# 谷歌浏览器
def upload_file(filepath):
    dialog = win32gui.FindWindow('#32770', '打开')  # 一级
    # 二级窗口
    ComBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComBoxEx32', None)
    # 三级窗口
    ComboBox = win32gui.FindWindowEx(ComBoxEx32, 0, 'ComboBox', None)
    # 四级窗口
    edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&0)")

    # 操作
    # 输入文件地址
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
    # 打开文件按钮
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
