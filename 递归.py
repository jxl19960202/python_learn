# 在python中的函数递归
#在递归中必须要有一个结束条件，不然会一直执行下去，会报错
# def clas(n):
#     print(n)
#     if n // 2 == 0:
#         return n
#     res = n // 2
#     clas(res)
#     print('--')
#     return  res
#
# clas(10)

#定义一个问路递归函数
person_list = ['mr','ba','ye','ol']
def _wen_lu():
    if len(person_list) == 0:
        return '没有人知道'
    person = person_list.pop(0)
    if person == 'ol':
        print('%s说的，在天上'%person)
        return '在天上'
    print('%s去找别人问'%person)
    res = _wen_lu()
    print('---')
    return res
_wen_lu()











