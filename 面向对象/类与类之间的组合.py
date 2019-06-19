#组合:类与类之间的组合,类之间没有共同的地方,但是有互相关联之处

class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

class Teacher:
    def __init__(self,name,age,gender,School):
        self.name = name
        self.age = age
        self.gender = gender
        self.school = School


class Course:
    def __init__(self,name,price,period,Teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = Teacher

s1 = School('oldboy','beijing')
s2 = School('oldboy','nanjing')

t1 = Teacher('lhf',30,'man',s1)
t2 = Teacher('alex',30,'man',s2)

c1 = Course('python',10000,'3month',t2)
print(c1.teacher.school.addr)   #将course,teacher,school3个类关联起来,采用点号的形式逐层调用












