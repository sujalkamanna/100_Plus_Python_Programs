# Program 35
# Write a Python Program to Split the array and add the first part to the end?

arr = []

value = int(input("enter no of values in array:"))
for  _ in range(value):
    no = int(input("Enter elements to add :"))
    arr.append(no)


print("the original array is:",arr)
arr[0],arr[-1]= arr[-1],arr[0]
print("The final array is :",arr)