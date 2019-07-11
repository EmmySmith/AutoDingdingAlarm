#coding=utf-8

import time
import os
import sys,importlib
importlib.reload(sys)
# sys.setdefaultencoding('utf8')
import unittest
from HTMLTestRunner import HTMLTestRunner     #引入HTMLTestRunner模板
# from HTMLTestReportCN import HTMLTestRunner
# from HTMLTestRunner_bingtu import HTMLTestRunner
# from HTMLTestRunner_new import HTMLTestRunner
# from sendEmail.sendEmail_new import SendMail
from common.replaceFile import *




def testRun(file):
    #根据接收到的env参数来替换相应的环境配置和数据库配置

    test_dir = "./test_interface/CDP/dataDashboard/"
    file = unittest.defaultTestLoader.discover(test_dir, pattern='homeproGet_test.py')  # 匹配结尾为test的py文件


testRun()