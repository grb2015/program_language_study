# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2017-10-12 21:45:12
# @Last Modified by:   Teiei
# @Last Modified time: 2017-10-12 21:51:53
#暂停一秒输出，并格式化当前时间。
import time ,datetime
cur_time =  time.strftime('%Y-%m-%d %H:%M:%s',time.localtime(time.time()))
print(cur_time)
time.sleep(1)
cur_time =  time.strftime('%Y/%m/%d %H:%M:%s',time.localtime(time.time()))
print(cur_time)


time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y:%m:%d %H-%M-%S"))


