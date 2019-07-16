# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 11:07 AM
# @Author  : Emmy

import requests
import unittest
import json,time,datetime,threading

import sys
from dingtalkchatbot.chatbot import DingtalkChatbot

sys.path.append("..")
from common.public import *
from common.commonData import *
from common.login import *


class a1_customerOverview_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/customer/overview"
        print("----------开始测试----------")

    def test_a2_customerOverview(self):
        """客户信息概览"""
        self.url = self.host + self.path

        data = {

        }
        print(self.url)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.allUsers = json.loads(response.text)["body"]["allUsers"]
        print(commonData.allUsers)
        return commonData.allUsers

if __name__ == '__main__':
    unittest.main()


