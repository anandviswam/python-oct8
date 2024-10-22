#author:anand v
#date:22/10/2024
#aim:to convert temprature value back and forth between celcius and farenheit.
tempr = float(input("enter the temprature"))
c_or_f=input("enter if temprature is in celsius(C) or fahrenheit(F)")
c_to_f=((9/5*tempr)-32)
f_to_c=(5/9*(tempr-32))

if(c_or_f== "c" or c_or_f == "C"):
    print(tempr,"celsius is",c_to_f,"fahrenheit")
else:
    print(tempr,"fahrenheit is ",f_to_c,"celsius" )

