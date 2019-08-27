#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file：     27_json.py
#   breif：
#   history:   2017-07-21renbin.guo created
#   usage：
#   note： 

#   >>> import json
#   >>> d = dict(name='Bob', age=20, score=88)
#   >>> json.dumps(d)
#        '{"age": 20, "score": 88, "name": "Bob"}'
#
#================================================================


import json
d = dict(name='Bob', age=20, score=88) #这里相当于是把()内的对象强制转为dict类型,为什么能这样做啊?
print(d)    #{'name': 'Bob', 'age': 20, 'score': 88}
json.dumps(d)
print(d)    # {'name': 'Bob', 'age': 20, 'score': 88}  #这个只有在命令行看起来才是字符串，dumps()方法返回一个str


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json_str)
json.loads(json_str)
print(json_str)
