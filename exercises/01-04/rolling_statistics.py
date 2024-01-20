"""Computing Rolling Statistics"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def test_run():
    # Read data
    dates = pd.date_range("2010-01-01", "2012-12-31")
    symbols = ["SPY", "XOM", "GOOG", "GLD"]
    df = get_adj_close(symbols, dates)

    # Plot SPY, retain matplotlib axis object
    axis = df["SPY"].plot(title="SPY Rolling Mean", label="SPY")

    # Compute rolling mean using a 20-day window
    rm_SPY = df["SPY"].rolling(window=20).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label="Rolling mean", ax=axis)

    # Add axis labels and legend
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.legend(loc="upper left")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    plt.show()


if __name__ == "__main__":
    test_run()
