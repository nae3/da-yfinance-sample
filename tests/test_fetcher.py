import pytest
from src.fetcher import get_historical_data, TOP_TICKERS

def test_top_tickers_list():
    """Ensure our hardcoded list has the expected number of tickers."""
    assert len(TOP_TICKERS) == 20

def test_get_historical_data_valid_ticker():
    """Test that we get a dataframe back for a valid ticker."""
    df = get_historical_data("AAPL", "5d")
    assert not df.empty
    assert "Close" in df.columns

# TODO: Write a test for get_top_stocks_close()
# TODO: Write a test to ensure invalid tickers throw the correct error