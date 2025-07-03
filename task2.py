# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 125
}

portfolio = {}
total_value = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from:", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate total investment value
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Total Value\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
    print(f"✅ Portfolio saved to {filename}")
