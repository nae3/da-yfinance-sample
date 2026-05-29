import sys
from src.fetcher import get_historical_data, get_top_stocks_close
from src.formatter import display_dataframe

def display_menu():
    print("\n--- Market Tracker Menu ---")
    print("1. Get Top Stocks (Yesterday's Close)")
    print("2. Get Historical Data for a Ticker")
    print("3. Export Last Query to CSV (Coming Soon)")
    print("4. Exit")
    return input("Select an option (1-4): ")

def run_cli():
    print("Welcome to Market Tracker CLI")
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            try:
                num = int(input("How many top stocks to fetch? (1-20): "))
                print(f"Fetching data for top {num} stocks... This might take a moment.")
                df = get_top_stocks_close(num_stocks=num)
                display_dataframe(df)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == '2':
            ticker = input("Enter ticker symbol (e.g., AAPL): ").upper()
            timeframe = input("Enter timeframe (1d, 5d, 1mo, 1y): ")
            print(f"Fetching {timeframe} data for {ticker}...")
            # TODO: The output of this is messy because it's a raw pandas dataframe 
            # with lots of columns. An agent should be asked to clean this up.
            df = get_historical_data(ticker, timeframe)
            # Reset index to make date a column for cleaner printing
            if not df.empty:
                df = df.reset_index()
            display_dataframe(df)
            
        elif choice == '3':
            print("\nFeature not implemented yet! Check the TODOs.")
            # TODO: Call formatter.export_to_csv() once it's built
            
        elif choice == '4':
            print("Exiting Market Tracker. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid selection. Please try again.")