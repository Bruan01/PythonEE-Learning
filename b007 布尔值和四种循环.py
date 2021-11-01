#while True:
    #print('while True')

#------------------------------------    
password = input('请输入密码：')

if password == 'abc':
    print('密码正确！')
else:
    print('密码错误！')

# and # or # in # not in
    #运行结果会是什么你应该很清楚啦，看看就好~
dict = {'法国':'巴黎','日本':'东京','中国':'北京'}
a = '法国'

print(bool(a in dict))

#简化
i = 1
while i<101 :
   print('把这句话打印100遍')
   i = i+1
#-----------
i = 100
while i:
   print('把这句话打印100遍')
   i = i-1
#----------------
for i in range(5):
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        break # 结束循环
#========================
while True:
    p = input('请输入你的密码:')
    if p == '小龙女':
        break
print('通过啦')
#--------------------------
# continue语句搭配for循环
for i in range(5):
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')

# continue语句搭配while循环
i = 0
while i<5:
    print('明日复明日')
    i = i+1
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')
#---------------------------------
while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
    if q1 != '黑暗的冰窖':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？')
    if q2 != '梦姑':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？')
    if q3 == '不知道':
        break
print('都答对了，你是虚竹。')
#------------------------------
#pass语句,直接跳过，就算不是循环选择也可以
#请你运行代码体验一下

a = int(input('请输入一个整数:'))
if a >= 100:
    pass
else:
    print('你输入了一个小于100的数字')

#最后一种else语句，我们在条件判断语句见过【else】
#其实，else不但可以和if配合使用，它还能跟for循环和while循环配合使用。
for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')    
        break
else:
    print('5次循环你都错过了，else语句生效了。')
#-----------------------------
# 把之前这段for循环的代码改成while循环，要求运行效果相同
i =1
while i<=5 :
    
    a = int(input('请输入0结束循环，你有5次机会:'))
    i=i+1
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')    
        break
else:
    print('5次循环你都错过了，else语句生效了。')
#--------------------------
#for ... else ...
#当循环中没有碰到break语句，就会执行循环后面的else语句，否则就不会执行。

secret = 24
for i in range(3):
    guess = input('guess which number is my secret:')
    if  int(guess) ==secret:
        print('正确！你很棒哦。')  #输出结果
        break
    elif int(guess)>secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')
else:
    print('给你3次机会都猜不到，你失败了。')
#----------------------------
#囚徒问题
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了')                            
        
    else:
        print('别捣乱，只能回答“认罪”或“不认”！')
        break
#-----------------------
# 需要的变量放到开头，明显一些。
n = 0
list_answer = []

while True:
    n += 1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a,b])
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

print('第' + str(n) + '对实验者选了最优解。')

for i in range(n):
    print('第' + str(i+1) + '对实验者的选择是：' + str(list_answer[i]))
# 打印是第几对实验者做出了最优选择。


# 通过循环打印每一对实验者的选择。

#-------------------------------------------