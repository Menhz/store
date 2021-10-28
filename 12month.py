import pandas as pd
import xlrd
data=xlrd.open_workbook("12月份衣服销售数据.xlsx")
sheet=data.sheet_by_index(0)
for row_index in range(sheet.nrows):
    print(sheet.row_values(row_index))

def pingzhong():
    df = pd.read_excel("12月份衣服销售数据.xlsx", usecols=[1],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result


def jiage():
    df = pd.read_excel("12月份衣服销售数据.xlsx", usecols=[2],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result1 = []
    for s_li in df_li:
        result1.append(s_li[0])
    return result1

def kuchun():
    df = pd.read_excel("12月份衣服销售数据.xlsx", usecols=[3],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result2 = []
    for s_li in df_li:
        result2.append(s_li[0])
    return result2

def days():
    df = pd.read_excel("12月份衣服销售数据.xlsx", usecols=[4],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result3 = []
    for s_li in df_li:
        result3.append(s_li[0])
    return result3



if __name__ == '__main__':
    pingzhong()
    jiage()
    kuchun()
    days()

list_pingzhong=pingzhong()
list_jiage=jiage()
list_kuchun=kuchun()
list_days=days()

i = 0
sum = 0
while i<30:
    sum = sum + list_jiage[i] * list_days[i]
    i+=1

i2=0
sum2=0
while i2<30:
    sum2 = sum2 + list_days[i2]
    i2 += 1

x , y = 0,0
q1,q2,q3,q4,q5,q6=0,0,0,0,0,0
while y<30:
    if list_pingzhong[y] == "羽绒服":
        q1 = q1 + list_days[y]
    elif list_pingzhong[y] == "牛仔裤":
        q2 = q2 + list_days[y]
    elif list_pingzhong[y] == "风衣":
        q3 = q3 + list_days[y]
    elif list_pingzhong[y] == "皮草":
        q4 = q4 + list_days[y]
    elif list_pingzhong[y] == "T血":
        q5 = q5 + list_days[y]
    elif list_pingzhong[y] == "衬衫":
        q6 = q6 + list_days[y]
    y+=1
q = q1 + q2 + q3 + q4 + q5 + q6
m1 = '%.2f%%'%(q1/q*100)
m2 = '%.2f%%'%(q2/q*100)
m3 = '%.2f%%'%(q3/q*100)
m4 = '%.2f%%'%(q4/q*100)
m5 = '%.2f%%'%(q5/q*100)
m6 = '%.2f%%'%(q6/q*100)

print('_'*30)
print('销售总额为','%.2f'%sum)
print('~'*30)
print('平均每日销售量为','%.2f'%(sum2/30))
print('~'*30)
print('羽绒服的销售百分比为',m1)
print('牛仔裤的销售百分比为',m2)
print('风衣的销售百分比为',m3)
print('皮草的销售百分比为',m4)
print('T血的销售百分比为',m5)
print('衬衫的销售百分比为',m6)