# Program 33
# Write a Python Program to find largest element in an array.

arr = []
value = int(input("enter the no of elements you want to add in array:"))

for _ in range(value):
    no = int(input("Enter elements to add :"))
    arr.append(no)
print(arr)

largest = max(arr)

print("the largest element in array is:",largest)