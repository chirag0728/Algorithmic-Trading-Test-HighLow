# **Algorithmic Trading Test - High/Low and EMA Directionality**

This application provides real-time insights into stock price movements, including daily highs, lows, and EMA-based directional analysis, helping you make informed decisions without executing trades automatically.

---

## **Features**

- **Real-Time Data Fetching**:
  - Fetches live stock data for selected tickers (e.g., SPY, QQQ) using `yfinance`.
  
- **EMA Calculations**:
  - Computes Exponential Moving Averages (EMAs) for 8, 9, and 200 periods.
  
- **High/Low Tracking**:
  - Identifies the highest and lowest prices of the day for each stock.

- **Directional Analysis**:
  - Analyzes trends based on EMA relationships (e.g., Uptrend, Downtrend, Sideways).

- **CLI Output**:
  - Displays all information directly in the terminal for a clean, user-friendly experience.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chirag0728/Algorithmic-Trading-Test-HighLow.git
   cd Algorithmic-Trading-Test-HighLow
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Run the Application**:
   Execute the main script to fetch stock data and analyze movements:
   ```bash
   python main.py
   ```

2. **View Output**:
   - Results are displayed directly in the terminal.
   - Example output:
     ```
     📈 Stock Movement Tracker

     Fetching data for SPY...
         ┌─────────────────────────────────────────┐
         │               SPY Summary              │
         ├─────────────────────────────────────────┤
         │ High of the Day       : 456.25          │
         │ Low of the Day        : 449.85          │
         │ Directionality        : Uptrend         │
         ├─────────────────────────────────────────┤
         │ EMA (8)               : 452.45          │
         │ EMA (9)               : 451.95          │
         │ EMA (200)             : 448.15          │
         └─────────────────────────────────────────┘
     ```

---

## **Configuration**

Modify the stocks you want to track in `config/settings.py`:
```python
STOCKS = ["SPY", "QQQ"]  # Add more tickers as needed
```

---

## **Project Structure**

```
Algorithmic-Trading-Test-HighLow/
├── main.py                # Entry point for the application
├── config/
│   ├── settings.py        # Configuration for stocks and data sources
├── data/
│   ├── fetch_data.py      # Fetches stock data
├── indicators/
│   ├── ema.py             # Calculates EMAs
├── analysis/
│   ├── high_low.py        # Tracks daily high and low
│   ├── decision.py        # Analyzes trends and directionality
├── utils/
│   ├── formatter.py       # Handles CLI output formatting
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## **Dependencies**

This project uses the following libraries:
- `pandas`: For data manipulation.
- `yfinance`: To fetch real-time stock data.

Install them via:
```bash
pip install -r requirements.txt
```

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Future Enhancements**

- Add more advanced indicators (e.g., RSI, MACD).
- Support for historical data analysis.
- Export results to other formats (e.g., PDF, Excel).

--- 