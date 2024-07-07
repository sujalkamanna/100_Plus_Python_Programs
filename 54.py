# Program 54
#Write a Python program to find N largest elements from a list.

list1 = [465,465,4,6,5,56,8654,89,546,3]
print("the length of list is :",len(list1))

largest = int(input("enter no of largest elements you want:"))
sorted = list1.sort(reverse=True)

list1.sort(reverse=True)
largest_elements = list1[:largest]
print(f"sorted elements is {largest_elements}")