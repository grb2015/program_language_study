#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file：     23_import.py
#   breif：
#   history:   2017-07-21renbin.guo created
#   usage：
#   note： 
#               好像运行不是很正确。       
#
#================================================================

from PIL import Image
im = Image.open('eat1.png')
im.show() # 
im = im.convert('RGB')      #不加这句会出错


print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')



#打印模块的搜索路径

import sys
print(sys.path)
