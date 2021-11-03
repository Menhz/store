# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]

# 统计每个人的平均薪资
com_sum = 0
for com in range(0, len(names)):
    com_sum += names[com][5]
com_mean = com_sum / len(names)

print('公司的平均薪资水平为%s' % com_mean)
print('*'*30)

# 统计每个人的平均年龄
names_age = 0
for names_age_i in range(0, len(names)):
    names_age += int(names[names_age_i][1])
names_age_mean = names_age / len(names)

print('每个人的平均年龄%s' % names_age_mean)
print('*'*30)


# 公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
a = ['刘备', '45', '男', '220', 'alibaba', 500, '30']
names.append(a)
print(names)
print('*'*30)


# 统计公司男女人数
sex = 0
woman ,man = 0,0
for names_sex in range(0,len(names)):
    if names[names_sex][2] == '男':
        man +=1
    else:
        woman += 1
print('女生的人数为%s,男生的人数为%s'%(woman,man))
print('*'*30)


#每个部门的人数
import pandas as pd
depar_list = []
for depar in range(0,len(names)):
    depar_list.append(names[depar][6])
names_department = pd.value_counts(depar_list)
print('各部门统计人数如下')
print(names_department)
