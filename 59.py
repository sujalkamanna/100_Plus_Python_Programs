# Program 59
# Write a Python program to Count occurrences of an element in a list.

from collections import Counter
list1 = [8654, 7465, 7546, 78654, 786, 754, 78, 78, 1, 2, 2, 3, 66, 5]

for i in list1:
    print(i, "is repeated ", list1.count(i), "times")

# or

my_list = [10, 20, 10, 30, 10, 40, 50]
element_counts = Counter(my_list)
print(element_counts)
