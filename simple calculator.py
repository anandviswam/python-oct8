#author:anand v
#date:10/8/24
num1=int(input("enter a number"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
print("the sum of num1 and num2 is:",num1+num2)
print("the difference when num2 is subtracted from num1 is:",num1-num2)
print("the product of num1 and num2 is:",num1*num2)
if num2==0:
    print("division by zero not possible")
else:
    div=num1/num2
    print("the quotient when num1 is divided by num2 is:",div)
print("the quotient when num1 is divided by num2:",num1/num2)
print("the reminder when num1 is divided by num2:",num1%num2)
result=(num1 + num2) * num3 /2
print("the result of (num1 +num2 *num3/2",result)