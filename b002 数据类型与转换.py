Chinese = '镜像世界'
English = "mirror world"
number = "666"
symbol = '''科A!@'''
mixture = '镜像世界mirror world666科A!@'

print(Chinese)
print(English)
print(number)
print(symbol)
print(mixture)
#字符串有【引号】的保护，可以和符号及其他文字类数据，譬如中文、英文随意组合。
#str int flaot

who = '我的'
action = '是'
destination = '镜像世界'
number = 153
code = '通行密码'
#print(type(who+action))#type()函数判断类型

#int()
#整数形式的字符串比如'6'和'1'，可以被int()函数强制转换。
#其次，文字形式，比如中文、火星文或者标点符号，不可以被int()函数强制转换。
#最后，小数形式的字符串，由于Python的语法规则，也不能使用int()函数强制转换。
#print(int('3.8')) error...............
#虽然浮点形式的字符串，不能使用int()函数。但浮点数是可以被int()函数强制转换的。

#float()
#float()函数也可以将整数和字符串转换为浮点类型。但同时，如果括号里面的数据是字符串类型，那这个数据一定得是数字形式。

number1 = 1
number2 = 2
unit1 = '人'
unit2 = '眼'
line1 = '我编程累'
line2 = '是bug相随'
sentence1 = '碎掉的节操满地堆'
sentence2 = '我只求今日能早归'
print(str(number1)+unit1+line1+sentence1)
print(str(number2)+unit2+line2+sentence2)

slogan = '脸黑怪我咯'
number = '7.8'
unit = '张'
sentence = '蓝票一个SSR都没有'
a ='int(number)'
print(slogan+a+unit+sentence)