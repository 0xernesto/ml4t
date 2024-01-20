"""Accessing Array Elements"""

import numpy as np


def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # Accessing element at position (3, 2)
    element = a[3, 2]
    print("\na[3, 2]: ", element)

    # Element in defined range
    print("\na[0, 1:3]: ", a[0, 1:3])

    # Top-left corner
    print("\na[0:2, 0:2]: ", a[0:2, 0:2])

    # Slicing
    # Note: Slice n:m:t specifies a range that starts n, and stops before m, in
    print("\na[:, 0:3:2]: ", a[:, 0:3:2])  # will select columns 0, 2 for every row

    # Assigning a value to a particular location
    a[0, 0] = 1
    print("\nModified Array (replaced element a[0, 0]):\n", a)

    # Assigning a single value to an entire row
    a[0, :] = 2
    print("\nModified Array (replaced first row with a single value, 2):\n", a)

    # Assigning a list to a column in an array
    a[:, 3] = [1, 2, 3, 4, 5]
    print("\nModified Array (replaced fourth column with a list):\n", a)


if __name__ == "__main__":
    test_run()
