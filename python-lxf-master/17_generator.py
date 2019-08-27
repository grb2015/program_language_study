#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     17_generator.py
#   breif��    ������
#   history:   2017-07-20renbin.guo created
#   usage��     
#   note��      һ��ѭ��һ�߼��㣬����������
#                          
#          
#           
#================================================================


# ����֪������һ��list��������
L=[x*x for x in range(10)]
print(L)

# ��[] ��Ϊ()��������һ��������
g=(x*x for x in range(10))
print(g)  # �����ܴ�ӡ��<generator object <genexpr> at 0x7f46ec00b410>
#Ҫ��ӡ������
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('-----------------\n')
#����
for i in g:
    print(i)



#��list����������쳲���������,�ú�������
print('------fib-----------\n')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# fib ��������������Ԫ�أ������߼���ʵ�ǳ�����generator��
# ��generator����fib ,ֻ�ǽ������print��Ϊ��yield
#����Ƕ���generator����һ�ַ��������һ�����������а���yield�ؼ��֣���ô��������Ͳ�����һ����ͨ����������һ��generator

print('------fib generator-----------\n')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(6)
print(f)
for i in f:
    print(i)



# ������˳��ִ�У�����return���������һ�к������ͷ��ء������generator�ĺ�������ÿ�ε���next()��ʱ��ִ�У�����yield��䷵�أ��ٴ�ִ��ʱ���ϴη��ص�yield��䴦����ִ��

print('------odd-----------\n')
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
print(next(o))
print(next(o))
print(next(o))
