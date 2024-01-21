"""Using bfll and ffill to fill missing data."""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def plot(df_data):
    axis = df_data.plot(title="Incomplete Data", fontsize=12)
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.show()


if __name__ == "__main__":
    symbols = ["FAKE2"]

    # Create date range
    start_date = "2005-12-31"
    end_date = "2014-12-07"
    dates = pd.date_range(start_date, end_date)

    # Get adjusted close of each symbol
    df_data = get_adj_close(symbols, dates)

    # Fill missing data
    df_data.ffill(inplace=True)
    df_data.bfill(inplace=True)

    plot(df_data)
