#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     27_json.py
#   breif��
#   history:   2017-07-21renbin.guo created
#   usage��
#   note�� 

#   >>> import json
#   >>> d = dict(name='Bob', age=20, score=88)
#   >>> json.dumps(d)
#        '{"age": 20, "score": 88, "name": "Bob"}'
#
#================================================================


import json
d = dict(name='Bob', age=20, score=88) #�����൱���ǰ�()�ڵĶ���ǿ��תΪdict����,Ϊʲô����������?
print(d)    #{'name': 'Bob', 'age': 20, 'score': 88}
json.dumps(d)
print(d)    # {'name': 'Bob', 'age': 20, 'score': 88}  #���ֻ���������п����������ַ�����dumps()��������һ��str


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json_str)
json.loads(json_str)
print(json_str)
