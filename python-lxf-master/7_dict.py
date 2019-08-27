#!/usr/bin/python
# -*- coding: utf-8 -*-
'''================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	7_dict.py
#    brief：
#  history:	2017-06-25  renbin.guo created
#     note:	
#    usage:	
#
#================================================================'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Bob'])

#增,改
d['Adam']= 67
d['Adam']= 88
print(d)


#删
d.pop('Adam')
print(d)

#查,获取value的值
  #方法1
Bvalue = d.get('Bob')
print(Bvalue)
  #方法2
print('bob = %s'%d['Bob'])  

#一般要先判断是否存在，为了判断是否存在有两种方法，
#1.使用get 不存在返回none
#2 判断是否存在，返回true or false
if('Thomas' in d):
    print(d['Thomas'])  
else:
    print('Thomas not exist!')
if( d.get('xx') != None ):
    print(d['Thomas'])  
else:
    print('Thomas not exist!')
    


