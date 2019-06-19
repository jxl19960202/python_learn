# import pickle   #pickle模块   只是适用于python,适用所有的数据格式
#
# a = [1,2,3,4,5,6]
# res = pickle.dumps(a)
# res1 = pickle.loads(res)
#
# with open('1','wb') as f:     #dump与文件操作: 将文件a序列化,并写入'1'文件中(这里的写入必须是二进制的形式)
#     pickle.dump(a,f)
#
# with open('1','rb') as f:        #load:将文件a序列化,并读出'1'文件中(这里的读必须是二进制的形式)
#     res2 = pickle.load(f)
#
# print(res2)

#json 多种语言之间传输的桥梁,json是以字符串形式保存文本的且引号必须是双引号   由道格拉斯发明
import json
a = ['a','b','c']

res = json.dumps(a)
print(res,type(res))
res1 = json.loads(res)
print(res1,type(res1))



# with open('2','w') as f:
#     json.dump(a,f)

# with open('2','r') as f:
#     res4 = json.load(f)
# print(res4,type(res4))







