"""Operations on Arrays"""

import numpy as np


def test_run():
    np.random.seed(693)  # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random integers in [0, 10)
    print("\nArray:\n", a)

    # Sum of all elements
    print("\nSum of all elements: ", a.sum())

    # Note: axis=0 means sum over columns, axis=1 means sum over rows   xa
    # Iterate over rows, to compute sum of each columns
    print("\nSum of each column:", a.sum(axis=0))

    # Iterate over columns to compute sume of each rows
    print("\nSum of each row: ", a.sum(axis=1))

    # Statistics: min, max, mean (across rows, cols, and overall)
    print("\nMinimum of each colulmn: ", a.min(axis=0))
    print("\nMaximum of each row: ", a.max(axis=1))
    print("\nMean of all elements: ", a.mean())  # leave out axis arg.


if __name__ == "__main__":
    test_run()
