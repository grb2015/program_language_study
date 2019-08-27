#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	5.py
#    brief£º题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#  history:	2017-10-10  renbin.guo created
#     note:	
#    usage:	
#
#================================================================
l =[]
for i in range(0,3):
	l.append ( int(input("input  l[%s] th num:"%i)) )
print("\n")
for i in range(0,3):
	if l[i] == max(l[0],l[1],l[2]):
		print("max is l[%s]=%s  "%(i,l[i]))
	elif l[i] == min(l[0],l[1],l[2]):
		print("min is l[%s]=%s  "%(i,l[i]))
	else:
		print("middle is l[%s]=%s  "%(i,l[i]))
