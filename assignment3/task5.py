#Write a Python program to calculate the sum of numbers between a starting and
#ending point provided by the user.

num1=int(input("enter starting point"))
num2=int(input("enter ending point"))
num=0
for i in range (num1+1,num2,1):
    num+=i
print("sum of the number",num)