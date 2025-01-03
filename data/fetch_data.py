import yfinance as yf

def fetch_historical_data(stock, interval="1d", period="1y"):
    """
    Fetches historical daily stock data from Yahoo Finance.

    Args:
        stock (str): Ticker symbol of the stock.
        interval (str): Time interval for data (default is '1d').
        period (str): Duration of data to fetch (default is '1y').

    Returns:
        pandas.DataFrame: Stock data.
    """
    try:
        print(f"Fetching daily data for {stock}...")
        data = yf.download(stock, interval=interval, period=period)
        if data.empty:
            raise ValueError(f"No data returned for {stock}. Check the ticker or network connection.")
        print(f"Data for {stock} fetched successfully. Rows: {len(data)}")
        return data
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None
