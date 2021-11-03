city_list = ['北京', '上海', '广东']
city_list.append('武汉')
city_list.append('石家庄')
city_list.append('济南')
city_list.append('呼和浩特')
city_list.append('拉萨')
city_list.append('成都')
city_list.append('天津')

city_1 = city_list.pop(2)
city_list.insert(1, city_1)

GDP_list = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
sum_1=GDP_list[0]+GDP_list[1]
sum, mean = 0, 0
for i in range(0, len(GDP_list)):
    sum = sum + GDP_list[i]
mean = sum / len(GDP_list)

print(city_list)
print('前八的GDP总值是:%s\n平均值是%s' % ('%.2f'%sum, '%.2f'%mean))
