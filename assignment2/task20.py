# Library Charge Calculation
# ○ Task: Write a program to calculate the library charges based on the number of
# days a book has been borrowed.
# ○ Charge Criteria:
# ■ Up to 5 days: ₹2/day.
# ■ 6 to 10 days: ₹3/day.
# ■ 11 to 15 days: ₹4/day.
# ■ More than 15 days: ₹5/day.
# ○ Output: Display the total charges.

days_borrowed = int(input("Enter the number of days the book has been borrowed: "))
if days_borrowed <= 5:
    charge = days_borrowed * 2
elif 6 <= days_borrowed <= 10:
    charge = days_borrowed * 3
elif 11 <= days_borrowed <= 15:
    charge = days_borrowed * 4
else:
    charge = days_borrowed * 5
print(f"Total Library Charges: ₹{charge}")
