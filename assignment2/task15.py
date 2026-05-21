# Tax Calculation for Car Purchase
# Write a program to calculate the tax on a car purchase based on the car brand and its price.
# 1. Mahindra: 5% tax for prices between 7L (7 lakh) and 10L.
# 2. Audi: 10% tax for prices between 10L and 15L.
# 3. Jaguar: 25% tax for prices between 15L and 20L.
# 4. Mercedes: 30% tax for prices between 20L and 25L.
# 5. Input: The car brand and price.
# 6. Output: The calculated tax on the purchase.
car_brand = input("Enter the car brand (Mahindra, Audi, Jaguar, Mercedes): ")
car_price = float(input("Enter the price of the car (in lakhs): "))

if car_brand == "Mahindra" and 7 <= car_price <= 10:
    tax = car_price * 0.05
elif car_brand == "Audi" and 10 < car_price <= 15:
    tax = car_price * 0.10
elif car_brand == "Jaguar" and 15 < car_price <= 20:
    tax = car_price * 0.25
elif car_brand == "Mercedes" and 20 < car_price <= 25:
    tax = car_price * 0.30
else:
    tax = 0
    print("No tax applicable for the given car brand and price.")   
if tax > 0:
    print(f"The tax on the purchase of the {car_brand} car priced at {car_price} lakhs is: {tax:.2f} lakhs.")
    