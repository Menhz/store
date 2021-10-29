'''
使用while循环实现NxN乘法表的打印。
'''
N = int(input('请输入乘法表的层数'))
i = 1
while i <= N:
    j=1
    while j<=i:
        print('%d*%d=%d\t' %(j, i, i*j),end=(''))
        j+=1
    print('')
    i+=1
print('')
