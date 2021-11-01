# coding=utf-8
dict1={102:'张三',105:'李四',109:'王五'}
print("遍历键")
for id1 in dict1.keys():
    print('学号：'+str(id1))
print("遍历值")
for name1 in dict1.values():
    print('学生：'+name1)
print("遍历键值")
for id1,name1 in dict1.items():
    print('学号： {0}'+'学生： {1}'.format(id1,name1))        