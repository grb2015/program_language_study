#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	python_app.py
#    brief��
#  history:	2017-08-01  renbin.guo created
#     note:	
#    usage:	
#
#================================================================

from flask import Flask
from flask import request

app = Flask(__name__)
## ���app.route��flask�ڲ�ʵ�ֵ�װ����,��������ִ��home()ǰ��󣬽���һЩ������Ҳ���ǽ�url��http ������ϵ����
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
			 <p><input name="username"></p>
              <p><input name="password" type="password"></p>
			 <p><button type="submit">Sign In</button></p>
			 </form>'''
@app.route('/signin',methods=['POST'])
def signin():
	#��Ҫ��request�����ȡ������   �������request������import������.
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin!</h3>'
	return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
	app.run()
