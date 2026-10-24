
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):#转换为字符串
        return f"name={self.name},age={self.age}"

    def __lt__(self, other):#比较,大于或等于
        return self.age<other.age

    def __le__(self, other):#比较，大于等于或小于等于
        return self.age<=other.age

    def __eq__(self, other):
        return self.age==other.age

student=Student('zhou',23)
print(student)
print('---------')
st1=Student('ssa',4)
st2=Student('dad',35)
print(st1>st2)
print(st1<st2)
print('---------')
st3=Student('da',6)
st4=Student('ad',6)
print(st3<=st4)
print(st3>=st4)
print('---------')
print(st3==st4)