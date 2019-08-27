# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2017-10-12 21:28:46
# @Last Modified by:   Teiei
# @Last Modified time: 2017-10-12 21:31:28
## 将一个列表的数据复制到另一个列表中。
a = [1,2,3]
b = a[:]
a[0]=0
print(b)      # 将a的数据赋值给b 当a的数值发生改变时b不变

a = [1,2,3]
b = a
a[0]=0
print(b)      # 将a的地址赋值给b 当a的数值发生改变时b随之改变

