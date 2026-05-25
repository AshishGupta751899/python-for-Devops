4#. Write a Python program to check if a number provided by the user is prime or not.
num=int(input("enter a number"))
for i in range(1,num+1):
    if num%1==0 and num%num==0:
        print("number is prime")
    else:
        print("number is not prime")
        