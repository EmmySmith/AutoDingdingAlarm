# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 5:10 PM
# @Author  : Emmy
# @File    : test.py.py
import counter

def create_counter():

    def increase(): #定义一个还有自然数算法的生成器,企图使用next来完成不断调用的递增

        n = 0

        while True:

            n = n+1

            yield n

    it = increase()#一定要将生成器转给一个(生成器)对象,才可以完成,笔者第一次做,这里一直出问题,

        #一直没解开,看到别人做的才更改完成

    def counter(): #再定义一内函数

        return next(it()) #调用生成器的值,每次调用均自增

    return counter



counter_ = create_counter()#用变量来指向(闭包函数返回的函数)



