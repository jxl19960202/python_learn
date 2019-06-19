#python3 中的是新式类  可以通过查看MRO列表,解析继承的顺序  (python2中的新式类 class 类名(object))

class A:
    def text(self):
        print('a')

class B(A):
    # def text(self):
    #     print('b')
    pass
class C(B):
    # def text(self):
    #     print('C')
    pass
class D(A):
    # def text(self):
    #     print('d')
    pass

class E(D):
    # def text(self):
    #     print('E')
    pass

class F(C,E):
    # def text(self):
    #     print('F')
    pass
F1 = F()
F1.text()
print(F.__mro__)   #通过查看__mro__ 查看继承中的顺序




