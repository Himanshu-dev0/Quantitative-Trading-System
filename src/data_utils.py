
import pandas as pd
import os
import yfinance as yf

def fetch_data(symbol, period="60d", interval="5m"):
    """
    Fetches historical data from Yahoo Finance.
    """
    try:
        data = yf.download(symbol, period=period, interval=interval, progress=False)
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

def save_data(df, filename, data_dir="../data"):
    """
    Saves DataFrame to CSV.
    """
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    path = os.path.join(data_dir, filename)
    df.to_csv(path)
    print(f"Saved: {path}")

def load_data(filename, data_dir="../data"):
    """
    Loads DataFrame from CSV.
    """
    path = os.path.join(data_dir, filename)
    if os.path.exists(path):
        return pd.read_csv(path, index_col=0, parse_dates=True)
    else:
        print(f"File not found: {path}")
        return None

def merge_data(dfs, on_index=True):
    """
    Merges a list of DataFrames.
    """
    if not dfs:
        return pd.DataFrame()
    
    merged_df = dfs[0]
    for i in range(1, len(dfs)):
        if on_index:
            merged_df = merged_df.join(dfs[i], how='inner', rsuffix=f'_{i}')
    
    return merged_df
