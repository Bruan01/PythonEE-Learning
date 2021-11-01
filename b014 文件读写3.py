# -*- coding:utf-8 -*-
"""
By：Bruan- 86178
Date: 2021-07-31 
"""
file_name = '../book.txt'
with open(file_name,'w') as file_object:
    file_object.write("I like coding! \n")
    file_object.write("I like coding! \n")

with open(file_name,'a') as file_object:
    file_object.write("adding context! \n")

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")