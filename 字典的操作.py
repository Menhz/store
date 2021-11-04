




#     一般不会去打印键，固定且不可重复
#               值是任意类型
#     键不能是列表、字典、集合，”“str
dict={"Z":{"A":1,},"L":"2"}
#首先字典是键值对形式，只能通过键来获取值
#打印字典：
#print(dict["键"]["A"])
#添加一对
# dict["键"]="2"
# dict.update({"P":{"A":1,}})
# c=dict.pop("B")#列表的pop弹出 ，dict.pop也是弹出的是值，同时要填入数据
# dict.popitem()#删除最后一个
for i in dict:
    print(i,dict[i])
# for i,x in dict.items():
#     print(i,x)
# print(dict)

