"""Fill missing values of mutliple assets."""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close
from utils.fill_missing import fill_missing


def plot_data(df_data):
    """Plot asset data with appropriate axis labels."""
    axis = df_data.plot(title="Asset Data", fontsize=12)
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    plt.show()


def test_run():
    """Function called by Test Run."""
    symbol_list = ["JAVA", "FAKE1", "FAKE2"]
    start_date = "2005-12-31"
    end_date = "2014-12-07"
    dates = pd.date_range(start_date, end_date)
    df_data = get_adj_close(symbol_list, dates)

    # Fill missing values
    fill_missing(df_data)

    # Plot
    plot_data(df_data)


if __name__ == "__main__":
    test_run()
