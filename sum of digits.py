#author:anand v
#date:15/10/24
num=int(input("enter a number"))
sum=0
while num>0:
    r=num %10
    sum=sum+r
    num=num//10
print(sum)
