set={"wo","men","de","wei","lai","lai","de"}
print(f"这个类型是{type(set)},输出为{set}")
#不可重复，顺序无法控制
set.add("L")
set.add("wo")
print(set)
set.remove("L")
print(set)
pop=set.pop( )
print(f"去除的是{pop},最终为{set}")
set.clear()
print(set)
#显示差集
set1={1,2,3}
set2={1,4,5}
set3=set1.difference(set2)
print(set3)
#删除相同元素
set1.difference_update(set2)
print(set1)
#合并
set3=set1.union(set2)
print(set3)
#统计
set1={1,2,3,4,5,1}
num=len(set1)
print(num)
#遍历
set1={1,2,3,4,5,6,7,8,9}
for i in set1:
    print(i)

