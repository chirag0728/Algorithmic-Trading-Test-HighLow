from config.settings import STOCKS
from models.predict_high_low import predict_high_low

def main():
    print("📈 Stock Predictor - Next Trading Day High/Low\n")
    for stock in STOCKS:
        print(f"Fetching data and predicting for {stock}...")
        predicted_high, predicted_low = predict_high_low(stock)
        print(f"{stock} - Predicted High: {predicted_high:.2f}, Predicted Low: {predicted_low:.2f}")

if __name__ == "__main__":
    main()
