#Write a Python program to generate the Fibonacci sequence up to a specified
#number of terms.
num=int(input("Enter the number of terms: "))
a=0
b=1
if num<=0:
    print("Please enter a positive integer.")
elif num==1:
    print("Fibonacci sequence up to",num,"term:")
    print(a)
else:
    print("Fibonacci sequence up to",num,"terms:")
    print(a, b, end=" ")
    for _ in range(2, num):
        c = a + b
        print(c, end=" ")
        a = b
        b = c