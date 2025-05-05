#!/usr/bin/python3

first_num = int(input("Enter the first number:\n"))
sec_num = int(input("Enter the second number:\n"))

whole_nun =first_num * sec_num

if whole_nun < 0:
    print(first_num , 'x' , sec_num , "=" , whole_nun)
    print("The result is negative.")
elif whole_nun > 0:
    print(first_num , 'x' , sec_num , "=" , whole_nun)
    print("The result is positive.")
else:
    print(first_num, 'x' ,sec_num , "=" , whole_nun)
    print("The result is positive and negative.")