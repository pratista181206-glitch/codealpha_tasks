# Stock Portfolio Tracker

# Stock prices in Indian Rupees
prices = {
    "AAPL":  15600,
    "TSLA":  20800,
    "GOOGL": 11600,
    "AMZN":  14800,
    "MSFT":  34500
}

print("Welcome to Stock Tracker!")
print("Available stocks:", list(prices.keys()))
print()

total = 0
portfolio = {}

# Ask user for stocks
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not found! Try again.")
        continue

    qty = int(input("How many shares? "))
    value = prices[stock] * qty
    portfolio[stock] = qty
    total += value
    print(f"Added! {stock} x {qty} = ₹{value}")
    print()

# Show summary
print("---- Your Portfolio ----")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares = ₹{prices[stock] * qty}")

print(f"Total investment: ₹{total}")

# Save to file
save = input("Save to file? (yes/no): ")
if save == "yes":
    file = open("portfolio.txt", "w", encoding="utf-8")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares = ₹{prices[stock] * qty}\n")
    file.write(f"Total: ₹{total}\n")
    file.close()
    print("Saved to portfolio.txt!")
