#!/usr/bin/python
# -*- coding: utf-8 -*-
'''================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	5_if.py
#    brief：    条件语句的演示
#  history:	2017-06-10  renbin.guo created
#     note:	
			python中没有&& || 只有and or 
			python 中没有else if 只有elif
#    usage:	
#
#================================================================'''

birth = input('birth:')
#   birth是str类型,所以要转换为int
if int(birth)>= 2000: 
    print('00后')
elif(1990<int(birth) and  int(birt)<2000):
    print('90后')
else:
	print('not defined')



