import pandas as pd
from src.indicators import candlestick_patterns

def clean_data(data):
    """
    Cleans raw OHLC data by dropping NaNs and handling data types.
    Args:
        data (pd.DataFrame): Raw OHLC data.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    print("Cleaning data...")
    data = data.dropna()
    required_columns = ['Open', 'High', 'Low', 'Close']
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"Required columns {required_columns} are missing from the data.")
    return data

def flatten_columns(data):
    """
    Flattens multi-index column names into single strings.
    Args:
        data (pd.DataFrame): DataFrame with multi-index columns.
    Returns:
        pd.DataFrame: DataFrame with flattened column names.
    """
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = ['_'.join(col).strip() for col in data.columns]
    return data

def add_directionality(data, window=3):
    """
    Adds a directionality indicator based on rolling window trends.
    Args:
        data (pd.DataFrame): Preprocessed data with OHLC columns.
        window (int): Rolling window size for directionality.
    Returns:
        pd.DataFrame: Data with an added 'Direction' column.
    """
    print("Calculating directionality...")
    close_column = [col for col in data.columns if 'Close' in col][0]  # Dynamically find 'Close' column
    data['Direction'] = data[close_column].diff().rolling(window=window).mean()
    data['Direction'] = data['Direction'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
    return data

def preprocess_with_patterns(data):
    """
    Preprocesses OHLC data by cleaning it, adding candlestick patterns, and computing directionality.
    Args:
        data (pd.DataFrame): Raw OHLC data.
    Returns:
        pd.DataFrame: Preprocessed data with additional features.
    """
    print("Preprocessing data with candlestick patterns...")
    data = clean_data(data)
    data = candlestick_patterns(data)

    # Reset index and drop unnecessary columns
    data = data.reset_index(drop=True).drop(columns=['Date'], errors='ignore')

    # Flatten multi-index columns
    data = flatten_columns(data)

    # Debugging: Print column names after flattening
    print("Columns after flattening:", data.columns)

    # Add directionality indicator
    data = add_directionality(data)

    # One-hot encode the Pattern column if it exists
    if 'Pattern' in data.columns:
        data = pd.get_dummies(data, columns=['Pattern'], drop_first=True)

    print("Preprocessing complete.")
    return data
