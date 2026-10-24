#默认值只可以在最后
from 序列 import result


#不定长参数
def user(*a):
    print(type(a))
    print(a)

user('tom')
user('tom',18)

#调用时要以key=value形式
def user1(**b):
    print(type(b))
    print(b)

user1(name='tom',age=2)

def test():
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x+y

test()

#匿名函数
#lambda x,y: x+y
def com(co):
    result=co(3,2)
    print(result)

com(lambda x,y:x+y)

