#coding=utf-8

# 测试
import pymysql
import pymysql.cursors
#将mysql需要的参数（DBHOST,DBPORT,DBUSERNAME,DBUSERPASSWD,DBNAME）导入
from common.public1 import *

#创建mysql连接类
class DB_api1(object):
    def __init__(self,dbname):
        self.conn = pymysql.Connect(host=DBHOST,port=DBPORT,user=DBUSERNAME,passwd=DBUSERPASSWD,db=dbname,charset='utf8')

    #获取动态盘点单id和库区id
    def get_values(self,sql):
        self.cur =self.conn.cursor()
        # sql = '''SELECT id FROM sms_dynamic_check ORDER BY id DESC LIMIT 1;'''
        self.cur.execute(sql)
        #获取执行的结果
        data = self.cur.fetchall()
        #根据字典取值的方式获取id和kq_id
        # print(data)
        values = data[0][0]
        # print(values)
        return values

    def delete_data(self,sql):
        self.cur =self.conn.cursor()
        # sql = '''DELETE FROM tprj_buhuodan_feedback WHERE material_id = '1000006' ORDER BY id DESC LIMIT 1;'''
        self.cur.execute(sql)
        self.conn.commit()
        self.cur.close()

    def update_values(self,sql4):

        self.cur=self.conn.cursor()
        try:
            self.cur.execute(sql4)
            self.conn.commit()
        except:
            self.conn.rollback()

        self.conn.close()
        

# if __name__ == "__main__":
#     con=DB_ICEM_proc()
#     con.get_dtpd_id("SELECT id FROM sms_dynamic_check ORDER BY id DESC LIMIT 1;")
    # print con.bank_domain()