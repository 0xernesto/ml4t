"""Select Rows"""

import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    print(df[10:21])  # print rows between index 10 and 20 inclusive


if __name__ == "__main__":
    test_run()
