#     Write a javascript program that calculates the library charge based on the number of days a
# book has been borrowed.
# Charge Criteria:
# ● Up to 5 days: Rs. 2 per day
# ● 6 to 10 days: Rs. 3 per day
# ● 11 to 15 days: Rs. 4 per day
# ● More than 15 days: Rs. 5 per day
# Instructions:
# 1. Input: Prompt the user to enter the number of days the book has been borrowed.
# 2. Processing: Calculate the charge based on the given criteria.
# 3. Output: Display the calculated charge.

days = int(input("Enter the number of days the book has been borrowed: "))
if days <= 5:
    charge = days * 2
elif 6 <= days <= 10:
    charge = days * 3
elif 11 <= days <= 15:
    charge = days * 4
else:
    charge = days * 5

print(f"The library charge is: Rs. {charge}")

    