#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	hello.py
#    brief��Http����Ĵ�����������һ��ֻ��һ�е�html�ļ�����ʾhello,name
#  history:	2017-08-01  renbin.guo created
#     note:	
#    usage:	
#
#================================================================


def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])

	#return [b'<h1>Hello,web!</h1>']  version 1

	#version 2 ������ʾ����		�����environ��һ��dict,'PATH_INFO'������һ��key ,����ȡ����[1:len]���ȵ��ֶ�
	body = '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:]or 'web')
	return [body.encode('utf-8')]

