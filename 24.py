# Program 24
# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

no = int(input("Enter a no:"))


def binary(no):
   return bin(no)


def octal(no):
    return oct(no)


def hexa(no):
    return hex(no)


options = int(input(
    "Enter your choice \n1.Decimal to Binary\n2.Decimal to Octal\n3.Decimal to Hexadecilal: "))

if options == 1:
    print("binary no is :",binary(no))
elif options == 2:
    print("The octal no is:",octal(no))    
elif options == 3:
    print("The octal no is:",hex(no))
else:
    print("invalid choice!")        