# Market Tracker CLI

A simple command-line interface for fetching and displaying stock market data using the `yfinance` library. 

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script to start the interactive menu:
`python main.py`

## TODO
- [ ] Add CSV export functionality.
- [ ] Improve error handling for network timeouts.
- [ ] Write more unit tests (currently only tests basic fetching).
- [ ] Fix the bug where weekend dates crash the "yesterday's close" feature.