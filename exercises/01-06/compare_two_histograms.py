"""Plot Two Histograms together"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0, :] = 0  # set daily returns for first to 0
    return daily_returns


def test_run():
    dates = pd.date_range("2009-01-01", "2012-12-31")
    symbols = ["SPY", "XOM"]
    df = get_adj_close(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Plot both histograms on the same figure
    daily_returns["SPY"].hist(bins=20, label="SPY")
    daily_returns["XOM"].hist(bins=20, label="XOM")
    plt.legend(loc="upper right")
    plt.title("Histogram of Daily Returns (20 Bins)")
    plt.xlabel("Daily Returns")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    test_run()
