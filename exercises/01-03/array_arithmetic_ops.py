"""Arithmetic Operations"""

import numpy as np


def test_run():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print("Original array a:\n", a)

    # Multiple a by 2
    print("\nMultiply a by 2:\n", 2 * a)

    # Divide a by 2
    print("\nDivide a by 2:\n", a / 2)

    # Divide a by 2
    print("\nDivide a by 2 float:\n", a / 2.0)

    b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
    print("\nOriginal array b:\n", b)

    # Add the two arrays
    print("\nAdd a + b:\n", a + b)

    # Multiply a and b
    #   - multiply each element in a by the corresponding element in b
    #   - this is called element-wise multiplication, not matrix multiplication
    print("\nMultiply a and b:\n", a * b)

    # Divide a by b
    print("\nDivide a by b:\n", a / b)

    c = np.array([(0, 1, 2, 3, 4), (5, 6, 7, 8, 9)])
    print("\nOriginal array c:\n", c)

    # Multiply b and c
    #   - multiply each element in b by the corresponding element in c
    #   - this is called element-wise multiplication, not matrix multiplication
    print("\nMultiply b and c:\n", b * c)

    # Matrix multiplication of b and transpose of c
    #   - Need to transpose c because the number of columns in b must equal the
    #     number of rows in c
    print("\nMatrix multiplication of b and c:\n", np.dot(b, c.T))


if __name__ == "__main__":
    test_run()
