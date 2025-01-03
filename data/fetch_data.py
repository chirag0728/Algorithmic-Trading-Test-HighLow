import yfinance as yf

def fetch_historical_data(stock, interval="5m", period="60d"):
    data = yf.download(stock, interval=interval, period=period)
    return data
