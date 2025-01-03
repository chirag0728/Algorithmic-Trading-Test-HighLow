import yfinance as yf

def fetch_historical_data(stock, interval="5m", period="1mo"):
    """
    Fetches historical stock data from Yahoo Finance.

    Args:
        stock (str): Ticker symbol of the stock.
        interval (str): Time interval for data (e.g., '1m', '5m').
        period (str): Duration of data to fetch (e.g., '1mo').

    Returns:
        pandas.DataFrame: Stock data.
    """
    try:
        print(f"Fetching data for {stock} with interval={interval} and period={period}...")
        data = yf.download(stock, interval=interval, period=period)
        if data.empty:
            raise ValueError(f"No data returned for {stock}. Check the ticker or network connection.")
        print(f"Data for {stock} fetched successfully. Rows: {len(data)}")
        return data
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None
