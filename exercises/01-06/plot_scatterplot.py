import os
import sys
import numpy as np
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
    daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range("2009-01-01", "2012-12-31")
    symbols = ["SPY", "XOM", "GLD"]
    df = get_adj_close(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind="scatter", x="SPY", y="XOM")

    # Calling polyfit will return the slope and intercept of the best fit line
    beta_XOM, alpha_XOM = np.polyfit(
        x=daily_returns["SPY"], y=daily_returns["XOM"], deg=1
    )
    print("\nbeta_XOM: ", beta_XOM)
    print("\nalpha_XOM: ", alpha_XOM)

    plt.plot(
        daily_returns["SPY"],
        beta_XOM * daily_returns["SPY"] + alpha_XOM,
        "-",
        color="r",
    )
    plt.title("Scatterplot of XOM vs SPY")

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind="scatter", x="SPY", y="GLD")
    beta_GLD, alpha_GLD = np.polyfit(
        x=daily_returns["SPY"], y=daily_returns["GLD"], deg=1
    )
    print("\nbeta_GLD: ", beta_GLD)
    print("\nalpha_GLD: ", alpha_GLD)

    plt.plot(
        daily_returns["SPY"],
        beta_GLD * daily_returns["SPY"] + alpha_GLD,
        "-",
        color="r",
    )
    plt.title("Scatterplot of GLD vs SPY")

    plt.show()


if __name__ == "__main__":
    test_run()
