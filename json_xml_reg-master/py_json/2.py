### 1.py学习了字符串的json和python互转
### 现在学习文件互转： 将python的数据结构转为json文件/从json文件解析python数据结构
# Writing JSON data
import json
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
with open('6-1.json', 'w') as f: ## 创建6-1.json
	json.dump(data, f)
 
# Reading data back
with open('6-2.json', 'r') as f:
	data = json.load(f)
print(data)
print(type(data))  ## dict 
