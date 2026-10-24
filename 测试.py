from sys import excepthook

f=open('D:/Pycharm/cs.txt','r',encoding='UTF-8')
nin=f.read()
cos=nin.count('nb')
print(cos)

f.close()

f=open('D:/Pycharm/cs.txt','r',encoding='UTF-8')
count=0
for line in f:
    line = line.strip()
    words = line.split(' ')
    print(words)
    for word in words:
        if word == "nb":
            count+=1

print(count)

f.close()



f=open("D:/try.txt","w",encoding="UTF-8")
f.write("hello")
f.close()
#文件存在，w会清空内容

f=open('D:/nb.txt','a',encoding='UTF-8')
f.write("nb")


#异常捕获
try:
    print(dk)
except NameError as e:
    print("ao,不存在哦")
    print(e)

#多个
try:
    1/0
except (NameError,ZeroDivisionError)as a:
    print("两种可能")

#全部
try:
    1/0
except Exception as s:
    print("errrror")

#异常的else和finally语法
try:
    print(666)
except:
    print("error")
else:
    print("无异常")
finally:
    print('正常与否我都执行')
    #一般加f.close()
#异常具有传递性