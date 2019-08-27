# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2017-10-12 19:57:31
# @Last Modified by:   Teiei
# @Last Modified time: 2017-10-12 21:27:39
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fabic(n):
	if n == 0 or n == 1:
		return n
	return fabic(n-1)+fabic(n-2)
if __name__ == '__main__':
	for i in range(0,11):
		print(fabic (i))
