#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	9_fun.py
#    brief��
#  history:	2017-07-19  renbin.guo created
#     note:	
#    usage:	
#
#================================================================'''

#1.��һ�����ľ���ֵ,�����Ķ���
def my_abs(x):
	if x>0:
		return x
	else:
		return	-x
a = -5
b = my_abs(a)
print(b)


# 2. ������Ĭ�ϲ���

#s=1  ���������ﻹ����
#��x^n�η�,������Ĭ�ϲ���Ϊ2�η�
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


#һ���༶��,Ĭ�����䶼Ϊ6�����ж�Ϊ����
def enroll(name, gender, age=6, city='Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
enroll('sarah','F')
# enroll('sarah','F','tianjing') ���������
enroll('sarah','F',city='tianjing') 



#3. Ĭ�ϲ����Ŀ�
	#���庯��add_end�ڸ����Ĳ���list���ͺ󣬼���һ��ENDԪ��,��֣�����ô֪��������������list?������������� add_end(1),��ᱨ��
	# 'int' object has no attribute 'append'
def add_end(L=[]):
	L.append('END')
	print(L)
	return L
add_end([1, 2, 3])
add_end(['x', 'y', 'z'])
add_end()
add_end()	#������д����ˣ��᷵��['END', 'END'],�ɼ���һ�ε���add_end()��Ĭ�ϲ����ͱ����'END'

#������ɱ����list������Ĭ�ϲ������ַ����������Ȳ��ɱ�������
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
# add_end(1) ����  'int' object has no attribute 'append'
