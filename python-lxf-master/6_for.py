#!/usr/bin/python
# -*- coding: utf-8 -*-
'''================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	6_for.py
#    brief：
#  history:	2017-06-25  renbin.guo created
#     note:	
#    usage:	
#
#================================================================'''


names = ['A','B','C']
for name in names:
	print(name)

# 计算从1到100所有的和
sum = 0
for x in range(101):
	sum = sum + x		
print(sum)


#如何生成一个[0,1,..,10]的数组
alist = list(range(10))
print(alist)
