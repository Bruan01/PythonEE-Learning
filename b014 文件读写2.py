# -*- coding:utf-8 -*-
"""
By：Bruan- 86178
Date: 2021-07-31 
"""
with open(r'/pi_digits.txt') as file_name:
    contents = file_name.read()
    print(contents)

with open(r'/pi_digits.txt') as file_name1:
    for line in file_name1:
        print(line.rstrip()) ##删掉右边的空格

with open(r'/pi_digits.txt') as file_name:
    file_list = file_name.readlines() ##存储为一个列表
pi_string=' '
for line in file_list:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

##birthday = input('enter your birthday, in the from mmddyy: ')
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print('your birthday does not appears in the first million digits op pi!')

message = "i really like dogs"
message.replace('dog', 'cats')
print(message)

print("-----------------------------------------------------------------")

