"""Computing Histogram Statistics"""

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
    plot_data(df_data=df, title="SPY Adj. Close", ylabel="Price")

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # Get mean and standard deviation
    mean = daily_returns["SPY"].mean()
    std = daily_returns["SPY"].std()
    print("Daily Returns Mean: ", mean)
    print("\nDaily Returns Standard Deviation: ", std)

    # Print bin count
    print("\nDaily Returns Bin Count: ", len(daily_returns))

    # Compute kurtosis
    print("\nDaily Returns Kurtosis: ", daily_returns.kurtosis())

    # Plot a histogram
    daily_returns.hist(bins=20)

    # Label histogram
    plt.title("Histogram of Daily Returns (20 Bins)")
    plt.xlabel("Daily Returns")
    plt.ylabel("Frequency")

    # Add mean and std line markers to the histogram
    plt.axvline(mean, color="w", linestyle="dashed", linewidth=2)
    plt.axvline(std, color="r", linestyle="dashed", linewidth=2)
    plt.axvline(-std, color="r", linestyle="dashed", linewidth=2)

    # Show all figures
    plt.show()


if __name__ == "__main__":
    test_run()
