#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	hello.py
#    brief：Http请求的处理函数，构造一个只有一行的html文件。显示hello,name
#  history:	2017-08-01  renbin.guo created
#     note:	
#    usage:	
#
#================================================================


def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])

	#return [b'<h1>Hello,web!</h1>']  version 1

	#version 2 可以显示参数		这里的environ是一个dict,'PATH_INFO'是它的一个key ,我们取它的[1:len]长度的字段
	body = '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:]or 'web')
	return [body.encode('utf-8')]

