#for 
for i in [1,2,3,4,5]: #不要忘记冒号
   print(i)

for i in [1,2,3,4,5]:
    print(i)

print('事情全部办完了！现在留在空房间里的人是谁？')
print(i)

dict = {'日本':'东京','英国':'伦敦','法国':'巴黎'}

for i in dict:
    print(i)#只会打印出键

for i in '吴承恩':#字符串就可以
   print(i)

#浮点数不能算
a = '100'#已经改为字符串
b = '0.01'#已经改为字符串
for i in a:
     print(i)
for i in b:
    print(i)
print("----------------------------------------------")
#range（） using range function to produce a array between 0 and x-1
# 使用range(x)函数，就可以生成一个从0到x-1的整数序列
for i in range(3):
    print(i)

for i in range(3):
    print('我很棒')

for i in range(10):
    print("楷洪走的第"+str(i+1)+"天，想他！")

#range()的另一种用法
#range(0,10,3)的意思是：从0数到9（取头不取尾），步长为3。
for i in range(0,20,2):
    print(i)

# 用for循环完成1-100分别乘以5的计算
for i in range(1,101):#步长默认为1
    print(i*5)

d = {'小明':'醋','小红':'油','小白':'盐','小张':'米'}
for i in d:
    print(d[i])
for i in d:
    print(i)

#while
a = 0
while a < 5:
    a = a + 1
    print(a)

#man = ''  # 注：''代表空字符串
#while man != '有':  #注：!=代表不等于
    #man = input('有没有愿意为小龙女死的男人？没有的话就不能出古墓。')
#print('小龙女可以出古墓门下山啦~')

#----------------------------------------------------------

password = ''  # 变量password用来保存输入的密码
#while password != '816':
    #password = input('请尝试输入密码：')
print('欢迎回家！')

#----------------------------------------------------------
a = 0  # 定义了一个变量a
while a < 5:  # 当a小于5的时候，就自动执行后续缩进部分的语句
    print('现在a的值是：' + str(a)) #加一个print看看现在的a是多少
    a = a + 1  # 每执行一次循环，变量a的值都加1
    print('加1后a的值是：' + str(a)) #加一个print看看加1后的a是多少
print(a)
#-------------------------------------------------------------
#用for循环把诗句打印3遍
for i in range(3) :
    print('明日复明日，明日何其多。')

#用while循环把诗句打印3遍
j = 1
while j<4 :
    print ('明日何其多，明日何其多。')
    j =j+1


#我们不要 '4' 
# while 循环
n = 0
while n < 7:
    n = n+1
    if n != 4:  # 当num != 4，执行打印语句；等于4时不打印。
        print(n)

# for 循环
for num in range(1,8):  # 为同时能运行两个循环，新取参数 num。
    if num != 4:  # 当num != 4，执行打印语句；等于4时不打印。
        print(num)

#--------------------------------------------
#列表顺序移动
students = ['小明','小红','小刚']
students1=students[0]
students=students[1:]#将后面提前
print(students)
#方法一

students = ['小明','小红','小刚']
for i in range(3):
    student1 = students[0]  # 获取第一个座位的学生 student1
    students = students[1:]  # 让 student1 暂时离开，后面的学生座位都进一位。
    students.append(student1)  # 将 student1 安排到最后一个座位
    print(students)
#方法二 用我们先介绍一下列表中的pop()函数，用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
#可以将其理解为提取和删除的融合：①提取：取到元素，对列表没有影响；②删除：删除列表的元素。
#而移除，则是同时做到取到元素，并且删除列表中的元素。
print("=============================================================")
students = ['小明','小红','小刚']
print(students.pop())#删除并且记录
print(students)

print("------------------------------------------------------------")
students = ['小明','小红','小刚']
for i in range(3):
    student1=students.pop(0) 
    print(students[0])
    #这里就不用再用切片了
    students.append(student1)
    print(students)
    print(students[0])
   
