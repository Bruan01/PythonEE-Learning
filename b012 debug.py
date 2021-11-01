a = input('请输入密码：')
if a == '123456':#care for :
    print('通过')
#--------------------------------
    # 这是debug前的代码：
for x in range(10)：
    　print（x）　　

# 这是debug后的代码：
for x in range(10):
    print(x)  
    #---------------------
#（多行注释有两种快捷操作：1、在需要注释的多行代码块前后加一组三引号''' 
# 2、选中代码后使用快捷键操作：Windows快捷键是ctrl+/，Mac为cmd+/，适用于本地编辑器）


movie = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

name = input('你想查询哪个演员？')
for i in movie:
    actors = movie[i]
    #取出字典的值
    if name in actors:
        print(name+'出演了电影'+i)

#-----------------------------
import random

all = ['正面','反面']#牛牛
guess = ''

while guess not in all:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

toss = all[random.randint(0,1)]  #牛牛
# 随机抛硬币，all[0]取出正面，all[1]取出反面

if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，再给你一次机会。')
    guess = input('再输一次“正面”或“反面”：')
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')

#为了不让一些无关痛痒的小错影响程序的后续执行，Python给我们提供了一种异常处理的机制，可以在异常出现时即时捕获，然后内部消化掉，让程序继续运行。
#这就是try…except…语句，具体用法如下：
#不用修改代码，直接运行即可，尝试多输入几次非数字
while True:
    try:
        age = int(input('你今年几岁了？'))#此时int是限制作用
        break
    except ValueError:
        print('你输入的不是数字！')

if age < 18:
    print('不可以喝酒噢')
    
#代码要点有两个：
#1）因为不知道用户什么时候才会输入正确，所以设置while循环来接受输入，只要用户输入不是数字就会一直循环，输入了数字就break跳出循环。
#2）使用try……except……语句，当用户输错的时候会给予提示。

num = [1,2,0,3]
for x in num:
    try:
    #尝试执行下列代码
        print (6/x)
        #使用6除以num中的元素，并打印
    except ZeroDivisionError:
    #除非发生ZeroDivisionError报错，执行下列代码：
        print('0是不能做除数的！')
        #打印“0是不能做除数的！”

        #关于Python的所有报错类型，有需要的话可以在这里查阅：
        #https://www.runoob.com/python/python-exceptions.html


print('\n欢迎使用除法计算器！\n')

while True:
    try:
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x)/float(y)
        print(x,'/',y,'=',z)
        break  # 默认每次只计算一次，所以在这里写了 break。
    except ZeroDivisionError:  # 当除数为0时，跳出提示，重新输入。
        print('0是不能做除数的！')
    except ValueError:  # 当除数或被除数中有一个无法转换成浮点数时，跳出提示，重新输入。
        print('除数和被除数都应该是整值或浮点数！')
    
    # 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
    # except(ZeroDivisionError,ValueError):
    #     print('你的输入有误，请重新输入！')
    
    # 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。
    # except Exception:
    #     print('你的输入有误，请重新输入！')
            