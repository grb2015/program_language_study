#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     22_Decorator.py
#   breif��     װ����
#   history:   2017-07-20renbin.guo created
#   usage��
#   note�� 
#
#================================================================

def now():
    print('2015-3-25')
f=now
f()

print (now.__name__)
print (f.__name__)

#���ڣ���������Ҫ��ǿnow()�����Ĺ��ܣ����磬�ں�������ǰ���Զ���ӡ��־�����ֲ�ϣ���޸�now()�����Ķ��壬�����ڴ��������ڼ䶯̬���ӹ��ܵķ�ʽ����֮Ϊ��װ��������Decorator����

# �����ϣ�decorator����һ�����غ����ĸ߽׺��������ԣ�����Ҫ����һ���ܴ�ӡ��־��decorator�����Զ�������
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
