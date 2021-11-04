dict = {"k1":"v1","k2":"v2","k3":"v3"}

print('所有的key')
for keys_all in dict.keys():
    print(keys_all)

print('*'*30)

print('所有的value')
for values_all in dict.values():
    print(values_all)

dict['k4'] = 'v4'

print(dict)