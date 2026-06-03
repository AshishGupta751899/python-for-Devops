#.Write a Python program that allows the user to search for a character within given string.
string=input("enter a string:")
character=input("enter a character to search:")
# for i in range(len(string)):

for character in string:
    if character in string:
        print("character found")
        break
else:
    print("character not found")
    