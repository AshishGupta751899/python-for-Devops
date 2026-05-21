# Find the greatest number.
# ○ Task: Write a program to find greatest number from three number
# ○ Input: Prompt the user to enter three numbers.
# ○ Output: Display the greatest number.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:

    greatest = num2             
else:
    greatest = num3
print(f"The greatest number is: {greatest}")
