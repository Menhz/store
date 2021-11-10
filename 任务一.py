city = {
    "北京": {
        "昌平": {
            "八达岭": ["八达岭长城"],
            "回龙观": ["永旺超市", "永辉超市", "呷哺呷哺"]
        },
        "朝阳": {
            "景观": ["玉渊潭公园"]
        },
        "海淀": {
            "高校": ["清华", "北大"],
            "公园": ["香山", "植物园"],
            "博物馆": ["军事博物馆", "国家地质公园"]
        }
    },
    "上海": {

    }
}

shoping_dict = {'食品':{'特色干果':60,'特色水果':100,'特色零食品':110},
                '纪念品':{'勋章':150,'吊坠':156,'手册':200},
                '玩偶':{'布熊':150,'布狗':100}
                }

def City(a, b):
    c = b[a]
    return c


def showCity(b):
    for a in b:
        print(a)


def citylist(a, b):
    return b[a]

def souvenir():
    for i in shoping_dict:
        print(i)
    souvenir_name = input('请输入您要购买的品种')
    list_key = list(shoping_dict[souvenir_name].keys())
    list_value = list(shoping_dict[souvenir_name].values())
    for j in list_key:
        print(j)
    souvenir_names = input('请输入您要购买的商品')
    b = list_key.index(souvenir_names)
    c = list_value[b]
    return (souvenir_name, c)


city_st = city
showCity(city)
while True:
    a = input('请输入城市')
    if a == "Q" or a == "q":
        print("欢迎下次光临")
        break
    else:
        if a not in city_st:
            print('输入错误，重新输入')
            continue
        else:
            if type(city_st[a]) == dict:
                city_st = City(a, city_st)
                showCity(city_st)
            else:
                print(citylist(a, city_st))
                print('门票1000')
                city_st = city
                souvenir_y_n = input("是否买点纪念品？请输入y or n")
                if souvenir_y_n == 'n':
                    break
                elif souvenir_y_n == 'y':
                    souvenir_list = []
                    money = int(input('请输入你的余额'))
                    while money > 60:
                        y_n = ('是否继续，继续输入是')
                        try:
                            (shoping_out, money_out) = souvenir()
                            money = money - money_out
                            souvenir_list.append(shoping_out)
                            if y_n != '是':
                                print('你当前购买的商品为', souvenir_list, '您的余额为', money)
                            else:
                                print('你当前购买的商品为', souvenir_list, '您的余额为', money, '欢迎下次光临')
                                break
                        except:
                            print('输入错误')
                            continue
                    print('你的余额不足， 你当前购买的商品为', souvenir_list, '您的余额为', money)
