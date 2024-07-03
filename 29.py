# Program 29
# Write a Python Program to calculate your Body Mass Index.

height = float(input("enter height of person(m):"))

weight = float(input("Enter weight of person:(kg):"))

BMI = weight/(height*height)
print(f"BMI is :{BMI:.2f}")