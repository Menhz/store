# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
list_info =['年龄','性别' ,'编号','任职公司','薪资','部门编号']
dict_info = {}
for i in names:
    dict_info[i[0]]={list_info[x]:i[1:][x] for x in range(len(list_info))}
print(dict_info)