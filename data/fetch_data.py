import yfinance as yf

def get_stock_data(stock):
    data = yf.download(stock, period="1d", interval="1m")
    if data.empty:
        print(f"Error: No data fetched for {stock}")
    return data
