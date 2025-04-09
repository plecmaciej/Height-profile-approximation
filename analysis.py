import numpy as np
import matplotlib.pyplot as plt
from interpolation import lagrange_interpolation, spline_interpolation


def chebyshev_nodes(a, b, n):
    """Generuje n węzłów Czebyszewa na przedziale [a, b]."""
    i = np.arange(n)
    x = np.cos((2*i + 1) * np.pi / (2*n))
    return 0.5 * (a + b) + 0.5 * (b - a) * x
def analyze_interpolation(x, y, method, filename):
    xi = np.linspace(x[0], x[-1], 1000)

    for num_points in [4, 8, 16]:
        indices = np.round(np.linspace(0, len(x) - 1, num_points)).astype(int)
        x_subset = x[indices]
        y_subset = y[indices]

        if method == 'Lagrange':
            yi = [lagrange_interpolation(x_subset, y_subset, x_) for x_ in xi]
        elif method == 'Spline':
            yi = spline_interpolation(x_subset, y_subset, xi)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'o', label='Punkty węzłowe', color='blue')
        plt.plot(xi, yi, '-', label=f'Interpolacja {method}, {num_points} punktów', color='red')
        plt.scatter(x_subset, y_subset, color='green', zorder=5, label='Punkty interpolacji')

        plt.legend()
        plt.title(f'Interpolacja {method} z {num_points} punktami węzłowymi\n({filename})')
        plt.xlabel('Odległość')
        plt.ylabel('Wysokość')
        plt.grid(True)
        plt.show()

def analyze_interpolation_chebyshev(x, y, filename):
    xi = np.linspace(x[0], x[-1], 1000)

    for num_points in [5, 10, 20]:
        x_chebyshev = chebyshev_nodes(x[0], x[-1], num_points)
        y_chebyshev = np.interp(x_chebyshev, x, y)  # Interpolacja w celu uzyskania wartości y w węzłach Czebyszewa

        yi = [lagrange_interpolation(x_chebyshev, y_chebyshev, x_) for x_ in xi]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'o', label='Punkty węzłowe', color='blue')
        plt.plot(xi, yi, '-', label=f'Interpolacja Lagrange z węzłami Czebyszewa, {num_points} punktów', color='red')
        plt.scatter(x_chebyshev, y_chebyshev, color='green', zorder=5, label='Punkty interpolacji (Czebyszew)')

        plt.legend()
        plt.title(f'Interpolacja Lagrange z węzłami Czebyszewa z {num_points} punktami\n({filename})')
        plt.xlabel('Odległość')
        plt.ylabel('Wysokość')
        plt.grid(True)
        plt.show()