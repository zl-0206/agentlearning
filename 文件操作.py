#open(name,mode,encoding)
import time
'''

name:目标文件名的字符串
mode：设置打开模式
encoding：编码格式
事例：
f=open('python,txt','r',encoding="UTF-8")
'''
#注意指针冲突
f=open("D:/cs.txt","r",encoding="UTF-8")
'''
print(type(f))
print(f.read(2))
print("------")
print(f.read())
lines=f.readlines()
print(type(lines))
print(lines)
'''
#逐行读取
one=f.readline()
print(one)
print(6666)
for line in f:
    print(line)

f.close()
#time.sleep(100)


#执行完后自动关闭文件
with open("D:/cs.txt","r",encoding="UTF-8")as f:
    print('-------')
    one = f.read()
    print(one)




'''
课后习题
'''
with open("D:/cs.txt","r",encoding="UTF-8")as f:
    print('课后习题')
    nei=f.read()
    count=nei.count('d')
    print(count)
