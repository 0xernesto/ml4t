"""Returns a joined dataframe for adjusted close price"""
import pandas as pd

from .symbol_to_path import symbol_to_path


def get_adj_close(symbols, dates):
    df = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        # Quiz: Read and join data for each symbol
        df_temp = pd.read_csv(
            symbol_to_path(symbol),
            index_col="Date",
            parse_dates=True,
            usecols=["Date", "Adj Close"],
            na_values=["nan"],
        )
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df = df.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df
