'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
i,num,num_max,num_sum = 0,0,0,0
while i < 10:
    i += 1
    num = int(input('请输入第%s数字'%i))
    if num > num_max:
        num_max = num
    num_sum = num_sum + num

print(num_max)
print(num_sum)
print('%.2f'%(num_sum/10))