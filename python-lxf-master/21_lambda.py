#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     21_lambda.py
#   breif��
#   history:   2017-07-20renbin.guo created
#   usage��
#   note�� 
#
#================================================================

l= list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print l

# ͨ���Աȿ��Կ�������������lambda x: x * xʵ���Ͼ��ǣ�
def f(x):
        return x * x

