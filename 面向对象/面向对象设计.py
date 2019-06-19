#面向对象   作用:避免出现重复的代码,封装.
#1.面向对象设计 使用函数的形式
# cat = {
#     'sex':'man',
#     'age':1,
# }
# def _jiao():
#     print('猫在叫')
#为了避免其他对象使用该特性,利用函数的作用域进行封装

# def cat(sex,age):
#     def _jiao():                       #利用函数的作用域将猫的特性封装起来避免其他东西使用该特性
#         print('猫在叫')
#
#     cat = {
#         'sex': sex,
#         'age': age,
#         'jiao':_jiao
#     }
#     return cat
#
# cat1 = cat('man',1)
# print(cat1)
# cat1['jiao']()

#改进如下:
def cat(sex,age):
    def _jiao():
        print('猫在叫')
    def init():
        cat = {
            'sex': sex,
            'age': age,
            'jiao': _jiao
        }
        return cat
    res = init()
    return res
c1 = cat('man',2)
print(c1['sex'])













