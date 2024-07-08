# Program 60
# Write a Python program to find words which are greater than given length k

list1 = ["apple", "banana", "pineapple", "grapes", "figs", "friuts",]

k = 5

for i in list1:
    if len(i) > k:
        print(i)
