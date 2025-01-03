from config.settings import STOCKS
from data.fetch_data import get_stock_data
from indicators.ema import calculate_ema
from analysis.high_low import track_high_low
from analysis.decision import analyze_directionality
from utils.logger import log_to_csv

def main():
    print("Stock Movement Tracker")
    for stock in STOCKS:
        print(f"\nFetching data for {stock}...")
        data = get_stock_data(stock)
        if data.empty:
            print(f"No data available for {stock}")
            continue

        ema_8 = calculate_ema(data['Close'], 8)
        ema_9 = calculate_ema(data['Close'], 9)
        ema_200 = calculate_ema(data['Close'], 200)

        high, low = track_high_low(data)
        direction = analyze_directionality(ema_8, ema_9, ema_200)

        log_to_csv(stock, high, low, direction)
        print(f"{stock}: High={high}, Low={low}, Direction={direction}")

if __name__ == "__main__":
    main()
