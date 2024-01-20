"""Plot data for multiple assets"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def plot_data(df, title="Asset Prices"):
    """Plot asset prices with a custom title and meaningful axis labels."""
    axis = df.plot(title=title, fontsize=12)
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range("2010-01-01", "2010-12-31")

    # Choose asset symbols to read
    symbols = ["GOOG", "IBM", "GLD"]  # SPY will be added in get_data()

    # Get asset data
    df = get_adj_close(symbols, dates)

    # Plot
    plot_data(df)


if __name__ == "__main__":
    test_run()
