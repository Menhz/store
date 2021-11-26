from threading import Thread
import time

kep = 0  # 蛋糕篮子（全剧变量）


class chef(Thread):  # 定义一个厨师类
    chef_name = ''
    kep_sum = 0

    def run(self) -> None:  # 重构run方法
        global kep  # 调用全局变量 kep
        start = time.time()  # 获取开始时间
        while True:
            end = time.time()  # 获取结束时间
            if (end - start) < 60:  # 判断前后时间差是否在一分钟内
                if kep < 500:  # 判断篮子里蛋挞个数：500以内
                    self.kep_sum = self.kep_sum + 1  # 厨师做蛋挞的个数
                    kep = kep + 1  # 篮子内蛋挞个数
                else:  # 500以上停留三秒
                    time.sleep(3)
            else:  # 大于一分钟结束执行
                break
        return self.kep_sum  # 返回做蛋挞的个数


class client(Thread):  # 定义顾客类
    client_name = ''  # 顾客名字
    money = 5000.0  # 顾客余额
    egg = 0  # 购买个数

    def run(self) -> None:  # 重构run方法
        global kep  # 调用全局变量
        start = time.time()  # 记录开始时间
        while True:
            end = time.time()  # 记录结束时间
            if end - start < 60:  # 判断时间
                if kep > 0:  # 判断篮子里蛋挞个数：不为空
                    if self.money >= 3:  # 判断顾客余额
                        self.money = self.money - 3  # 余额计算
                        kep = kep - 1  # 篮子内蛋挞个数
                        self.egg = self.egg + 1  # 购买蛋挞个数
                    else:  # 余额不足结束
                        break

                else:  # 篮子为空等待2秒
                    time.sleep(2)

            else:  # 大于60秒结束
                break
        print(self.client_name, '一共做了抢了', self.egg, '个蛋挞')
        return self.egg


'''调用厨师类'''
chef1 = chef()
chef1.chef_name = '厨师1'

chef2 = chef()
chef2.chef_name = '厨师2'

chef3 = chef()
chef3.chef_name = '厨师3'

'''调用顾客类'''
client1 = client()
client1.client_name = '顾客1'

client2 = client()
client2.client_name = '顾客2'

client3 = client()
client3.client_name = '顾客3'

client4 = client()
client4.client_name = '顾客4'

client5 = client()
client5.client_name = '顾客5'

client6 = client()
client6.client_name = '顾客6'

'''运行线程'''
chef1.start()
chef2.start()
chef3.start()
client1.start()
client2.start()
client3.start()
client4.start()
client5.start()
client6.start()
'''闭塞线程'''
chef1.join()
chef2.join()
chef3.join()
client1.join()
client2.join()
client3.join()
client4.join()
client5.join()
client6.join()
'''会计结算'''
print(chef1.chef_name, '一共做了', chef1.kep_sum, '个蛋挞', '工资', chef1.kep_sum * 1.5)
print(chef2.chef_name, '一共做了', chef2.kep_sum, '个蛋挞', '工资', chef2.kep_sum * 1.5)
print(chef3.chef_name, '一共做了', chef3.kep_sum, '个蛋挞', '工资', chef3.kep_sum * 1.5)
