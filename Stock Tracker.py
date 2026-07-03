stock_prices = {
    'AAPL': 180,
    'TSLA': 210,
    'COGS': 110,
    'DASK': 240,
    'FBEW': 130,
    'MSFT': 300
}

total_value = 0
print("***** STOCK PORTFOLIO TRACKER *****")

num_stocks = int(input("\nHow many stocks do you want to enter? "))

for i in range(num_stocks):

    stock_name = input("\nStock Name: ").upper()
    stock_quantity = int(input("Stock Quantity: "))

    if stock_name in stock_prices:

        invest = stock_prices[stock_name] * stock_quantity
        total_value += invest

        print("Price per Share: ", stock_prices[stock_name])
        print("Investment Value: $", invest)

    else:
        print("Stock not found!")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value: ", total_value)

# file = open("stock_portfolio.txt", "w")
file = open("stock_details.txt", "a", newline='')
file.write("\nTotal Investment Value: $" + str(total_value))
file.close()

print("Portfolio saved to stock_details.txt")
