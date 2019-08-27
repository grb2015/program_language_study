# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2017-10-12 21:34:31
# @Last Modified by:   Teiei
# @Last Modified time: 2017-10-12 21:42:22
#输出 9*9 乘法口诀表
for i in range(1,10):
	for j in range(i,10):
		print('%s*%s=%s\t'%(i,j,i*j),end="")  ### 不加end=""则每个print都会换行
	print('\n')