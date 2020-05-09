#coding=utf-8
import requests
import json
from common.login import login



host = '***********'
userName = "***********"
password = "***********"
# host_dev = 'https://icem-dev-fix.jiekecloud.cn'
headers = {'content-type': "application/json;charset=UTF-8",
				'Authorization': login(host,userName,password)}

headers_fileUpload = {'content-type': "multipart/form-data; boundary=----WebKitFormBoundaryzzZ5MqJKTjSzisxe",
				'Authorization': login(host,userName,password)}


#预发布库
DBHOST = u'*****'
DBUSERNAME = u'****'
DBUSERPASSWD = u'*****'
DBPORT = ****


# DBHOST = u'*****'
# DBUSERNAME = u'****'
# DBUSERPASSWD = u'*****'
# DBPORT = ******





