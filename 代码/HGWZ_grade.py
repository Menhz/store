grade_list = [
    ['罗恩', 23, 35, 44],
    ['哈利', 60, 77, 68, 88, 90],
    ['赫敏', 97, 99, 89, 91, 95, 90],
    ['马尔福', 100, 85, 90]
]

for i in range(0, len(grade_list)):
    a = grade_list[i]
    sum = 0
    for j in range(1, len(a)):
        sum = sum + a[j]
    print('%s的总成绩是%s' % (a[0], sum))
