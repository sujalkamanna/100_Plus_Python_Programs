#Program 43
# Write a Python program to check if the given number is a Disarium Number
# Function to calculate the power of digits in Disarium number
def is_disarium(num):
    # Convert number to string to iterate through each digit
    str_num = str(num)
    length = len(str_num)
    sum = 0
    
    # Calculate sum of each digit raised to its own position index
    for i in range(length):
        sum += int(str_num[i]) ** (i + 1)
    
    # Check if the number is Disarium
    if sum == num:
        return True
    else:
        return False

# Input number from user
num = int(input("Enter a number: "))

# Check if the number is a Disarium number and print result
if is_disarium(num):
    print(f"{num} is a Disarium Number.")
else:
    print(f"{num} is not a Disarium Number.")
