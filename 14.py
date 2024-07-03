# Program 14
# Write a Python Program to Check Prime Number.
number = int(input("enter a no :"))


for i in range(2, number):
    if number % i == 0:
        print("the no is prime")
        break
else:
    print("the no is not prime")
