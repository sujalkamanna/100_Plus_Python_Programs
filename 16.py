# Program 16
# Write a Python Program to Find the Factorial of a Number

fact = int(input("Enter a no to factorial:"))

if fact ==0 or fact ==1:
    print("the factorial of given no is :1",)
elif fact <0:
    print("please enter a positive value!")
    raise ValueError
else :
    for i in range(1,fact):
        fact = fact*i
    print("the factorial of given no is :",fact)


