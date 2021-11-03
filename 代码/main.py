list=[1,"A",2, 3, ]#代引号的全部为""str
print([[x,i] for x in range(10) for i in range(9)])#快速生成列表
#角标  0，1，2， 3，
#长度减1就是角标的最大值
#len()计算内容的长度,还可计算所有数据类型的长度
#print(len(list))
#列表的更改
# list[1]="abc"
# print(list)
#列表的删除
# pop1=list.pop()#pop弹出是可以赋值 不同于删除
# list.remove("A")#填入你要删除的内容，不是角标
# print(pop1)
#列表的写入
# list.append(1)#append默认添加到最后一个
# list.insert(1,"abc") #insert(元素1，元素2) 元素1是插入的角标 ，元素2是内容
# print(list)
#列表的读取
# print(list[0])#list[角标]，不是元素
#第一种写法
# for i in list:#结果是列表的每个内容都赋值给i
#     print(i)
#第二种写法
#   默认从0开始(0,4) range[) 实际数数是 0 ，1，2，3 【4娶不到】
# for i in  range(len(list)):
#     print(list[i])
#
# b=[]
# b.append(list.pop())
# print(b)
# index=int(input("数字"))
# for i in range(index):
#     print(" "*(index-i) ,"* "*i)