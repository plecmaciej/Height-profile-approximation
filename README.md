# Height Profile Approximation

## Project Overview

The goal of this project is to approximate the elevation profile of a terrain, a crucial task in many fields such as geodesy, civil engineering, and satellite navigation. The height profile approximation involves creating mathematical functions that describe the terrain's elevation changes as a function of distance. This allows for smooth and accurate representations of terrain based on point data.

### Methods Used

This project employs several interpolation methods to approximate the terrain profile:

1. **Lagrange Polynomial Interpolation:**
   This method finds a polynomial that passes through all given data points. The Lagrange interpolating polynomial for a set of points \((x_0, y_0), (x_1, y_1), ..., (x_n, y_n)\) is defined as a sum of basis polynomials that are constructed so that the polynomial value at each data point is equal to the function value at that point. However, this method can suffer from oscillations, especially for large datasets.

2. **Cubic Spline Interpolation:**
   Cubic splines are piecewise polynomial functions that are defined on intervals and joined in such a way that ensures continuity and smoothness across the entire domain. The cubic spline interpolation constructs a piecewise cubic function that is continuously differentiable, making it a popular choice for smooth and stable interpolations.

3. **Chebyshev Nodes:**
   Chebyshev nodes are a set of specially spaced points used to improve interpolation accuracy, especially at the boundaries of the interval. They help minimize the Runge phenomenon, a problem that occurs when using uniformly spaced nodes for polynomial interpolation.

## Project Files

### `data_fetcher.py`
Contains the `load_elevation_data` function that reads elevation data from CSV files and returns the x (distance) and y (elevation) values.

### `analysis.py`
Includes functions to analyze interpolation results, including:
- `analyze_interpolation`: To perform interpolation using Lagrange or cubic spline methods.
- `analyze_interpolation_chebyshev`: To perform interpolation using Lagrange with Chebyshev nodes.

### `interpolation.py`
This file includes the interpolation functions:
- `lagrange_interpolation`: Implements Lagrange interpolation.
- `spline_interpolation`: Implements cubic spline interpolation.

### `main.py`
The main script that loads elevation data, performs interpolation using different methods, and plots the results for each dataset.

## Results and Observations

The project compares the performance of three interpolation methods on different terrain profiles:

- **Mount Everest**: Due to its smooth terrain, polynomial interpolation and cubic spline interpolation produced similar results. The Chebyshev node method improved interpolation at the boundaries, but overall, the cubic spline method proved to be the most reliable.
  
- **Gdańsk Spacerniak**: Despite small jumps in elevation, the terrain profile was difficult to approximate, especially at smaller scales. None of the methods provided precise approximations with the tested number of nodes.

### Key Findings:
- **Lagrange Polynomial Interpolation**: Not suitable for larger datasets or datasets with high variations in elevation due to the Runge phenomenon.
- **Cubic Spline Interpolation**: Provides a smooth and accurate representation, even with a larger number of nodes.
- **Chebyshev Nodes**: Improve interpolation at the boundaries, but with fewer nodes in the middle of the interval, accuracy can decrease.

