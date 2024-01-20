"""Bollinger Bands."""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def get_rolling_mean(values, windows):
    """Return rolling mean of given values, using specified window size."""
    return values.rolling(window=windows).mean()


def get_rolling_std(values, windows):
    """Return rolling standard deviation of given values, using specified window size."""
    # Quiz: Compute and return rolling standard deviation
    return values.rolling(window=windows).std()


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    # Quiz: Compute upper_band and lower_band
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


def test_run():
    # Read data
    dates = pd.date_range("2012-01-01", "2012-12-31")
    symbols = ["SPY"]
    df = get_adj_close(symbols, dates)

    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df["SPY"], windows=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df["SPY"], windows=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    axis = df["SPY"].plot(title="Bollinger Bands", label="SPY")
    rm_SPY.plot(label="Rolling mean", ax=axis)
    upper_band.plot(label="Upper Band", ax=axis)
    lower_band.plot(label="Lower Band", ax=axis)

    # Add axis labels and legend
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.legend(loc="upper left")

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    plt.show()


if __name__ == "__main__":
    test_run()
