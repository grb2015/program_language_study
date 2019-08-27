#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file：     20_return_fun.py
#   breif：    返回值为函数。闭包
#   history:   2017-07-20renbin.guo created
#   usage：
#   note： 
#
#        在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#
#================================================================
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9 )
print(f)  #当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
         # <function lazy_sum.<locals>.sum at 0x7f27d89f3048>


a=f()   # 调用函数f时，才真正计算求和的结果：
print(a) #25


print('-----------------count----------------\n')
# 在下面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 所以，返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print(f1())  #返回时9 还是1   ,是9 ！
print(f2()) # 9
print(f3()) # 9


