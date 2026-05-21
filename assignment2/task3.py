#  Task: Retirement Age Calculator
# ● Objective: Write a program that prompts the user for their age and tells them how
# many years until they reach retirement age (65).
# ● Hints:
# ○ Ask the user to input their age.
# ○ Calculate how many more years they have until they reach 65 years of
# age.
# ○ Display the number of years left until retirement or a message if the user
# has already reached retirement age.

age = int(input("Enter your age: "))
retirement_age = 65
if age < retirement_age:
    years_until_retirement = retirement_age - age
    print(f"You have {years_until_retirement} years until you reach retirement age.")
elif age == retirement_age:
    print("Congratulations! You have reached retirement age.")
else:
    print("You have already reached retirement age.")
