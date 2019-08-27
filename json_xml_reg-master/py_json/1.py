## 参考 http://www.jb51.net/article/73450.htm
##      http://www.jb51.net/article/122614.htm
import json
'''
json字符串和python的转换:
 1.json.dumps() :将python数据转为json字符串
 2.json.loads() :将json字符串解析为python的数据结构

运行结果:
example1 
[root@localhost py_json]# python 1.py 
{"name": "ACME", "shares": 100, "price": 542.23}
<class 'str'>
{'name': 'ACME', 'shares': 100, 'price': 542.23}
<class 'dict'>

 '''
##example1.
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
# 将python的数据类型(dict)转为json的格式  
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
## 反之，将json_str转为python的dict
py_str = json.loads(json_str)
print(py_str)
print(type(py_str))
print('\n\n')


### example2: 再次举个例子将json格式字符串解析出来作为Python的dict
''' output
{'name': 'test', 'type': {'name': 'seq', 'parameter': ['1', '2']}}
dict_keys(['name', 'type'])
test
seq
2
'''

s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print (s)  ### 得到一个python的dict
print (s.keys())
print (s["name"])
print (s["type"]["name"])
print (s["type"]["parameter"][1])


### example 3: 将python的list转为json
aItem = {}
aItem["id"] = "2203"
aItem["title"] = "title"
aItem["subTitle"] = "sub title"
bItem = {}
bItem["id"] = "2842"
bItem["title"] = "b标题"
bItem["subTitle"] = "b副标题"
bItem["content"] = "内容"
bItem["list"] = ["a", "a 2", "b", "bb"]

python_list = []    ###  [{},{}]  list的元素为dict
python_list.append(aItem)
python_list.append(bItem)
jsonArr = json.dumps(python_list, ensure_ascii=False)
print(jsonArr)
###输出的json  [{"id": "2203", "title": "title", "subTitle": "sub title"}, {"id": "2842", "title": "b标题", "subTitle": "b副标题", "content": "内容"}]
