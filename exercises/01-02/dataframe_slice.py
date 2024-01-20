"""Dataframe slicing"""

import os
import sys
import pandas as pd

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close


def test_run():
    # Define a date range
    dates = pd.date_range("2010-01-01", "2010-12-31")

    # Choose asset symbols to read
    symbols = ["GOOG", "IBM", "GLD"]  # SPY will be added in get_data()

    # Get asset data
    df = get_adj_close(symbols, dates)

    # Slice by row range (dates) using DataFram.loc[] selector
    print(
        "All January Adj Close:\n", df.loc["2010-01-01":"2010-01-31"]
    )  # the month of January

    #  Slice by column (symbols)
    print("\nGOOGL Adj Close:\n", df["GOOG"])  # a single label selects a single column
    print(
        "\nIBM and GLD Adj Close:\n",
        df[["IBM", "GLD"]],  # a list of labels selects multiple columns
    )

    # Slice by row and column
    print(
        "\nSPY and IBM Adj Close from March 1 to 15:\n",
        df.loc["2010-03-01":"2010-03-15", ["SPY", "IBM"]],
    )


if __name__ == "__main__":
    test_run()
