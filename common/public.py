#coding=utf-8
import requests
import json
from common.login import login



host = 'https://icem-geek-fix.jiekecloud.cn'
userName = "admin_lqx"
password = "0192023a7bbd73250516f069df18b500"
# host_dev = 'https://icem-dev-fix.jiekecloud.cn'
headers = {'content-type': "application/json;charset=UTF-8",
				'Authorization': login(host,userName,password)}

headers_fileUpload = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundaryzzZ5MqJKTjSzisxe",
				'Authorization': login(host,userName,password)}



DBHOST = u'rm-2zeoguh8vww5yhn2w.mysql.rds.aliyuncs.com'
DBUSERNAME = u'dbwrite'
DBUSERPASSWD = u'uvSQz3QwnU4dIE9Fwf'
DBPORT = 3306





