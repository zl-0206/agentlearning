from typing import Union

class Phone:
    IMEI=31939
    producer='wudi'
    def call_4g(self):
        print('4g')

class Phone2025(Phone):
    face=313
    producer='change'#复写
    def call_5g(self):
        print(f'父类是{super().producer}')
        print('5g')


phone=Phone2025()
print(phone.face)
print(phone.producer)
phone.call_4g()
phone.call_5g()






print('========')

#多继承
class nfc:
    nfc_type='5generation'
    producer='nb'

    def read(self):
        print('读卡')
    def write(self):
        print('写卡')

class reomte:
    rc_type='红外'

    def control(self):
        print('红外已开启')

class myphone(Phone,nfc,reomte):
    pass#空内容，无意义

phone=myphone()
phone.read()
phone.control()
print(phone.producer)#同名看括号内从左到右


#类型注解：
#定义：类型=。。。
my_list:list =[1,2,3]#或：list[int]=
my_tuple:tuple =(1,2,3)
my_dict:dict[str,int]={"age":11,'sa':31}
#函数与方法类型注解
#->是收集返回值类型
def add (x:int,y:int)->int:
    pass
    return x+y
print(add(1,2))

#Union()类型
#描述混合类型的
list1:list[Union[str,int]]=[1,2,'s','d']

def func(data:Union[int,str])->Union[str,int]:
    pass

func(12)
