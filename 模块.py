#[from 模块名] import[模块|类|变量|函数|*][as 别名]
#import time
#print(1)
#time.sleep(5)
  #5s
#print(5)

from time import sleep
print(6)
sleep(2)
print(4)

#*表示全部
from time import*
#此时可以直接sleep()而不需要time.sleep()


import time as t
print(2)
t.sleep(1)
print(3)

from time import sleep as sl
print(2)
sl(2)
print(4)



########自定义模块########

#做调试需要加
if __name__ == '__main__':
