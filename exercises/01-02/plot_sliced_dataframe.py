"""Slice a dataframe, normalize, and plot the price data."""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def normalize_data(df):
    """Normalize asset prices using the first row of the dataframe."""
    return df / df.iloc[0, :]


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # Quiz: Your code here
    plot_data(df.loc[start_index:end_index, columns], title="Selected Normalized Data")


def plot_data(df, title="Asset Prices"):
    """Plot asset prices with a custom title and meaningful axis labels."""
    axis = df.plot(title=title, fontsize=12)
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))


def test_run():
    # Define a date range
    dates = pd.date_range("2010-01-01", "2010-12-31")

    # Choose asset symbols to read
    symbols = ["GOOG", "IBM", "GLD"]  # SPY will be added in get_data()

    # Get asset data
    df = get_adj_close(symbols, dates)

    print("Pre-Sliced Price Data:\n", df)

    df_norm = normalize_data(df)

    # Plot all normalized data
    plot_data(df=df_norm, title="All Normalized Data")

    # Slice and plot normalized data
    plot_selected(
        df=df_norm,
        columns=["SPY", "IBM"],
        start_index="2010-03-01",
        end_index="2010-04-01",
    )

    # Putting this here so both plot figures show up at the same time.
    plt.show()


if __name__ == "__main__":
    test_run()
