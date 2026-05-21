# Task: Salary Calculation
# ● Objective: You have to calculate an employee's salary by computing the gross
# salary tax and net salary based on the given parameters.
# ● Hints:
# ○ Base Salary = ₹50000
# ○ Bonus = ₹5000
# ○ Tax Rate = 10%
# ○ Other Charges = ₹2000

base_salary = 50000
bonus = 5000
tax_rate = 0.10
other_charges = 2000
gross_salary = base_salary + bonus
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount - other_charges
print(f"Gross Salary: ₹{gross_salary:.2f}")
print(f"Tax Amount: ₹{tax_amount:.2f}")
print(f"Net Salary: ₹{net_salary:.2f}")