"""Minimize error of polynomial function using SciPy."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(C, data):  # error function
    """Compute error between given polynomial and observed data.

    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point (x, y)

    Returns error as a single real value.
    """
    # Metric: Sum of squared Y-axis differences
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err


def fit_poly(data, error_func, degree):
    """Fit a polynomial to given data, using a supplied error function.

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a polynomial and observed data

    Returns polynomial that minimizes the error function.
    """
    # Generate initial guess for line model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float64))

    # Plot initial guess (optional)
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), "m--", linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize error function
    result = spo.minimize(
        error_func, Cguess, args=(data,), method="SLSQP", options={"disp": True}
    )
    return np.poly1d(result.x)  # convert optimal result into a poly1d object and return


def test_run():
    # Define original line: 1.x5x^2 - 10x^3 - 5x^2 + 60x + 50
    l_orig = np.float64([1.5, -10, -5, 60, 50])
    print(
        "Original line: C0 = {}, C1 = {}, C2 = {}, C3 = {}, C4 = {}".format(
            l_orig[0], l_orig[1], l_orig[2], l_orig[3], l_orig[4]
        )
    )
    Xorig = np.linspace(0, 10, 21)
    Yorig = (
        l_orig[0] * Xorig**4
        + l_orig[1] * Xorig**3
        + l_orig[2] * Xorig**2
        + l_orig[3] * Xorig
        + l_orig[4]
    )
    plt.plot(Xorig, Yorig, "b--", linewidth=2.0, label="Original line")

    # Generate noisy data points
    noise_sigma = 50.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], "go", label="Data Points")

    # Try to fit a 3rd degree polynomial to this data
    poly_fit = fit_poly(data, error_poly, degree=4)
    print("Fitted Polynomial: {}".format(poly_fit))
    plt.plot(
        data[:, 0],
        np.polyval(poly_fit, data[:, 0]),
        "r--",
        linewidth=2.0,
        label="Fitted Polynomial",
    )

    # Add a legend and show plot
    plt.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    test_run()
