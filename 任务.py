"""
孩子要回家
定位值，获取值进行计算

"""
dict={"中国":{"北京":{"昌平":{"沙河":{"北科院":"汉科软"}}}},
      "俄罗斯":{"拉斯维加斯":{"弗罗里达":{"午托":{"北路":"大加"}}}}}
a=input('请输入起始地')
stat_list = list(dict.keys())
city_list = list(dict.values())
if a in stat_list:
    b = stat_list.index(a)
    dict1= city_list[b]
    while True:
        dict1 = list(dict1.values())[0]
        print(dict1)
        if type(dict1) == type('w'):
            print('小朋友的家是%s'%dict1)
            break
else:
    print('未查找到信息')
