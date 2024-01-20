"""Compute Daily Returns"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def plot_data(df, title="Asset Prices", xlabel="Date", ylabel="Price"):
    """Plot asset prices with a custom title and meaningful axis labels."""
    axis = df.plot(title=title, fontsize=12)
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # 1. Make a copy of the dataframe
    daily_returns = df.copy()

    # 2. Compute daily returns starting at index 1
    daily_returns = (df / df.shift(1)) - 1

    # 3. Set the first row's returns to 0, since
    #    Pandas leaves the 0th row full of Nans
    daily_returns.iloc[0, :] = 0

    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range("2012-07-01", "2012-07-31")  # one month only
    symbols = ["SPY", "XOM"]
    df = get_adj_close(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    plt.show()


if __name__ == "__main__":
    test_run()
