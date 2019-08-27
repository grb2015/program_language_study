#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	producer_consumer.py
#    brief：用协程实现生产者，消费者
#  history:	2017-08-05  renbin.guo created
#     note:	
#    usage:	
#
#================================================================

### 关于协程
### '协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行'
## '注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断'
## '看起来A、B的执行有点像多线程 ,协程的特点在于是一个线程执行'
##

##１最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
## 2. 不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多


##  Python对协程的支持是通过generator生成器实现的

#消费者
def consumer():
    r = ''      #声明变量r
    while True:
        n = yield r     #使用了yield ,代表consumer是一个生成器
                        # yield不但可以返回一个值，它还可以接收调用者发出的参数
                        # 所以,从produce中send过来的参数n就是通过yield 被传递给了consumer的n
                        # 而显然consumer中每次返回的r就通过produce的send返回给了produce的中r
        if not n:       #如果n为0 (也即是consumer中send(0)),则返回
            return 
    print('[CONSUMER]consuming %s...'%n)
    r='200 ok'
#生产者
def produce(c):
    c.send(None)        #启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   # 一旦生产了东西，通过c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close() ## produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

c = consumer()  ## 之类consumer是一个生成器。
produce(c)      ## 生成器(函数)作参数，就是一个协程?

    

      
    

