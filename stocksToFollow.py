import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period="1d")
    return todays_data['Close'][0], stock.info['fiftyDayAverage'], stock.info['twoHundredDayAverage']

tickers = ["SPY", "AMZN", "SHOP"]
stock_info = {ticker: get_stock_info(ticker) for ticker in tickers}

# ANSI escape codes for text colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0m"

colors = [RED, GREEN, YELLOW]
print("\n")
print("Stock Prices", end=" ")
for i, (ticker, info) in enumerate(stock_info.items()):
    price, ma50, ma200 = info
    print(f"{colors[i]}{ticker}: ${price:.2f} (50-day MA: ${ma50:.2f}, 200-day MA: ${ma200:.2f}){RESET}", end=" " * (5 - len(ticker)))

print()  # Add a newline at the end
