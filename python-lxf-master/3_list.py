# -*- coding: UTF-8 -*- 
#================================================================
#   Copyright (C) 2017 free for learn
#   
#   file:	2_list.py
#   brief：
#   history：2017-06-08
#   note：
#   usage：
#        [root@grb_host python-lxf]# python 2_list.py 
#        ['micheal', 'bob', 'tracy']
#               3
#        micheal
#        bob
#        tracy
#        tracy
#        [root@grb_host python-lxf]# 
#
#================================================================
classmate = ['micheal','bob','tracy']

#   1.打印list
print ('list classmate= %s'%classmate)

#   2.获取list长度
len = len(classmate)
print('len = ',len)

#   3.循环访问list中的成员
     	#方法1
print('-----for 1-----')
for i in range(len):
    print('classmate[%d]= %s'%(i,classmate[i]))
	#方法2
print('-----for 2-----')
for name in classmate:
	print(name)



#   4.要访问最后一个成员，可以使用-1作下标
print('classmate[-1]=%s'%classmate[-1])

#-----增删查改------------

#   5.增(追加/插入)
classmate.append('adam')
print ('\nAfter appended \'adam\' in last:\nlist classmate= %s'%classmate)

classmate.insert(1,'Jack')
print ('\nAfter inserted \'Jack\' in the 1 position:\nlist classmate= %s'%classmate)

#   6.删
classmate.pop();
print ('\nAfter pop():\nlist classmate= %s'%classmate)
classmate.pop(0);
print ('\nAfter pop(0):\nlist classmate= %s'%classmate)

#   7.改
classmate[1]='Sarah'
print ('\nAfter modify: classmate[1] = \'Sarah\'\nclassmate= %s'%classmate)


#list 可以有不同的数据类型
print('\n')
L = ['Apple', 123, True]
print(L)

#list中可以包含另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
#等价于 
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
#类似二维数组的访问
print('\n')
print(s[2][0])
print(s[2][1])


