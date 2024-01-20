"""Accessing Array Elements Using List of Indices"""

import numpy as np


def test_run():
    a = np.random.rand(5)
    print("Array:\n", a)

    # accessing using list of indices
    indices = np.array([1, 2, 3, 3])
    print("\na[1, 2, 3, 3]:\n", a[indices])

    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print("\nArray:\n", a)

    # calculating mean
    mean = a.mean()
    print("\nMean: ", mean)

    # masking - get all values that are less than mean
    print("\nValues of Array < than mean: ", a[a < mean])

    # masking2 - set all values that are less than mean to mean
    a[a < mean] = mean
    print("\nUpdate Array with mean where value is < than mean:\n", a)


if __name__ == "__main__":
    test_run()
