#Write a Python program to check whether a string entered by the user is a palindrome.
string=input("enter a string:")
reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Number is Palindrome")
else:
    print("Number is not a palindrome")