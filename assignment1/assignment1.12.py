# Calculate profit or loss percentage
# Input: cost_price = 500, selling_price = 600
# Output: Profit or Loss = ?

cost_price=500
selling_price=600
if selling_price>cost_price:
    profit=selling_price-cost_price
    profit_percentage=(profit/cost_price)*100
    print("Profit percentage=",profit_percentage)
else:
    loss=cost_price-selling_price
    loss_percentage=(loss/cost_price)*100
    print("Loss percentage=",loss_percentage)