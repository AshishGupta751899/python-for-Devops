#Write a Python program to find the greatest character from the string "python".
string="python"
greatest=string[0]
for i in string:
    if i>greatest:
        greatest=i
print("the greatest character is",greatest)
