#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	9_fun.py
#    brief：
#  history:	2017-07-19  renbin.guo created
#     note:	
#    usage:	
#
#================================================================'''

#1.求一个数的绝对值,函数的定义
def my_abs(x):
	if x>0:
		return x
	else:
		return	-x
a = -5
b = my_abs(a)
print(b)


# 2. 函数的默认参数

#s=1  定义在这里还不行
#求x^n次方,并设置默认参数为2次方
def my_power(x,n=2):
	s=1;
	for i in range(n):
	#while(n>0):
	#	n-=1
		s*=x
	return s
print(my_power(5,2))
print(my_power(5))
print(my_power(5,3))


#一个班级中,默认年龄都为6，城市都为北京
def enroll(name, gender, age=6, city='Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
enroll('sarah','F')
# enroll('sarah','F','tianjing') 这个有问题
enroll('sarah','F',city='tianjing') 



#3. 默认参数的坑
	#定义函数add_end在给定的参数list类型后，加入一个END元素,奇怪，你怎么知道参数的类型是list?如果你这样调用 add_end(1),则会报错：
	# 'int' object has no attribute 'append'
def add_end(L=[]):
	L.append('END')
	print(L)
	return L
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
add_end()
add_end()	#这里就有错误了，会返回['END', 'END'],可见上一次调用add_end()后，默认参数就变成了'END'

#解决，可变对象list不能作默认参数，字符串和整数等不可变对象可以
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	print(L)
	return L
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
add_end()
add_end()	
# add_end(1) 报错  'int' object has no attribute 'append'
