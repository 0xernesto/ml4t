"""Reading in a CSV File"""

import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    # Quiz: Print last 5 rows of the data frame
    # print df				# prints entire data set (dataframe)
    # print df.head()		# prints first five records
    print(df.tail())  # prints last five records


if __name__ == "__main__":
    test_run()
