"""Plot a histogram."""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close
from utils.plot_data import plot_data


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0, :] = 0  # set daily returns for first row to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range("2009-01-01", "2012-12-31")
    symbols = ["SPY"]
    df = get_adj_close(symbols, dates)
    plot_data(df, title="Adjusted Close Asset Prices", ylabel="Price")

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # Plot a histogram
    daily_returns.hist()  # default number of bins, 10
    plt.title("Histogram of Daily Returns (10 Bins)")
    plt.xlabel("Daily Returns")
    plt.ylabel("Frequency")

    daily_returns.hist(bins=20)  # changing number of bins to 20
    plt.title("Histogram of Daily Returns (20 Bins)")
    plt.xlabel("Daily Returns")
    plt.ylabel("Frequency")

    # Show all figures from plot_data and histograms
    plt.show()


if __name__ == "__main__":
    test_run()
