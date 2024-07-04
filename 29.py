# Program 29
# Write a Python Program to calculate your Body Mass Index.

height = float(input("enter height of person(m):"))

weight = float(input("Enter weight of person:(kg):"))

BMI = weight/(height*height)
print(f"BMI is :{BMI:.2f}")

if BMI <= 18.5:
 print("You are underweight.")
elif 18.5 < BMI <= 24.9:
 print("Your weight is normal.")
elif 25 < BMI <= 29.29:
 print("You are overweight.")
else:
 print("You are obese.")