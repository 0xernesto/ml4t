"""Plot Two Columns"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("data/IBM.csv")
    df[["Close", "Adj Close"]].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
