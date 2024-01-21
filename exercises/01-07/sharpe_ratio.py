"""Caclulate Sharpe Ratio"""

import os
import sys
import pandas as pd
from math import sqrt

# Get the absolute path of the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from utils.get_adj_close import get_adj_close
from utils.normalize_data import normalize_data


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0, :] = 0  # set daily returns for first row to 0
    return daily_returns


def test_run():
    # Setup
    start_val = 1000000
    start_date = "2009-01-01"
    end_date = "2011-12 -31"
    allocs = [0.4, 0.4, 0.1, 0.1]
    k = 252
    daily_rf = 0
    dates = pd.date_range(start_date, end_date)
    symbols = ["SPY", "XOM", "GOOG", "GLD"]

    # Dataframes
    df = get_adj_close(symbols, dates)
    df_norm = normalize_data(df=df)
    df_alloc = df_norm * allocs
    df_pos_vals = df_alloc * start_val
    port_val = df_pos_vals.sum(axis=1)

    # Portfolio Statistics
    daily_ret = compute_daily_returns(df)
    cum_ret = port_val.iloc[-1] / port_val.iloc[0] - 1
    avg_daily_ret = daily_ret.mean()
    std_daily_ret = daily_ret.std()
    SR = sqrt(k) * avg_daily_ret / std_daily_ret

    # Results
    print("\nStart Date:", start_date)
    print("\nEnd Date:", end_date)
    print("\nSymbols:", symbols)
    print("\nAllocations:", allocs)
    print("\nCummulative Return: ", cum_ret)
    print("\nAverage Daily Return:\n", avg_daily_ret)
    print("\nStandard Deviation of Daily Return (Risk):\n", std_daily_ret)
    print("\nRisk Free Rate:", daily_rf)
    print("\nSharpe Ratio of Daily Returns:\n", SR)
    print("\nInitial Portfolio Value: ", start_val)
    print("\nFinal Portfolio Value: ", port_val.iloc[-1])
    print(
        "\nInsight:\nSince GLD has the highest Sharpe ratio, it yields a higher return per unit of risk than the other assets.\n"
    )


if __name__ == "__main__":
    test_run()
