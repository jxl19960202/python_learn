#高阶函数：函数接收的参数是一个函数名，函数的返回值包含函数。
# def text1():
# #     print('text1')
# #
# # def text2():
# #     print('text2')
# #     return text1()
# #
# # text2()

#lambda表达式（匿名函数）
# def muil(x):
#     return x**2
#
# print(muil(2))
# lambda x:x**2
# print(a(2))

#map()
# a = [1,2,3,4,5]
# # def _cl(x):
# #     b = []
# #     for i in x:
# #         i = i**2
# #         b.append(i)
# #     return b
# # c= _cl(a)
# # print(c)
# #
# # a = [1,2,3,4,5]
# # def muil(y):
# #     return y**3
# #
# # def _cl(func,x):
# #     b = []
# #     for i in x:
# #         i = func(i)
# #         b.append(i)
# #     return b
# # c= _cl(muil,a)
# # print(c)
# #
# # def _cl(func,x):
# #     b = []
# #     for i in x:
# #         i = func(i)
# #         b.append(i)
# #     return b
# # c= _cl(lambda x:x**2,a)
# # print(c)
# #
# # a = [1,2,3,4,5]
# # b = map(lambda x:x**3,a)
# # print(b)
# # print(list(b))

# filter() 过滤掉不需要的元素


# a = [1,2,3,4,5,6,7,8]
# def _filter(x):
#     b = []
#     for i in x:
#         if i < 5:
#             b.append(i)
#     return b
# c = _filter(a)
# print(c)
#
# a = [1,2,3,4,5,6,7,8]
# def _panduan(y):
#     if y < 5:
#         return True
#
# def _filter(func,x):
#     b = []
#     for i in x:
#         if func(i):
#             b.append(i)
#     return b
# c = _filter(_panduan,a)
# print(c)
#
# a = [1,2,3,4,5,6,7,8]
# def _filter(func,x):
#     b = []
#     for i in x:
#         if func(i):
#             b.append(i)
#     return b
# c = _filter(lambda x:x<5,a)
# print(c)
#
# a = [1,2,3,4,5,6,7,8]
# b = filter(lambda x:x<5,a)
# print(list(b))

#reduce函数的使用，要先引入functools模块中的reduce函数。


# num1 = [1,2,3,4,5,6,7]
# def muil(x,y):
#     return x*y
#
# def _muil(func,sequence,initial = None):
#     if initial == None:
#         res = sequence.pop(0)
#     else:
#         res = initial
#     for i in sequence:
#         res = func(res,i)
#     return res
# a =_muil(muil,num1,10)
# print(a)
#
# num1 = [1,2,3,4,5,6,7]
# def _muil(func,sequence,initial = None):
#     if initial == None:
#         res = sequence.pop(0)
#     else:
#         res = initial
#     for i in sequence:
#         res = func(res,i)
#     return res
# a =_muil(lambda x,y:x*y,num1,10)
# print(a)
#
# from functools import reduce
# num1 = [1,2,3,4,5,6,7]
# a= reduce(lambda x,y:x*y,num1)
# print(type(a),a)


