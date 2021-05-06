x=int(input("enter the length of fibonacci series (more than two) : "))
a=0
b=1
print(a,'\n',b)
for i in range(1,x-1,1):
    c=a+b
    print (c)
    a,b,c=b,c,0
