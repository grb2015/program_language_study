#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file：     18_higher_order_function.py
#   breif：     高阶函数
#   history:   2017-07-20renbin.guo created
#   usage：
#   note： 
#
#================================================================

#允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#python中函数也是(对象)

#函数作为参数 把函数作为参数传入，这样的函数称为高阶函数
def add(x, y, f):
    return f(x) + f(y)
t = add(-5, 6, abs)
print(t)


# map函数 
# 返回8 
print({'0': 0, '1': 8, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['1'] )
def f(x)



