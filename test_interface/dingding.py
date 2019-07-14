# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 11:04 AM
# @Author  : Emmy

import requests
import unittest
import json,time,datetime

import sys
from dingtalkchatbot.chatbot import DingtalkChatbot

sys.path.append("..")
from common.public import *
from common.commonData import *
from common.login import *


class CDP_Interface(unittest.TestCase):

    def test_b(self):
        """调用钉钉机器人通知"""
        # WebHook地址
        #测试
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=94957547970c3816d2db8d2ea7aea8fbf6eeac0ed7341c611e5d5d0b085762c8'
        #钉钉
        #webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e1cf8bea4453ea92a5af082d92950ff451d76ae087df7e301ce2cbc7bcc003de'
        # 初始化机器人小精灵
        xiaoding = DingtalkChatbot(webhook)
        # Text消息@所有人
        if commonData.flag == True:
            xiaoding.send_text(msg='😊线上环境今日首页有数据显示', is_at_all=True)
            # xiaoding.send_link(title='😊线上首页今日有数据显示', text='真的有数据，请点击链接登录查看',
            #                    message_url='https://icem-geek-fix.jiekecloud.cn/manager/#/login", pic_url="http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4eb0bab1d3c94565a03d41d08ef845c3.jpg')


        else:
            xiaoding.send_text(msg='💔线上环境今日首页无数据显示', is_at_all=True)

            # xiaoding.send_link(title='💔线上环境首页今日无数据/(ㄒoㄒ)/~~', text='不信你就亲自登录查看',
            #                    message_url='https://icem-geek-fix.jiekecloud.cn/manager/#/login", pic_url="http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4eb0bab1d3c94565a03d41d08ef845c3.jpg')

    def tearDown(self):
        pass






if __name__ == "__main__":
    unittest.main()