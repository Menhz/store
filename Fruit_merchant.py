info = {
    '苹果': 32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
fruit_c = input('请输入水果')
if fruit_c in info.keys():
    print(fruit_c, info[fruit_c])
else:
    print('未查询到')

Friuts = {
    '苹果': 12.3,  # 水果和单价
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8
}

info_name = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 0
    }
}

d = 0
Friuts_money = list(Friuts.values())

for name_ in info_name.keys():
    c = 0
    for a in Friuts.keys():
        b = info_name[name_]['fruits'].get(a, -1)
        if b == -1:
            continue
        else:
            c = c + b * Friuts_money[d]
            d += 1
    info_name[name_]['money'] = c
print(info_name)
