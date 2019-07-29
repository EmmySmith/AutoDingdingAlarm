# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 10:05
# @Author  : renming
# @File    : getIssueCount.py


#coding:utf-8

from common.count import *
c = num


def replace():
    number = c + 1
    data = ''
    with open('../common/count.py', 'r+',encoding='UTF-8') as f:
        for line in f.readlines():
            if(line.find('num=') == 0):
                line = "num="+str(number)
            data += line
    with open('../common/count.py', 'r+') as f:
        f.writelines(data)
        f.flush()
        f.seek(0)
        f.close()



def getOldNum(num):
    print("Num is :",num)
    if num == 1:
        number = c + 1
        replace()
        return number
    else:
        return c

# getOldNum(1)
# n = getOldNum(1)
# print(n)


# replace("dev")







def readFile():
    with open('../common/count.py', 'r+', encoding='utf8') as f:
        # for line in f:
        #     count = int(line)
        #     print(count)
        #     # f.close()
        #     print("count is:",count)
        count = f.read()
        # print(type(count))
        c = "".join(count)
        print(c)
        return c



def writeFile(num):
    with open('../common/count.py','w+',encoding='utf8') as f:
        count = num + 1
        f.write(str(count))
        f.flush()
        f.seek(0)
        # f.close()
        return count


def bugCount(issue):
    if issue == 0:
        readFile()
    else:
        num = readFile()
        writeFile(num)

# count = bugCount(0)
# print(count)