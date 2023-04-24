import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period="1d")
    return todays_data['Close'][0]

tickers = ["SPY", "AMZN", "SHOP"]
stock_info = {ticker: get_stock_info(ticker) for ticker in tickers}

# ANSI escape codes for text colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0m"

colors = [RED, GREEN, YELLOW]

print("Stock Prices:", end=" ")
print("\n")
for i, (ticker, price) in enumerate(stock_info.items()):
    print(f"{colors[i]}{ticker}: ${price:.2f}{RESET}", end=" " * (20 - len(ticker)))

print()  # Add a newline at the end
