#Write a Python program to calculate the product of numbers between a starting
#and ending point provided by the user.

num1=int(input("enter starting point"))
num2=int(input("enter ending point"))
num=1
for i in range(num1+1,num2):
    num=num*i
print("multiple is",num)