# .Employee Salary Based on Experience.
# You are building a system for a Human Resources (HR) department that calculates an
# employee's salary based on their years of experience. The system assigns salary tiers
# based on the number of years an employee has been working. It also offers bonuses for
# employees who have more than 15 years of experience.
# Scenario Breakdown:
# Context 1: Senior Employee
# ● An employee with 10 or more years of experience is classified as a Senior
# Employee. The base salary for such an employee is 80000.
# ● If the employee has more than 15 years of experience they receive a bonus of
# 5000 to their salary.
# Example:
# An employee with 18 years of experience:
# ● They are classified as Senior Employees.
# ● Their base salary is 80000.
# ● Since they have more than 15 years of experience they receive an additional
# 5000 bonus.
# ● The final salary is 85000.
# Context 2: Mid-Level Employee
# ● Employees with 5 to 9 years of experience are classified as Mid-Level
# Employees.
# ● Their base salary is 50000 with no bonus.
# Example:
# An employee with 7 years of experience:
# ● They are classified as a Mid-Level Employee.
# ● Their base salary is 50000.
# ● Since they have fewer than 10 years of experience no bonus is added.
# ● The final salary is 50000.
# Context 3: Junior Employee
# ● Employees with less than 5 years of experience are classified as Junior
# Employees.
# ● Their base salary is 30000 with no bonus.
# Example:
# An employee with 3 years of experience:
# ● They are classified as Junior Employees.
# ● Their base salary is 30000.
# ● No bonus is added.
# ● The final salary is 30000.
# Output Examples:
# Senior Employee with 18 years of experience:
# Enter years of experience: 18
# Senior employee
# Experience exceeds 15 years. Bonus added.
# Salary: 85000
# Mid-Level Employee with 7 years of experience:
# Enter years of experience: 7
# Mid-level employee
# Salary: 50000
# Junior Employee with 3 years of experience:
# Enter years of experience: 3
# Junior employee
# Salary: 30000

years_of_experience = int(input("Enter years of experience: "))
if years_of_experience >= 10:       
    print("Senior employee")
    salary = 80000
    if years_of_experience > 15:
        print("Experience exceeds 15 years. Bonus added.")
        salary += 5000
elif 5 <= years_of_experience < 10:
    print("Mid-level employee")
    salary = 50000
else:
    print("Junior employee")
    salary = 30000
print(f"Salary: {salary}")