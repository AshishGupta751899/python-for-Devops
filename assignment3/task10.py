#Write a Python program to display all letters except 'm' and 'i' from the string
#"Dreamer infotech".
string="Dreamer infotech"
for i in string:
    if i=='m' or i=='i':
        continue
    print(i, end=" ")
