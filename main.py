import os
import logging
from data_fetch import fetch_multiple_stocks
from strategy import generate_signals
from prediction_model import train_predictor
from data_sheet import log_signals_to_sheet

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def run():
    symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    logging.info("Algo-Trading System Started")
    
    all_data = fetch_multiple_stocks(symbols)
    for symbol, df in all_data.items():
        df = generate_signals(df, symbol)
        clf, accuracy = train_predictor(df)
        logging.info(f"{symbol} - Model Accuracy: {accuracy:.2f}")
        log_signals_to_sheet(df, stock=symbol.split('.')[0])

    logging.info("Execution completed.")

if __name__ == "__main__":
    run()
