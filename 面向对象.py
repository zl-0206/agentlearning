class Student:
    name=None    #后使用init时此处定义可以不用写
    gender=None
    nationality=None
    native_place=None
    age=None
    def hi(self):
        print(f"姓名：{self.name},年龄{self.age}")
    def hi2(self,msg):
        print(f"我是{self.name},{msg}")
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel



stu1=Student('li',13,1414144)
stu1.name='li'
stu1.gender='female'
stu1.nationality='china'
stu1.native_place='guangdong'
stu1.age=18
stu1.hi2("无敌了")

# class clock:
#     id=None
#     price=None
#
#     #def ring(self):
#         #import winsound
# #         #winsound.Beep(2000,3000)
#
# clock1=clock()
# clock1.id=313
# clock1.price=255
# clock1.ring()


