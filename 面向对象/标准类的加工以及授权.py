#对标准的类型添加新的功能,或改变原来的功能  及派生类继承标准类,并做出新增功能或改变标准类原有的功能
# class List(list):
#     def get_median(self):
#         res = len(self)//2   #给列表添加了找中间值的功能(派生)
#         return self[res]
#     def append(self,x):
#         if isinstance(x,str):
#             # list.append(self,x)         #这里必须调用list内的append方法,如果调用该类的会出现无限递归
#             super().append(x)
#         else:
#             print('必须是字符串格式的')
#
#
# l1 = List('abcde')
# # print(l1.get_median())
# l1.append('l')
# print(l1)

#授权,对一个类赋予其他的功能(不是继承),且类内不出现该功能的代码.运用组合的方式,
#__getatter__以及detatter()

#写一个文件处理的类,对该类授权文件的读写操作并对写操作添加新的功能(组合)
import time
class Haddle_file:
    def __init__(self,file,pattern,encoding):
        self.file = open(file,pattern,encoding=encoding)
        self.pattern = pattern
        self.encoding = encoding

    def write(self,obj):
        return self.file.write(str(time.asctime()) +'---'+ obj)


    def __getattr__(self, item):
        return getattr(self.file,item)


f1 = Haddle_file('jxl','w+',encoding='utf-8')
f1.write('111')
f1.seek(0)       #seek 的作用是移动光标的位置
res = f1.read()
print(res)




































