# Program 4
# Write a Python program to swap two variables.

first = int(input("Enter the value of first variable:"))
second = int(input("Enter the value of second variable:"))

temp = first
first = second
second = temp

print(f"The value of first variable is {first}")
print(f"The value of second variable is {second}")