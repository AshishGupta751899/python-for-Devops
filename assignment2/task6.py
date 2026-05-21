# Task: Bank Loan Approval System
# ● Objective: You have to create a javascript script that checks whether an user is
# eligible for a bank loan based on various criteria.
# ● Hints:
# ○ The applicant's age must be between 18 and 60 years.
# ○ The applicant's monthly income must be greater than or equal to ₹25000.
# ○ The applicant's credit score must be greater than or equal to 700.
# ○ The applicant must not have any outstanding debts greater than ₹10000
# 1. Output:
# ○ Display "Loan Approved" if the applicant meets all the conditions.
# ○ Otherwise display "Loan Rejected"

age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))   
credit_score = int(input("Enter your credit score: "))
outstanding_debts = float(input("Enter your outstanding debts: "))
if 18 <= age <= 60 and monthly_income >= 25000 and credit_score >= 700 and outstanding_debts <= 10000:
    print("Loan Approved")  
else:
    print("Loan Rejected")
