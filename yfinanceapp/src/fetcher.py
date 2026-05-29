import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# A hardcoded list of popular tickers to simulate "Top Stocks" since yfinance 
# doesn't have a native "Top 20" screener endpoint.
TOP_TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "BRK-B", "TSLA", "LLY", "V",
    "UNH", "XOM", "WMT", "JPM", "JNJ", "MA", "PG", "AVGO", "HD", "ORCL"
]

def get_historical_data(ticker_symbol, timeframe="1mo"):
    """
    Fetches historical data for a specific ticker.
    Timeframe options: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    """
    # TODO: Add error handling if the ticker doesn't exist
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=timeframe)
    return hist

def get_top_stocks_close(num_stocks=20):
    """
    Gets yesterday's closing price for the top N stocks.
    """
    if num_stocks > len(TOP_TICKERS):
        num_stocks = len(TOP_TICKERS)
        
    selected_tickers = TOP_TICKERS[:num_stocks]
    results = []
    
    # INTENTIONAL FLAW: This downloads one by one, which is slow.
    # An agent should probably optimize this to use yf.download(threads=True)
    for symbol in selected_tickers:
        try:
            ticker = yf.Ticker(symbol)
            # Getting the last 2 days to ensure we get yesterday's close
            hist = ticker.history(period="2d")
            
            # INTENTIONAL BUG: If it's Monday, "yesterday" (Sunday) has no data.
            # This will raise an IndexError on the weekend/Mondays.
            yesterday_close = hist['Close'].iloc[-2] 
            
            results.append({
                "Ticker": symbol,
                "Close Price": round(yesterday_close, 2)
            })
        except Exception as e:
            # TODO: Better logging needed here
            print(f"Failed to fetch {symbol}: {e}")
            
    return pd.DataFrame(results)