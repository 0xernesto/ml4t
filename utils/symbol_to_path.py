"""Returns the CSV file path for a given asset symbol."""

import os


def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
