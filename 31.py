#Program 31
# Write a Python Program for cube sum of first n natural numbers
no = int(input("enter no to print cubes:"))

sum = 0
for i in range(1,no+1):
    sum = sum+i**3
print(f"sum of cubes of first {no} natural number is {sum}")