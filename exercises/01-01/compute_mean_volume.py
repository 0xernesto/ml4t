"""Compute Mean Volume"""

import pandas as pd
import matplotlib.pyplot as plt


def get_mean_volume(symbol):
    """Return the mean volume for asset indicated by symbol.
    Note: Data for a asset is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    # Quiz: Compute and return the mean volume for this asset
    return df["Volume"].mean()


def test_run():
    """Function called by Test Run."""
    for symbol in ["AAPL", "IBM"]:
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    test_run()
