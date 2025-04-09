import numpy as np
from scipy.interpolate import CubicSpline

def lagrange_interpolation(x, y, xi):
    def L(k, x):
        Lk = [(xi - xj) / (x[k] - xj) for j, xj in enumerate(x) if j != k]
        return np.prod(Lk, axis=0)

    yi = np.sum(y[k] * L(k, x) for k in range(len(x)))
    return yi

def spline_interpolation(x, y, xi):
    cs = CubicSpline(x, y)
    return cs(xi)
