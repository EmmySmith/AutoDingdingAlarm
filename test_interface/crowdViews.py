# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 1:11 PM
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


class test_a3_crowdViews(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-report/crowd/charts/views"
        print("----------开始测试----------")

    def test_a3_crowdViews(self):
        """人群绩效"""
        self.url = self.host + self.path

        data = {
            "crowdInstId": 528,
            "startTime": "2018-08-01",
            "endTime": "2019-07-31"
                }
        print(self.url)
        print(data)
        response = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        print(response.text)
        commonData.value = json.loads(response.text)["body"]["averagePrice"][0]["nameValues"][0]["value"]
        print(commonData.value)

if __name__ == '__main__':
    unittest.main()




