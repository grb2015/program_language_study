#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     23_import.py
#   breif��
#   history:   2017-07-21renbin.guo created
#   usage��
#   note�� 
#               �������в��Ǻ���ȷ��       
#
#================================================================

from PIL import Image
im = Image.open('eat1.png')
im.show() # 
im = im.convert('RGB')      #�����������


print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')



#��ӡģ�������·��

import sys
print(sys.path)
