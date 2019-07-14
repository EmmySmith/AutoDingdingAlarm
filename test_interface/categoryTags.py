# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 11:20 AM
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


class test_c_customerOverview(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/portrait/category/tags"
        print("----------开始测试----------")

    def test_c_categoryTags(self):
        """人群画像"""
        self.url = self.host + self.path

        data = {
            "crowdId": 534,
            "categoryId": 1
        }
        print(self.url)
        print(data)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.allUsers = json.loads(response.text)["body"]["allUsers"]
        print(commonData.allUsers)



