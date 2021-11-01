
print(1)
print('我是傻逼') #两个不同print会换行
print(1+2)
print("1+2")
print("1"+"2")
print("1"+str(1))

print('''我愿意留在汤婆婆的澡堂里工作两年，
第一年在锅炉房和锅炉爷爷一起烧锅炉水，
将在这个世界变成一头猪。
''')
#a=input()
#print(6.798*float(a))

#1-001打印皮卡丘
print('''    へ　　　　　／|
　　/＼7　　　 ∠＿/
　 /　│　　 ／　／
　│　Z ＿,＜　／　　 /`ヽ
　│　　　　　ヽ　　 /　　〉
　 Y　　　　　`　 /　　/
　ｲ●　､　●　　⊂⊃〈　　/
　()　 へ　　　　|　＼〈
　　>ｰ ､_　 ィ　 │ ／／
　 / へ　　 /　ﾉ＜| ＼＼
　 ヽ_ﾉ　　(_／　 │／／
　　7　　　　　　　|／
　　＞―r￣￣`ｰ―＿''')

print('千寻你好，人们叫我\'无脸男\'\n这个世界的人都选择无视我\n只有你看到了我并和我打招呼\n我感到很孤单，很孤单\n你愿意和我成为朋友吗？\n')

#例如 print('敌人发起了攻击，【玩家】剩余血量{}'.format(player_life))
#print 一共三种
print("a"+'b')
print('%s'%'jib')
print('%s'+'jib')
print('%s','jib')
print("{}".format("我是傻逼"))
#关于换行
print('hello')
print('world')#自动换行

print('hello',end='')
print('world')

print('hello',end='  ')
print('world')

print('hello',end='!')
print('world')
#---------------------------------------
for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2),end = '  ')
print('    ') #用来换行!!!!

for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3),end = '  ')
#----------------------------------------
    print('金枪鱼', '三文鱼', '鲷鱼')
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+')
# sep控制多个值之间的分隔符，默认是空格
print('金枪鱼', '三文鱼', '鲷鱼', sep = '+', end = '=?')
# end控制打印结果的结尾，默认是换行)
