#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================
#  Copyright (C) 2017 free for learn
#   
#     file:	1.py
#    brief����Ŀ����1��2��3��4�����֣�����ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
#  history:	2017-10-10  renbin.guo created
#     note:	
#    usage:	
#
#================================================================
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i!= j and i!=k and j!=k:
				print(i*100+j*10+k)
    


