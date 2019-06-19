#random 随机模块
import random
# print(random.random())   #随机选取0-1的小数
# print(random.randint(1,10))   #传入2个数字,随机取这2个数之间的一个数(包括这2个数)
# print(random.randrange(1,3))   #传入2个数字,随机取这2个数之间的一个数(前开后闭)
# print(random.choice([i for i in range(10)]))    #传入一个可迭代的
# print(random.sample([i for i in range(10)],2))  #参数传入一个可迭代的,以及要返回的几个数
#随机验证码
# def _random():
#     _str = ''
#     for i in range(4):
#         num1 = random.randint(0,9)
#         num2 = chr(random.randint(65,122))
#         res = str(random.choice([num1,num2]))
#         _str += res
#     return _str
# print(_random())






