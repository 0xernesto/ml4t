"""Maximum Value of a 1D Array."""

import numpy as np


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return np.argmax(a)


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("\nArray:", a)

    # Find the maximum and its index in array
    print("\nMaximum value: ", a.max())
    print("\nIndex of max.: ", get_max_index(a))


if __name__ == "__main__":
    test_run()
