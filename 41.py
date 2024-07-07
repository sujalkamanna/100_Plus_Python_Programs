# Program 41
# Write a Python Program to Remove Punctuation From a String.

string = input("Please enter a string:")

punctuation = ".+-*/=_()*&^%$#@!<>,?'}{[]"
string_with_no_punct = ""

for char in string:
    if char not in punctuation:
        string_with_no_punct = string_with_no_punct + char

print("String with no pucntituation = ",string_with_no_punct)
