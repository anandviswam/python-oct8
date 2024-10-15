age=int(input("enter your age"))
if age < 10:
    print("the entry ticket fare is 7")
elif age >= 10 and age < 60:
    print("enty ticket fare is 10")
elif age >= 60:
    print("the entry ticket fare is 5")
else:
    print("you are not eligible for ticket")

