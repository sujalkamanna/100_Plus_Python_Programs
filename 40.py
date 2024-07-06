# Program 40
# Write a Python Program to Sort Words in Alphabetic Order.

str = (input("Enter words:"))

lower_case = str.split()
print(lower_case)
lower_case.sort()
print("the sorted words are:")
for i in lower_case:
    print(i)
