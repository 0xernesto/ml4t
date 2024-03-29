"""Plotting Asset Price Data"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    """Plot a single column."""
    df = pd.read_csv("data/AAPL.csv")
    print(df["Adj Close"])
    df["Adj Close"].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
