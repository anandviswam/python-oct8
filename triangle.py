def right_triangle(a,b,c):
    if a^2+b^2==c^2:
        print("It is right triangle")
    else:
        print("It is not right triangle")

one_side=int(input("Enter the length of first side"))
second_side=int(input("Enter the length of second side"))
third_side=int(input("Enter the length of third side"))
right_triangle(one_side,second_side,third_side)r