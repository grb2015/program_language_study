# note:
#   python3 中print 必须加括号
#   输入函数变为了input 而非raw_input
#   格式化输入(转义字符)跟c一样

name = input('what\'s your name: ')

print   ('hello,'    ,name)	#只有一个参数的时候可以这样写,renbin.guo added 2017-07-18 建议都写成%
print   ('hello,%s'  %name)

#name 为%s 100为%d
print   ('hello,%s, you have $%d' %(name,100) )

print   ('%.2f' %3.14)

# 最简单的方法，把所有的都打印成字符串
print   ('name:%s,age:%s'%('Jane',13))

