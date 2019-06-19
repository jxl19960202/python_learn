# enumerate(iterable,start) iterable可以迭代的对象，（star开始索引的下标，默认为0）
# enumerate（）函数为可迭代对象，返回可迭代对象内部的下标以及对应的值
# a = ['a','b','c','d']
# dict_1 = {}
# for i,j in enumerate(a):
#     dict_1[j] = i
# print(dict_1)

# eval() 去掉两侧的引号
# a ='[1,2,3]'
# b = eval(a)
# print(type(b),b)

# ord , chr   0rd()将字符转化为ascii码表中对应的数字，chr将数字转化为ascii码表中对应的字符
# print(ord('a'))
# print(chr(97),type(chr(97)))

#bytes 转化字符的编码
# a = '姜小龙'
# b = bytes(a,encoding='utf_16')
# print(b)

# isinstance(x,y)  判断x这个对象是否是y类的，返回bool值
# b = isinstance(1,int)
# print(b)

# divmod(x,y) :取商取余 可用于分页。 返回值为x//y,x%y
# a= divmod(10,3)
# print(a)

# name = ['jiang','xiao','long']
# age = [14,5,78,34]
# sex = ['man','man','girl','man']
# print(zip(name,age,sex))
# print(list(zip(name,age,sex)))
# people = [
#     {'nane':'jiang','age':18,'xingbie':'man'},
#     {'nane':'jian','age':17,'xingbie':'man'},
#     {'nane':'jia','age':13,'xingbie':'man'},
#     {'nane':'ji','age':11,'xingbie':'man'},
# ]
# # _people = {'age1':17,'age2':16,'age3':12,'age4':19}
# a = min(people,key=lambda dic:dic['age'])
# print(a)

#max 同上用法

# round(number,ndigits = N) 四舍五入  number 为输入的数字，ndigits保留小数，默认为0
# a = round(7.3678)
# print(a)

#slice(start,stop,step) 切片操作
# a = slice(1,5,2)
# b = [1,2,3,4,5,6,7,8]
# print(b[a])



# a = ['agedd','agg','bged']
# print(min(a))

# sum(*args, **kwargs) 传入最多2个参数,第一个为可迭代的,第二个默认参数(默认为0)
# a = [1,2,3,4]
# x = sum(a,10)     #for 循环a列表中的数字,全部加起来,在加上默认参数
# print(x)

