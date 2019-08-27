#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	3.py
#    brief£º题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#  history:	2017-10-10  renbin.guo created
#     note:	
#    usage:	
#
#================================================================
import math
for num in range(1,10001):
	if math.sqrt(num+100) == int(math.sqrt(num+100))  and math.sqrt(num+168) == int(math.sqrt(num+168)):
		print("%s"%num)

