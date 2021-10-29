N = int(input('请输入乘法表的层数'))
for i in range(N,0,-1):
    for j in range (1,i+1):
        print('%d*%d=%d\t' %(j, i, i*j),end=(''))
    print('')
print('')