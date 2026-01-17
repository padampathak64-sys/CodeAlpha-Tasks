# This program calculates total investemnt values based on user input

# Hardcoded stock prices

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

# Variable to store total investment value
total_investment = 0

# List to store investment details
investment_details = []

print("Available stocks:", ", ".join(stock_prices.keys()))

# User input loop

while True:
    stock_name = input("\nEnter stock name (or type 'exit' to finish):").upper()

    # Exit loop if user is exit
    if stock_name == "EXIT":
        break

    # Check if stock exists in dictionary
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        investment_details.append([stock_name, quantity, price, investment])

        print(f"Added {quantity} shares of {stock_name} worth ${investment}")
    
    # Check if stock doesn't exists in dictionary
    else:
        print("Stock not found!")

# Display final result

print("\n----- Investment Summary -----")
for item in investment_details:
    print(f"{item[0]} | Quantity: {item[1]} | Price: ${item[2]} | Value: ${item[3]}")

print(f"\nTotal investment value: {total_investment}")

# Save result to file
save_file = input("\nDo you want to save the result to a file? (yes/no):").lower()

if save_file == "yes":
    with open("stock_investment.txt", "w") as file:
        file.write(f"Total Investment Value: {total_investment}\n")

    print("✅ Data saved to stock_investment.txt")

print("\nThank you for using the stock tracker!")