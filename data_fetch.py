import yfinance as yf
import pandas as pd

def fetch_daily_stock_data(symbol):
    df = yf.download(symbol, period="6mo", interval="1d")
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df

def fetch_multiple_stocks(symbols):
    data = {}
    for symbol in symbols:
        try:
            df = fetch_daily_stock_data(symbol)
            data[symbol] = df
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
    return data



