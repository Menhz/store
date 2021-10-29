'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：给提示猜了多少次， 初始金额有1000，每猜一次 减去100 输入qorQ退出
'''
import random
money=1000
randint_num = random.randint(0, 10)
while money > 0:
    money -= 100
    num = input("请输入一个数字")
    if num == 'Q' or num == 'q':
        print('欢迎下次光临')
        break
    elif int(num) == randint_num:
        print("Ok")
        break
    elif int(num) > randint_num:
        print("你输入的过大")
    elif int(num) < randint_num:
        print("你输入的过小")
    if money<100:
        print('余额不足请充值')
    print('您的余额还有%s元'%money)
    '''
           *
            
    '''