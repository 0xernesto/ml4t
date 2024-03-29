"""Computing Max Closing Price"""

import pandas as pd


def get_max_close(symbol):
    """Return the maximum closing value for asset indicated by symbol.

    Note: Data for a asset is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df["Close"].max()  # compute and return max


def test_run():
    """Function called by Test Run."""
    for symbol in ["AAPL", "IBM"]:
        print("Max close")
        print(symbol, get_max_close(symbol))


if __name__ == "__main__":  # if run standalone
    test_run()
