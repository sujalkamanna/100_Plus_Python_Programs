# Program 26
# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

print('''
 _____________________
|  _________________  |
| |HAPPY CALCULATION| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
      ''')
while True:
    int_1 = float(input("Enter first no:"))
    int_2 = float(input("Enter second no:"))
    print("1.Addition")
    print("2.Substration")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choices = int(input("Enter your choice:"))

    match(choices):
        case 1:
            print("The addition of two no is :", int_1+int_2)
        case 2:
            print("The Substraction of two no is :", int_1-int_2)
        case 3:
            print("The multiplication of two no is :", int_1*int_2)
        case 4:
            print("The division of two no is :", int_1/int_2)
        case 5:
            break
            print("Exit")
