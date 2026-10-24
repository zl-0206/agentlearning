#定义
#{key:value,key:value}
from typing import runtime_checkable

mydict={"nb":{1:6,
              2:66,
              3:666},
        "wudi":{4:6,
                5:66,
                6:666}
}
print(f"类型是：{type(mydict)}，内容是：{mydict}")
dict1={1:6,2:66,3:666}
print(dict1[1])
#常用操作
#1增加
my_dict={"zhoujie":1,"linjun":2,"joji":3}
print(f"字典现在为：{my_dict}")
my_dict["me"]="rich"
print(f"字典现在为：{my_dict}")
#2删减
score=my_dict.pop("linjun")
print(f"删除的为{score}字典现在为：{my_dict}")
#3清空
my_dict.clear()
print(f"字典现在为：{my_dict}")
#4获取全部keys
me={1:'rich',2:'handsome',3:'health',4:'happiness'}
print(me.keys())
keys=me.keys()
print(keys)
for i in keys:
    print(f"字典的key值是：{i}")
    print(f"字典的value值是：{me[i]}")

for i in me:
    print(f"字典的key值是：{i}")
    print(f"字典的value值是：{me[i]}")

#5统计字典数量
print(len(me))


#案例
info={
    "wangli":{"部门":"科技部",
              "工资":7000,
              "级别":1
            },
    "zhouji":{"部门":"采购部",
              "工资":3000,
              "级别":2
              },
    "linjun":{"部门":"市场部",
              "工资":5000,
              "级别":3},
    "liudeh":{"部门":"宣传部",
              "工资":4000,
              "级别":1},
    "joji":{"部门":"音乐部",
              "工资":6000,
              "级别":2}
}
for i in info:
    if info[i]["级别"]==1:
        info[i]["级别"]=2
        info[i]["工资"]+=1000
print(info)



