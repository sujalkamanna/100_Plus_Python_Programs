# Program 49
#Write a Python program to find sum of elements in list

list1 = [1,2,3,4,5,6,7,8,9,10]

def add():
    sum = 0
    for i in list1:
        sum = sum+i
    print(sum)
add()

sum = sum(map(int , list1))
print(sum)