# coding=utf-8
s='1.hello world'
print(s)
s='2.hello\nworld'
print(s)
#s = '3.hello\u000world'
#print(s)
s='4.hello\tworld'
print(s)
s='5.hello\'world'#转译符号输出法
print(s)
s="6.hello'world"#同5
print(s)
s='7.hello"world'
print(s)
s='8.hello\"world'#同7
print(s)
s='9.hello\\world'
print(s)
s=r'10.hello\tworld'
print(s)  #原始字符串
s=""" 11.agwudguwd 
             hausdhukahwd   
           dhuaghduahd  asjhdadhjwk sdjahkdhwk """
print(s) #原始字符串原样输出

#----------------占位符输出法----------------------------
i=32
s='1.   i * i ='+str(i*i)
print(s)
s='2.   i*i={}'.format(i*i)
print(s)
s='3.   s={0}+{0}={1}'.format(i,i*i)
print(s)
s='4.   s={p0}+{p0}={p1}'.format(p0=i,p1=i*i)
print(s)
s="5.   s={0:d}+{0:d}={1:d}".format(i,i*i)#冒号规定格式
print(s)