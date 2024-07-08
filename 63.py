# Program 63
# Write a Python program to check if a given string is binary string or not

string = input("Enter string: ")

def is_binary(string):
    return all(char in '01' for char in string)

if is_binary(string):
    print(f"'{string}' is a valid binary string!")
else:
    print(f"'{string}' is not a valid binary string.")
