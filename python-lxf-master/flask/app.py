#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	python_app.py
#    brief：
#  history:	2017-08-01  renbin.guo created
#     note:	
#    usage:	
#
#================================================================

from flask import Flask
from flask import request

app = Flask(__name__)
## 这个app.route是flask内部实现的装饰器,它用于在执行home()前或后，进行一些动作，也就是将url和http 方法联系起来
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
	#需要从request对象读取表单内容   ，这里的request是我们import进来的.
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin!</h3>'
	return '<h3>Bad username or password.</h3>'
if __name__ == '__main__':
	app.run()
