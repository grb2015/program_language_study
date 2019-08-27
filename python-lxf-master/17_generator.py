#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file：     17_generator.py
#   breif：    生成器
#   history:   2017-07-20renbin.guo created
#   usage：     
#   note：      一边循环一边计算，推算出后面的
#                          
#          
#           
#================================================================


# 我们知道生成一个list可以这样
L=[x*x for x in range(10)]
print(L)

# 将[] 变为()就生成了一个生成器
g=(x*x for x in range(10))
print(g)  # 它不能打印，<generator object <genexpr> at 0x7f46ec00b410>
#要打印生成器
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('-----------------\n')
#或者
for i in g:
    print(i)



#用list并不能生成斐波拉契数列,用函数可以
print('------fib-----------\n')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# fib 推算出后续任意的元素，这种逻辑其实非常类似generator。
# 用generator生成fib ,只是将上面的print改为了yield
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

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



# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

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
