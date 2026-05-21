# Write a javascript program to arrange three numbers in descending order.
# Input:
# Prompt the user to enter three numbers.
# Processing:
# Sort the numbers in descending order.
# Example:
# ● Enter first number: 3
# ● Enter second number: 1
# ● Enter third number: 2
# Output:
# ● Numbers in Descending Order: 3, 2, 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
numbers = [num1, num2, num3]
numbers.sort(reverse=True)
print("Numbers in Descending Order:", numbers)
    