#import time   #调用time模块
#time.sleep(secs)   
#使用time模块下面的sleep()函数，括号里填的是间隔的秒数（seconds，简称secs）
#time.sleep(1.5)就表示停留1.5秒再运行后续代码

#import random 
#调用random模块，与
#a = random.randint(1,100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
#print(a)

import time,random

player_victory = 0
enemy_victory = 0

for i in range(1,4):
    time.sleep(2)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第'+str(i)+'局——————')  # 作为局的标记
 
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)

    # 展示双方角色的属性
    print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量'+str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量'+str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    #打印最终战果
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

if player_victory > enemy_victory :
    time.sleep(1)
    print('【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('【最终结果：你输了！】')
else: 
    print('【最终结果：平局！】')
    
    #a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')  # 在 while True 循环中设置跳出条件。
    #if a1 == 'n':
        #break    

#所以，为了更方便地实现不同数据类型的拼接，用【格式符%】是更常用更便利的一种方式。
#我们可以把%想象成：图书馆里用来占位的一本书。先占一个位置，之后再填上实际的变量。举个例子：下面这两种写法是相同的，请你着重研究下第二行的语法。
#print('血量：'+str(player_life)+' 攻击：'+str(player_attack))
#print('血量：%s 攻击：%s' % (player_life,player_attack))

lucky = 8
print('我的幸运数字是%d' % lucky)
print('我的幸运数字是%d' % 8)
print('我的幸运数字是%s' % '小龙女的生日816')
print('我的幸运数字是%d和%d' % (8,16))

#________________________________
# 只有这种情况下用的 %d %s 是一样的

print('我的幸运数字是%d' % 8)  #8以整数展示
print('我的幸运数字是%s' % 8)  #8以字符串展示

print(8) #整数8与字符串'8'打印出来的结果是一样的
print('8')

# format()函数是从 Python2.6 起新增的一种格式化字符串的函数，功能比课堂上提到的方式更强大。
# format()函数用来占位的是大括号{}，不用区分类型码（%+类型码）。
# 具体的语法是：'str.format()'，而不是课堂上提到的'str % ()'。
# 而且，它对后面数据的引用更灵活，不限次数，也可指定对应关系。

#例如 print('敌人发起了攻击，【玩家】剩余血量{}'.format(player_life))
#print 一共三种
print("a"+'b')
print("%s",'jib')
print("{}".format("我是傻逼"))