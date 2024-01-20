"""Array Attributes"""

import numpy as np


def test_run():
    a = np.random.random((5, 4))  # 5x4 array of random numbers
    print("5x4 Array:\n", a)
    print("\nShape: ", a.shape)

    print("\n# of Rows: ", a.shape[0])  # number of rows
    print("\n# of Columns: ", a.shape[1])  # number of columns

    print("\nDimensions: ", len(a.shape))
    print("\n# of Elements: ", a.size)
    print("\nData Type of Elements: ", a.dtype)


if __name__ == "__main__":
    test_run()
