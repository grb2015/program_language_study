#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file��     24_debug.py
#   breif��
#   history:   2017-07-21renbin.guo created
#   usage��
#   note�� 
#
#================================================================
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


