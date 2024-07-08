# Program 61
# Write a Python program for removing 𝑖 character from a string.

string = input("enter the string:")
length = len(string)

print("the string is:")
for index, char in enumerate(string):
    print(f"[{index}]: {char}")


remove = 0

def rem():
    global remove
    remove = int(input("enter char no you want to remove:"))


rem()
string = string.replace(string[remove], "")
print(string)
