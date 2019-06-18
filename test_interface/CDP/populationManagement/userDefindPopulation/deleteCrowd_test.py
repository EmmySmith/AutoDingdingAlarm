#!/usr/bin/python
# coding=utf-8
import requests
import unittest
import json
from common.public import *
from mysqlHandle.common_mysql import *

class ICEM_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.headers = headers
        self.host = host
        self.path = "/api/icem-crowd/crowd/copy"
        self.sql = "SELECT id FROM t_crowd ORDER BY id DESC LIMIT 1;"
        self.dbname = "geek_icem_crowd"
        print("----------开始测试----------")


    #人群复制接口
    def test_crowdCopy(self):
        self.url = self.host + self.path
        self.crowd_id = DB_ICEM_proc(self.dbname).get_vslues(self.sql)
        print(self.crowd_id)
        data = {"id":self.crowd_id}
        print(data)
        print(self.url)
        response = requests.post(url=self.url,data= json.dumps(data), headers=self.headers)
        print (response.text)
        assert response.json()['error'] == 0


    def tearDown(self):
        pass

if __name__ == "__main__":
    sms = ICEM_Interface()