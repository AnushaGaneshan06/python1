# Python Input & Strings Questions:

# ======================================================================================================================
# Write a Python program that asks the user to enter a string, and then prints out whether the string is a palindrome (i.e. the same forwards and backwards).

string = input("Enter the string : ")

reverse_string = string[:-1]

if string == reverse_string:
    print("The string is the palindrome!")
else:
    print("The string is not the palindrome!!")





