import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_data_yfinance(ticker: str, days: int = 365):
    """
    Fetch historical OHLC data for a ticker from Yahoo Finance.
    Args:
        ticker (str): Ticker symbol (e.g., "SPY").
        days (int): Number of days of data to fetch (default: 365).
    Returns:
        pd.DataFrame: Historical OHLC data.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - pd.Timedelta(days=days)).strftime('%Y-%m-%d')
    print(f"Fetching {days} days of data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=today)
    return data.reset_index()
