#coding=utf-8//要这个才行
#直接运行代码即可
students = ['党志文', '浦欣然', '罗鸿朗', '姜信然', '居俊德', '宿鸿福', '张成和', '林景辉', '戴英华', '马鸿宝', '郑翰音', '厉和煦', '钟英纵', '卢信然', '任正真', '翟彭勃', '蒋华清', '双英朗', '金文柏', '饶永思', '堵宏盛', '濮嘉澍', '戈睿慈', '邰子默', '于斯年', '扈元驹', '厍良工', '甘锐泽', '姚兴怀', '殳英杰', '吴鸿福', '王永年', '宫锐泽', '黎兴发', '朱乐贤', '关乐童', '养永寿', '养承嗣', '贾康成', '韩修齐', '彭凯凯', '白天干', '瞿学义', '那同济', '衡星文', '公兴怀', '宫嘉熙', '牧乐邦', '温彭祖', '桂永怡']
for i in students :#注意冒号
    print(i+'在不在？')
#一个列表需要用中括号[ ]把里面的各种数据框起来，里面的每一个数据叫作“元素”。每个元素之间都要用英文逗号隔开。
#这就是列表的标准格式，现在请你创建一个列表名为list1的列表，列表里有三个元素：'小明',18,1.70，并将其打印出来：

list2 = [5,6,7,8,9]
print(list2[:])
print(list2[2:])
print(list2[:2])
print(list2[1:3])
print(list2[2:4])
#切片法 冒号左边空，就要从偏移量为0的元素开始取；右边空，就要取到列表的最后一个元素。后半句：冒号左边数字对应的元素要拿，右边的不动

#增加元素
# 请运行以下代码：报错后，可读一下报错信息，然后将第6行注释掉再运行。
list3 = [1,2]
list3.append(3)#增加元素
print(list3)

#list3.append(4,5)
list3.append([4,5])
print(list3)

#删除元素
del list2[1]#索引值
print(list2)

#字典
scores = {'小明':95,'小红':90,'小刚':90}#注意大括号，键值对，冒号
# 用len()函数来得出一个列表或者字典的长度（元素个数），括号里放列表或字典名称。
print(len(scores))
#字典中的键具备唯一性，而值可重复
#键值对覆盖
# 请你运行下面的代码：
# scores = { '小明': 95, '小红': 90, '小明': 90 } 键值对覆盖
print(scores)
#从字典中提取元素
# 请你运行下面的代码：
scores = {'小明': 95, '小红': 90, '小刚': 90}
print(scores['小明']) #也是用的中括号

#字典的删除与添加
# 直接运行下面的代码，留意字典以及新的键值对是如何增加的：
album = {'周杰伦':'七里香','王力宏':'心中的日月'}
del album['周杰伦']#跟列表差不多的方式
print(album)

album['周杰伦'] = '十一月的萧邦'#这个通过键值赋值的方式增加键值对!
print(album)
print(album['周杰伦'])

scores = {'小明':95,'小红':90,'小刚':90}
del scores['小刚']
print(scores)
scores['小刚']=92#同名的话会修改其值
scores['小美']=85
print(scores)

#字典与列表的区别
scores1 = {'小明':95,'小红':90,'小刚':100}
scores2 = {'小刚':100,'小明':95,'小红':90}
print(scores1 == scores2)#两个字典顺序换不影响，而列表就影响

#嵌套
#列表嵌套列表
students = [['小明','小红','小刚','小美'],['小强','小兰','小伟','小芳']]
print(students[1][3])
#字典嵌套字典
scores = {
    '第一组':{'小明':95,'小红':90,'小刚':100,'小美':85},
    '第二组':{'小强':99,'小兰':89,'小伟':93,'小芳':88}
    }
print(scores['第二组']['小芳'])
#列表和字典相互嵌套
# 最外层是大括号，所以是字典嵌套列表，先找到字典的键对应的列表，再判断列表中要取出元素的偏移量
students = {
    '第一组':['小明','小红','小刚','小美'],
    '第二组':['小强','小兰','小伟','小芳']
    }
print(students['第一组'][3])
#取出'第一组'对应列表偏移量为3的元素，即'小美'

# 最外层是中括号，所以是列表嵌套字典，先判断字典是列表的第几个元素，再找出要取出的值相对应的键
scores = [
    {'小明':95,'小红':90,'小刚':100,'小美':85},
    {'小强':99,'小兰':89,'小伟':93,'小芳':88}
    ]
print(scores[1]['小强'])
#先定位到列表偏移量为1的元素，即第二个字典，再取出字典里键为'小强'对应的值，即99。

#元组跟列表差不多就是是要用（）来代替【】
tuple1=("a","b")
print(tuple1[1])

#找到那只狼
townee = [
    {'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},
    '丑小鸭','坚定的锡兵','睡美人','青蛙王子',
    [{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]
    ]

print(townee[5][1]['反面角色'])

list100=[]
for i in range(1,10):
    list100.append(i**2)
print(list100)

list101 = [i**2 for i in range(1,100)]
print (list101)

cars = ['audi','bmw','subaru','toyota'] 
for i in cars:
    if i=='bmw':
        print (i.upper())
        
        
favourate_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}           
for name,language in favourate_language.items():
    print('\n'+name.title()+"'s favorite language is"+language.title()+".")
for name in favourate_language.keys():
    print("keys: "+name.title())
    print("values: "+language.title())##停留在最后name所对应的values那里
for language in favourate_language.values():
    print("keys: "+name.title())
    print("values: "+language.title()) ##停留在最后values所对应的names那里   
for name in sorted(favourate_language.keys()):
    print(name.title()+", thank you for your learning!")    
for language in set(favourate_language.values()):
    print(language.title())    

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princrton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username,user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: "+location.title())
    
    pets = ['pig','cat','dog','cat','dog']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)    
    

list_a = [1,2,3,4]
list_b = [1,6,7,8]
list_a.extend(list_b);
print(list_a)
print(set(list_a+list_b))


