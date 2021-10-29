'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a = int(input('请输入一个数'))
b = int(input('请输入一个数'))
c = int(input('请输入一个数'))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('是等边三角形')
    elif a == b or a == c or c == b:
        print('是等腰三角形')
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c ==a*a :
        print('是直角三角形')
    else:
        print('是普通三角形')
else:
    print('不可以构成三角形')