from indicators import add_indicators
from telegram_alerts import send_telegram_message
import logging
import pandas as pd

def generate_signals(df, symbol):
    df = add_indicators(df)
    df['Signal'] = ((df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])).astype(int)

    # Make sure 'Date' is a column
    if 'Date' not in df.columns:
        df.reset_index(inplace=True)

    for idx, row in df.iterrows():
        try:
            signal_value = row['Signal']
            if isinstance(signal_value, (int, float)) and signal_value == 1:
                date_value = row['Date']
                date_str = pd.to_datetime(date_value).strftime('%Y-%m-%d') if not pd.isna(date_value) else "Unknown"

                send_telegram_message(
                    f"Buy Signal: {symbol}\nDate: {date_str}\nClose: ₹{row['Close']:.2f}"
                )
        except Exception as e:
            logging.error(f"Telegram Alert Error: {str(e)}")
            try:
                send_telegram_message(f"Error in Algo-Trading System:\n{str(e)}")
            except Exception as e2:
                logging.error(f"Telegram Send Failed: {e2}")

    return df


