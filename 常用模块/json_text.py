#json的作用,用于不同语言之间数据的传输.json作为中介
#序列化与反序列化
#json数据的格式,必须是字符串,而且必须是用双引号表示的
#序列化  python转化为json
dict1 = {'name':'jiang','age':17}
import json
date1 = json.dumps(dict1)
# 将字典转化为字符串,并将字符串内的单引变为双引.其他数据类型的也一样
print(type(date1),date1)#<class 'str'> '{"name": "jiang", "age": 17}'
#反序列化  json转其他语言
date2 = json.loads(date1)   #  将json语言转化为python语言
print(type(date2),date2)   #<class 'dict'> {'name': 'jiang', 'age': 17}













