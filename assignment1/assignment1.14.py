# Calculate compound interest
# Input: principal = 10000, rate = 5, time = 2
# Output: Compound Interest = ?


principal = 10000
rate = 5
time = 2

# Compound Interest formula: A = P(1 + r/100)^t
amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)