i = 3
while 1 :
    i-=1
    user = input('user')
    password = input('password')
    if user == 'root' and password == 'admin':
        print('正确')
    else:
        print('密码输入错误，还有%d次机会'%i)
    if i <= 0:
        print('账户锁定')
        break