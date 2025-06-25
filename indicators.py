import pandas as pd

def add_indicators(df):
    df['20DMA'] = df['Close'].rolling(20).mean()
    df['50DMA'] = df['Close'].rolling(50).mean()

    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df
