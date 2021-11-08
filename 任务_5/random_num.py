import random
list_num = [random.randint(20,100) for i in range(1000)]
list_num_set = list(set(list_num))
dict_num = {}
for j in list_num_set:
    dict_num[j] = list_num.count(j)
print(dict_num)