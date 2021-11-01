for i in range(1,3):
    print(str(i) + ' X 2 = ' + str(i*2))

for i in range(1,4):
    #print(str(i) + ' X 3 = ' + str(i*3))  
    print("%d * 3 = %d"%(i,3*i))



print('hello',end='')
print('world')

print('hello',end='  ')
print('world')

print('hello',end='!')
print('world')

#----------------------------------
for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')
    
#---------------------
#合并列表 列表排序
list1 =  [91, 95, 97, 99]  
list2 =  [92, 93, 96, 98]
for i in list1:
    list2.append(i)
list2.sort()
print(list2)