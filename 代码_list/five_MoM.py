a = [1, 5, 21, 30, 15, 9, 30, 24]
five_sum = 0
for i in range(0, len(a)):
    if a[i] % 5 == 0:
        five_sum = five_sum + a[i]
print(five_sum)
