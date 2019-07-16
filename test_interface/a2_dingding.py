# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 11:04 AM
# @Author  : Emmy

import requests
import unittest
import json,time,datetime

import sys
from dingtalkchatbot.chatbot import DingtalkChatbot

sys.path.append("..")
from test_interface.a0_homeproGet_test import *
from test_interface.a1_customerOverview_test import *
from common.commonData import *


class a2_dingding(unittest.TestCase):
    def test_z1_homeproGet(self):

        """调用钉钉机器人通知"""
        # WebHook地址
        #测试
        # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=94957547970c3816d2db8d2ea7aea8fbf6eeac0ed7341c611e5d5d0b085762c8'
        #钉钉
        #webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e1cf8bea4453ea92a5af082d92950ff451d76ae087df7e301ce2cbc7bcc003de'
        # 初始化机器人小精灵
        xiaoding = DingtalkChatbot(webhook)
        # Text消息@所有人
        print(commonData.flag)

        HEADERS = {"Content-Type": "application/json;charset=utf-8"}

        String_textMsg = {
            "msgtype": "text",
            "at": {
                "isAtAll": "true"
            },
            "text": {
                "content": xiaoding.send_text
            }
        }
        String_textMsg = json.dumps(String_textMsg)


        res = requests.post(url=webhook, data=json.dumps(String_textMsg), headers=HEADERS)

        print(res.text+"ces")

        # if (commonData.flag == True  and  commonData.allUsers != 0):
        #     xiaoding.send_text(msg='😊\n 环境：线上 \n 首页今日有数据显示\n 客户信息概览有数据显示', is_at_all=True)
        #     # xiaoding.send_link(title='😊线上首页今日有数据显示', text='真的有数据，请点击链接登录查看',
        #     #                    message_url='https://icem-geek-fix.jiekecloud.cn/manager/#/login", pic_url="http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4eb0bab1d3c94565a03d41d08ef845c3.jpg')
        #
        #
        # else:
        #     xiaoding.send_text(msg='💔\n 环境：线上 \n 首页今日无数据显示\n 客户信息概览无数据显示', is_at_all=True)
        #
        #     # xiaoding.send_link(title='💔线上环境首页今日无数据/(ㄒoㄒ)/~~', text='不信你就亲自登录查看',
        #     #                    message_url='https://icem-geek-fix.jiekecloud.cn/manager/#/login", pic_url="http://geek-icem.oss-cn-beijing.aliyuncs.com/release/1000/material/4eb0bab1d3c94565a03d41d08ef845c3.jpg')








if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(a0_homeproGet_test())
    suite.addTest(a1_customerOverview_test())
    suite.addTest(a2_dingding())
