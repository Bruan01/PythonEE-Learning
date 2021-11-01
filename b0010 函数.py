#Don't Repeat Yourself。
# 函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
#      2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
# def math(x):
# # 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
# # 规范：括号是英文括号，后面的冒号不能丢
#     y = 3*x + 5
# # 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
#     return y
# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略
def math(x):
    y = 3*x + 5
    return y
print(math(3))

# #def my_len(words):
#     counter = 0
#     for i in words:
#         counter = counter + 1
#     return counter

# a = '三根皮带，四斤大豆'
# print(my_len(a))
#等价于print(my_len('三根皮带，四斤大豆'))

#【默认参数】
def  menu(appetizer, course, dessert = '绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)

menu('话梅花生','牛肉拉面')
#因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。

#不能限定死数量，这时候【不定长参数】就能派上用场，即传递给参数的数量是可选的、不确定的。
def menu1(*barbeque):
    return barbeque

order = menu1('烤鸡翅','烤茄子','烤玉米')
#括号里的这几个值都会传递给参数barbeque

print(order)
print(type(order))#不定长的话会返回元组
#主要区别在于列表中的元素可以随时修改，但元组中的元素不可更改。

def menu2(*barbeque):
    for i in barbeque:
        print('一份烤串：' + i)

menu2('烤香肠', '烤肉丸')        
menu2('烤鸡翅', '烤茄子', '烤玉米')
#--------------------------------------
# 不定长参数可以接收任意数量的值
print('金枪鱼', '三文鱼', '鲷鱼')
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+')
# sep控制多个值之间的分隔符，默认是空格
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+', end = '=?')
# end控制打印结果的结尾，默认是换行)

#要返回多个值，只需将返回的值写在return语句后面，用英文逗号隔开即可。

import random 
#引入random模块

appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 <= money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'#返回多个值,以元组的形式

print(coupon(3))
print(coupon(6))

#我们也可以同时定义多个变量，来接收元组中的多个元素
anything,egg=coupon(7)
print(anything)
print(egg)

#当多个函数同时运行时，就涉及函数中一个非常重要的概念 —— 变量作用域。
# 第一点：一个在函数内部赋值的变量仅能在该函数内部使用（局部作用域），它们被称作【局部变量】，如cost()函数里的variable_cost。

# icon
# 第二点：在所有函数之外赋值的变量，可以在程序的任何位置使用（全局作用域），它们被称作【全局变量】，如第一行的rent。
#第一种方法最取巧：把局部变量都放在函数外，变成全局变量。还是以上面的代码为例：

rent = 3000
utilities = int(input('请输入本月的水电费用'))
food_cost = int(input('请输入本月的食材费用'))
variable_cost = utilities + food_cost 
# 以上均为全局变量
print('本月的变动成本是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

sum_cost()

#那有没有一个能在函数内修改的方法呢？这时候global语句就能派上用场了，它可以将局部变量声明为全局变量，仔细看第四行代码。

#直接 global 全局变量 


def div(num1, num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + '%'
    return percent

def warning():
    print('Error: 你确定上个月一毛钱都不赚不亏吗？')

def main():
    while True:
        num1 = float(input('请输入本月所获利润'))
        num2 = float(input('请输入上月所获利润'))
        if num2 == 0:
            warning()
        else:
            print('本月的利润增长率：' + div(num1,num2))
            break

main()


#-----------------------------
#练习 年终奖有多少？
def bonus(month):
    if month < 6:
        money = 500
        return money
    elif 6 <= month <= 12:
        money = 120 * month
        return money
    else:
        money = 180 * month
        return money

def info(name, month):
    gain = bonus(month)
    print('%s来了%s个月，获得奖金%s元' % (name, month, gain)) 

info('大聪',14)


#%f的意思是格式化字符串为浮点型，%.1f的意思是格式化字符串为浮点型，并保留1位小数。
