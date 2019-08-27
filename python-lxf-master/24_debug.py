#!/usr/bin/sh
#-*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2017  free for learn .
#   
#   file£º     24_debug.py
#   breif£º
#   history:   2017-07-21renbin.guo created
#   usage£º
#   note£º 
#
#================================================================
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


