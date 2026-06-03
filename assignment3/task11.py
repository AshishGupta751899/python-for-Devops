#Write a Python program to print alternate characters from a given string
string=input("enter a string:")
for i in range(0,len(string),2):
    print(string[i], end=" ")