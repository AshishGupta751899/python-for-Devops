#Write a Python program to reverse a string entered by the user.
string=input("enter a string:")
reversed_string=""
for i in string:
    reversed_string=i+reversed_string
print("the reversed string is",reversed_string)
