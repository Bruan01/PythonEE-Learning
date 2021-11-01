print ("hello!")
x=100
while x<1000:
    a=(x%10)
    b=(x//10%10)
    c=(x//100)
    if(a**3+b**3+c**3==x):
        print("水仙数是："+ str(x) )
    x += 1
