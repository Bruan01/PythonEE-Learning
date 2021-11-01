import math

# 为函数设置了三个参数，并都带有默认参数）
def estimated(size=1,number=None,time=None):
    # 人力计算：如果参数中填了时间，没填人数，就计算人力
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    # 工时计算：如果参数中填了人数，没填时间，就计算工时
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

# 调用函数的时候，传递两个参数，会自动计算出第三个参数
estimated(size=1.5,number=2)
estimated(size=0.5,time=20.0)
#--------------------------------------------------------------
import math

def estimated(size=1,number=None,time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

def myinput():
choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
if choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = None
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size,number,time)
elif choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    time = None
    estimated(size,number,time)

    # 主函数
def main():
    myinput()
    estimated()

# 调用主函数
main()

#---------------------------------------------

import math

# 采集信息的函数
def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
        # 这里返回的是一个元组
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time
        # 这里返回的数据是一个元组

# 完成计算的函数
def estimated(my_input):
    # 把元组中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number)) 
    # 工时计算
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

def again():
    global key=1
    a=input("你是否想继续下去？是的话请输入1")
    if a!=1:
        key=0
# 主函数
def main():
    print("欢迎使用计算器")
    while key==1:
        my_input = myinput()
        estimated(my_input)
        again()
    print("程序已退出")    
# 调用主函数
main()

#--------------------------------------------
#出拳游戏
import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
elif (user_choice == '石头' and computer_choice == '剪刀') or (user_choice == '剪刀' and computer_choice == '布') or (user_choice == '布' and computer_choice == '石头'):
    print('你赢了！')
else:
    print('你输了！')