# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2017-10-12 21:43:14
# @Last Modified by:   Teiei
# @Last Modified time: 2017-10-12 21:44:06
# 暂停一秒输出。
import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) # 暂停 1 秒
