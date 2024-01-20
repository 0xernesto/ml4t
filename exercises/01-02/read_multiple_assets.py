"""Read data for multiple assets."""
import os
import sys
import pandas as pd

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def test_run():
    # Define data range
    start_date = "2010-01-22"
    end_date = "2010-01-26"
    dates = pd.date_range(start_date, end_date)

    symbols = ["GOOG", "IBM", "GLD"]

    df = get_adj_close(symbols, dates=dates)

    print(df)


if __name__ == "__main__":
    test_run()
