#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	count.py
#    brief£º
#  history:	2017-07-22  renbin.guo created
#     note:	
#    usage:	
#
#================================================================

from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch]=c[ch]+1
print (c)


