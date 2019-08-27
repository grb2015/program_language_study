#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	4_tuple.py
#    brief：    tuple:const的list
#  history:	2017-06-10  renbin.guo created
#     note:	
#    usage:	
#
#================================================================

#classmate不能变了，所以不能对其增/删/改
classmates = ('Michael', 'Bob', 'Tracy')


#定义只有一个元素的tuple,注意要加,不然等价于t=1,成了变量
t= (1,)

# 可以对里面的[]现有的元素进行增删改
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)

t[2].append('Z')
print(t)

t[2].pop(0)
print(t)

t[2].pop()
print(t)


