#coding=utf-8
s_str="hello world"
print (s_str.find('e')) #if can find 'e',return it is keys
print(s_str.find('l'))
print(s_str.find('k'))
print(s_str.find('e',2)) #start on 2,include 2
print(s_str.find('e',1,5)) #start on 1 and end on 5,just include 1  如果找不到就返回负一