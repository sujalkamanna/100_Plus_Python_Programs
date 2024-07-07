# Program 50
# Write a Python program to Multiply all numbers in the list.

from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult = 1
for i in list1:
    mult = mult*i
print(mult)

product = reduce(lambda x , y : x*y , list1)
print(product)

 