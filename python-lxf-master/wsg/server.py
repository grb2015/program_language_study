#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	server.py
#    brief��
#  history:	2017-08-01  renbin.guo created
#     note:	
#    usage:	
#[root@localhost wsg]# python server.py 
#		version1:
#		Serving HTTP on port 8000 ...		# then visit http://localhost:8000/   on �����

#		127.0.0.1 - - [01/Aug/2017 22:22:44] "GET / HTTP/1.1" 200 19
#		127.0.0.1 - - [01/Aug/2017 22:22:44] "GET /favicon.ico HTTP/1.1" 200 19
#		127.0.0.1 - - [01/Aug/2017 22:22:44] "GET /favicon.ico HTTP/1.1" 200 19
#
#		version 2:
#			[root@localhost wsg]# python server.py 

#			Serving HTTP on port 8000 ...	#����������� http://localhost:8000/guorenbin

#			127.0.0.1 - - [01/Aug/2017 22:33:51] "GET /guorenbin HTTP/1.1" 200 25
#
#================================================================

# wsgiref��һ��������ģ��
from wsgiref.simple_server import make_server

# ���������Լ���д��application����
from hello import application

#����һ����������IP��ַΪ�գ��˿���8000
httpd = make_server('',8000,application)   #application���Ǵ���http����ĺ���
print('Serving HTTP on port 8000 ...')
httpd.serve_forever()
