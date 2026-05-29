import pandas as pd

def display_dataframe(df):
    """
    Prints a pandas dataframe in a clean format to the console.
    """
    if df is None or df.empty:
        print("No data available to display.")
        return
    
    print("\n" + "="*40)
    print(df.to_string(index=False))
    print("="*40 + "\n")

# TODO: Implement export_to_csv(df, filename) function here
# The CLI menu has an option for it, but the function doesn't exist yet!