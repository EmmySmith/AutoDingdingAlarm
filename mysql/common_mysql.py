#coding=utf-8

import pymysql
import pymysql.cursors
#将mysql需要的参数（DBHOST,DBPORT,DBUSERNAME,DBUSERPASSWD,DBNAME）导入
from common.public import *

#创建mysql连接类
class DB_api(object):
    def __init__(self,dbname):
        self.conn = pymysql.Connect(host=DBHOST,port=DBPORT,user=DBUSERNAME,passwd=DBUSERPASSWD,db=dbname,charset='utf8')

    #获取动态盘点单id和库区id
    def get_values(self,sql):
        self.cur =self.conn.cursor()
        self.cur.execute(sql)
        #获取执行的结果
        data = self.cur.fetchall()
        #根据字典取值的方式获取id和kq_id
        # print(data)
        # values = list(data)
        values = data[0][0]

        # print(values)
        return values

    def delete_data(self,sql):
        self.cur =self.conn.cursor()
        self.cur.execute(sql)
        self.conn.commit()
        self.cur.close()

    def update_date(self):
        sql=''
        self.cur=self.conn.cursor()
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

        self.conn.close()
        

