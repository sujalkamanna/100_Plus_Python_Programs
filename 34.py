# Program 34
# Write a Python Program for array rotation.

arr = []


value = int(input("enter the no of elements you want to add in array:"))

for _ in range(value):
    no = int(input("Enter elements to add :"))
    arr.append(no)
print(arr)


print("the array after rotation is:",arr[::-1])