# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 7:16 PM
# @Author  : Emmy

# !/usr/bin/python
# coding=utf-8
import requests
import unittest
import json, time, datetime, threading
from dateutil.parser import parse

import sys
from dingtalkchatbot.chatbot import DingtalkChatbot

sys.path.append("..")
from common.public import *
from common.commonData import *
from common.login import *
from mysqlHandle.common_mysql import *



class test_a1_homeproGet(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.sql1 = 'select count(*) from t_crowd t where t.flag = "NO" and t.is_show="YES" and t.type = "USER_DEFINED" and t.crowd_number=0'
        # self.sql2 = 'select crowd_id from t_crowd t where t.flag = "NO" and t.is_show="YES" and t.type = "USER_DEFINED" and t.crowd_number=0'
        self.dbname = "geek_icem_crowd"


        self.path1 = "/api/icem-report/home/pro/get"
        self.path2 = "/api/icem-report/customer/overview"
        print("----------开始测试----------")

    def test_a1_homeproGet(self):
        """客户生命周期"""
        self.url = self.host + self.path1

        data = {
            "startDate": (datetime.datetime.now() + datetime.timedelta(days=-8)).strftime('%Y-%m-%d'),
            "endDate": (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
        }

        print(self.url)
        print(data)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.flag = json.loads(response.text)["body"]["underDTOList"][0]["active"]["flag"]
        print(commonData.flag)


    def test_a2_customerOverview(self):
        """客户信息概览"""
        self.url = self.host + self.path2

        data = {

        }
        print(self.url)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.allUsers = json.loads(response.text)["body"]["allUsers"]
        print(commonData.allUsers)
        return commonData.allUsers






    def test_b_dingding(self):
        """调用钉钉机器人通知"""

        d2 = parse(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        print('当前日期：'+str(d2))
        d4 = parse('2019-07-15 00:00:00')
        print('开始时间：'+str(d4))
        chazhi = (d2 - d4).days
        print(chazhi)
        print('截止今天总监控'+str(chazhi) +'次')

        counts = (DB_api(self.dbname).get_values(self.sql1))
        # crowd_id  = (DB_api(self.dbname).get_values(self.sql2))
        print(counts)




        # WebHook地址
        # 测试
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=94957547970c3816d2db8d2ea7aea8fbf6eeac0ed7341c611e5d5d0b085762c8'
        # 测试内部群
        # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e1cf8bea4453ea92a5af082d92950ff451d76ae087df7e301ce2cbc7bcc003de'
        # 数据组群
        # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a68da51f8604fa5672eac4f05a67a372d393facb6d05f6e4e9dc2ccca619b4ca'
        # 林清轩项目组
        # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=0e8af2347f4aa16039735fa738114c8305445342b546547f054931611750c7a1'
        # 初始化机器人小精灵
        xiaoding = DingtalkChatbot(webhook)

        # Text消息@所有人

        if (commonData.flag == True and commonData.allUsers != 0):
            xiaoding.send_text(msg='😄\n 环境：线上 \n 首页今日有数据显示\n 客户信息概览有数据显示\n 标签中圈选人数有'+str(counts)+'个人群为0 \n\n 截止今日共监控'+str(chazhi) +'次', is_at_all=True)

        elif (commonData.flag == False  and commonData.allUsers != 0):
            xiaoding.send_text(msg='😢\n 环境：线上 \n 首页今日无数据显示\n 客户信息概览有数据显示\n 标签中圈选人数有'+str(counts)+'个人群为0 \n\n 截止今日共监控'+str(chazhi) +'次', is_at_all=True)

        elif (commonData.flag == True  and commonData.allUsers == 0):
            xiaoding.send_text(msg='😢\n 环境：线上 \n 首页今日有数据显示\n 客户信息概览有数据显示\n 标签中圈选人数有'+str(counts)+'个人群为0 \n\n 截止今日共监控'+str(chazhi) +'次', is_at_all=True)

        else:
            xiaoding.send_text(msg='💔\n 环境：线上 \n 首页今日无数据显示\n 客户信息概览有数据显示\n 标签中圈选人数有'+str(counts)+'个人群为0 \n\n 截止今日共监控'+str(chazhi) +'次', is_at_all=True)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
