# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 11:57 PM
# @Author  : Emmy
# @File    : days.py

import time
import datetime


# def Caltime(date1,date2):
#     #%Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
#     #date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
#     #date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
#     date1=time.strptime(date1,"%Y-%m-%d")
#     print(date1)
#     date2=time.strptime(date2,"%Y-%m-%d")
#     #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
#     #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
#     #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
#     date1=datetime.datetime(date1[0],date1[1],date1[2])
#     date2=datetime.datetime(date2[0],date2[1],date2[2])
#     #返回两个变量相差的值，就是相差天数
#     return date2-date1
#     print(date2-date1)



# def Caltime(date1,date2):
#     # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
#     # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
#     # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
#     date1 = datetime.datetime.now().strftime('%Y%m%d')
#     date2 = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y%m%d')
#     # date1 = str(datetime.datetime(date1[0], date1[1], date1[2]))
#     # date2 = str(datetime.datetime(date2[0], date2[1], date2[2]))
#     print(date1)
#     minus = str(abs(date1 - date2))
#
#     return minus
#
# if __name__ == '__main__':
#
#
#     Caltime()
from dateutil.parser import parse


now=datetime.datetime.now()
d2 = parse(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print('当前日期：')
print (d2)


print('7天前的日期为：')
d3=parse((datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d'))
print (d3)

chazhi = (d3 - d2).days


print(chazhi)





