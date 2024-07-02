# Program 10
# Write a Python program to swap two variables without temp variable.

a = int(input("enter first no:"))
b = int(input("enter second no:"))
a,b = b,a
print(f"two nos before swap are {a,b} and after swapping are {b,a}")