#  If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred.

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

profit_loss = selling_price - cost_price

if profit_loss == 0:
    print("Nither profit nor loss....")
elif selling_price > cost_price:
    print(f"The total profit is {profit_loss}")
elif selling_price < cost_price:
    print(f"The total loss is {abs(profit_loss)}")