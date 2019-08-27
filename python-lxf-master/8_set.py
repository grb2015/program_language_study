#!/usr/bin/python
# -*- coding: utf-8 -*-

#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	8_set.py
#    brief：
#  history:	2017-07-19  renbin.guo created
#     note:	
#    usage:	
#================================================================

# set更dict一样，不过它只有key,没有value,它可以看做数学上的集合。
# 具有互异向和无序性 

#要创建一个set ,需要传入一个list
s = set([1,2,3])
print(s)

#增 
s.add('a')	#这里加入一个value 4,由于set是无序的,它是一个集合,所以不需要s.add(4,'a')
print(s)

#删 remove(key)
s.remove(2)
print(s)

#查,由于它是一个集合，所以不存在说查第几个元素的说法，查就是查看这一个集合
print(s)

#改  对于集合而已，其实只有增加元素和删除元素


#集合的交、并操作

a = set([1,2,3])
b = set([1,2,4])
c = a & b
d = a|b
print(c)
print(d)
