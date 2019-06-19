def triangle():
    _list, new_list = [], []
    while True:
        length = len(_list)
        if length == 0:
            new_list.append(1)
        else:
            for times in range(length + 1):
                if times == 0:
                    new_list.append(1)
                elif times == length:
                    new_list.append(1)
                else:
                    temp = _list[times - 1] + _list[times]
                    new_list.append(temp)
        yield new_list #返回值，然后挂起函数，等待下一次调用
        _list = new_list.copy()#调用后会继续执行下去
        new_list.clear()

n = 0
for result in triangle():
    n += 1
    print(result)
    if n == 10:
        break