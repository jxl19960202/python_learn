# open（‘文件所在位置+文件名’，‘对文件处理的方式（r，w，a）‘ ,encoding = '编码形式（如utf-8）'）  ‘r’只读，'r+'读写模式
# f = open('11.text','r',encoding='utf-8')     #打开文件的编码要与文件本身的编码要一致
# a = f.read()                                 #read（）将文件中的所有内容读出
# print(a)
# b = f.readable()                                #判断文件是否可以读出来，返回bool值
# print(b)
# c = f.readline()                             #一行一行的读
# print(c)
# d = f.readlines()                             #将所有的文件内容全部读出来，每一行为一个元素放在列表中
# print(d)
# f.close()
#
# ‘w’模式，当文件名不存在时，创建文件（存在时，者覆盖原文件）
# f = open('11.text','w',encoding='utf-8')
# f.write('jiang\njiang\njiang')        #'w'模式下也有writeline（），writeable（）等使用方法，与‘r’模式相似
# f.close()
#
# 'a'模式，添加模式，在文件的最后添加内容
# f = open('11.text','a',encoding='utf-8')
# f.write('jianren\n')                             #从文件中的最后处开始添加
# f.close()
#
# ‘r+’ 读写模式
# f = open('11.text','r+',encoding='utf-8')
# print(f.read())
# f.write('jiangxiaolong\njiangxiaolong\njiangxiaolong\n')  # 在‘r+’模式下，write（）是追加文件
# f.writelines(['jiangxiaolong\n','age\n','ttt'])    #writelines（），传入列表，‘\n’,元素换行
# f.close()
#
#
#
# with open('11.text','r+',encoding='utf-8') as f:     #使用with更加方便,省略了close（）
#     a = f.read()
#     print(a)
#     f.write('\nsb\n sb')
#
# 除了'r','a','w'等模式外还可以在这些模式的后面加‘b（bytes二进制）’，表示以二进制的方式读写
# 那么为什么要有‘b’呢，因为读写文件时，文件不是只有字符串串，还有图片，视频等
# f = open('11.text','rb+')     #在二进制的模式下，不能加入encoding
# a = f.read()                 #以二级制的形式读出文件内容
# print(a)
# f.write('jiang\nxiao\nlong'.encode('utf-8'))            # 要在写入的内容后面使用encode（）方法，
# f.write(bytes('jiang\nxiao\nlong',encoding='utf-8'))   #将字符串转化为二进制，也可以用bytes函数
# f.close()
#
#
# 一个小练习，给你一个文件怎么读出超大文件的最后面一行的信息
# 这里要介绍 光标（读取写从什么位置开始（从光标的位置向后操作）类似于鼠标在文件中的位置）
# seek（offset: int） offset表示向后移动的数量，int有3种类型。1（表示从0的位置开始移动），2（表示从相对位置开始移动），
# 3（表示从文件的最后开始移动）
# # f = open('11.text','r+',encoding='utf-8')
# # f.seek(9,0)   #这里要注意的是1中文字符代表3个字节，在Windows中换行代表2个字节，其他的都是一个
# # print(f.read())
# # f.close()
# 读取文件的最后一行
# f = open('11.text','rb')
# x = -3
# while True:
#     f.seek(x,2)
#     print(f.fileno())       #fileno()函数，查看当前光标所在的位置
#     date = f.readlines()
#     if len(date) > 1:
#         print(date[-1].decode(encoding='utf-8')) #decode()解码函数，将二级制解码
#         break
#     x = x -3
# f.close()












