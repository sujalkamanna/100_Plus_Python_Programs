# Program 57
# Write a Python program to Remove empty List from List.


list1 = [ [1,645,68,6,6,87,987,],[54],[54,78,89], []]

for i in list1:
    if i == []:
        list1.remove(i)

print(list1)