#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	4.py
#    brief£º题目：输入某年某月某日，判断这一天是这一年的第几天？
#  history:	2017-10-10  renbin.guo created
#     note:	
#    usage:	
#
#================================================================
year =int(input("please input the year:"))
month =int( input("please input the mouth:"))
day   = int(input("please input the day:"))
num = -1
if year % 4 == 0:
	months = [31,28,31,30,31,30,31,31,30,31,30,31]
else:
	months = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
	if i<month:
		num = num+months[i-1]
	else:
		break
num = num + day+1
print("%s-%s-%s is the %sth day of this year"%(year,month,day,num))



