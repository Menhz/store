goods = [{"name": "电脑", "price": 1999},

         {"name": "鼠标", "price": 10},

         {"name": "显示器", "price": 120},

         {"name": "内存", "price": 230}, ]
for i in range(len(goods)):
    print(i + 1, goods[i]['name'], goods[i]['price'])

while True:
    a = input('请输入序号')
    try:
        if a == 'q' or a == 'Q':
            print('退出成功')
            break
        else:
            print(goods[int(a) - 1]['name'], goods[int(a) - 1]['price'])
    except:
        print('输入的数据有误')

