#该模块可以把一个类型，如数字，转成固定长度的bytes
import struct  #结构体

a = 1737886677
res1 = struct.pack('i',a)   #可以将数字转化成固定字节的bytes,'i'代表的是4个字节
print(res1)
(res2,) = struct.unpack('i',res1) #unpack,将字节转化为一个touple,元组的第一个元素就是数字了
print(res2)












