# Task: Calculate Profit Percentage
# ● Write a program that takes input for the cost price and selling price of an item.
# ● Hints
# ○ Prompt the user to input the cost price and selling price.
# ○ Determine whether the transaction resulted in a profit or loss.
# ○ If there is a profit calculate the profit percentage; if there is a loss
# calculate the loss percentage.
# ○ Display the profit or loss and the respective percentage.

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))       
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100         
    print(f"Profit: {profit:.2f}")
    print(f"Profit Percentage: {profit_percentage:.2f}%")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100         
    print(f"Loss: {loss:.2f}")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
else:
    print("No profit, no loss.")
    