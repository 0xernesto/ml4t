"""Creating NumPy Arrays"""

import numpy as np

# NOTE: A numpy ndarray is not a Python list. It's type is np.ndarray

# NOTE: The default type of all values in a numpy nd array is float


def test_run():
    # List to 1D array
    print("1D Array:\n", np.array([2, 3, 4]))

    # List of tuples to 2D array
    print("\n2D Array:\n", np.array([(2, 3, 4), (5, 6, 7)]))

    # Empty arrays
    #   - Initializing empty arrays is essentially pre-allocating memory.
    #   - When the size of the array is known in advance, it's more efficient
    #     to pre-allocate an array with np.empty or np.zeros than to extend the
    #     array incrementally, such as using np.append, which incurs additional
    #     performance costs due to repeated memory allocation.
    #
    #   - "Empty" arrays created with np.empty are not actually empty; rather, they
    #     are filled with whatever values happen to already be in the memory allocated
    #     for the array (essentially garbage values). If you need to ensure that the array
    #     is initialized with zeros, use np.zeros instead.
    print("\n5x5 Empty Array:\n", np.empty(5))
    print("\n5x4 Empty Array:\n", np.empty((5, 4)))
    print("\n5x5x3 Empty Array:\n", np.empty((5, 4, 3)))

    # Array of 0s
    # Array of 1s
    print("\n5x4 Array of 0s:\n", np.zeros((5, 4)))

    # Array of 1s
    print("\n5x4 Array of 1s:\n", np.ones((5, 4)))

    # Specifying the datatype
    print("\n5x4 Array of 1s (integers):\n", np.ones((5, 4), dtype=np.int_))


if __name__ == "__main__":
    test_run()
