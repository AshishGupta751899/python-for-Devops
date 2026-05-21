    # Finding the Middle Number
    # ○ Task: Write a program to determine the middle number among three inputs.
    # ○ Input: Prompt the user to enter three numbers.
    # ○ Processing: Identify the middle number, which is neither the largest nor the
    # smallest.
    # ○ Output: Display the middle number.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
    middle = num2
elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
    middle = num1
else:
    middle = num3   
print(f"The middle number is: {middle}")
    