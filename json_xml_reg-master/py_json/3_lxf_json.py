## 将python的类对象于json互转
import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

## 1.类对象转为json对象. 
def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

# 为Student专门写一个转换函数，再把函数传进去即可：

s = Student('Bob',20,88)
print(json.dumps(s, default=student2dict))   ### josn 类型  {"age": 20, "score": 88, "name": "Bob"}  



## 2. json字符串转为类对象。

# 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str='{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))  ## 得到一个student对象 <__main__.Student object at 0x00BFA510> 
