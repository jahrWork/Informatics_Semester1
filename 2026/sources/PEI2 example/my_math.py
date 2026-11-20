# ****************************************************************************
# MISSION ICARO - EXERCISE 1: MATHEMATICAL NUMERICAL METHODS
# Module: my_math.py
# Description: Reusable numerical mathematics utilities implemented with
#              NumPy and SciPy (linear systems, linear regression, 1D
#              interpolation, vectorized finite differences, numerical
#              integration, and nonlinear root finding).
#              No physical constants or matplotlib code belong in this module.
# ****************************************************************************

from numpy import dot, mean, polyfit, sum, zeros_like
from scipy.linalg import solve
from scipy.interpolate import interp1d
from scipy.integrate import simpson, trapezoid
from scipy.optimize import newton, bisect


def solve_linear_system(matrix_a, vector_b):
    """
    Solve a linear system of equations A * x = b using SciPy LU decomposition.
    """
    return solve(matrix_a, vector_b)


def linear_regression_fit(x_data, y_data):
    """
    Perform ordinary least-squares linear regression (y = slope * x + intercept)
    and proportional least-squares fit through the origin (y = k * x).
    Returns slope, intercept, proportional_slope, and r_squared.
    """
    # Standard linear regression y = m * x + c using numpy.polyfit
    slope, intercept = polyfit(x_data, y_data, 1)

    # Proportional least-squares fit y = k * x (minimizing ||k * x - y||_2^2)
    proportional_slope = dot(x_data, y_data) / dot(x_data, x_data)

    # Coefficient of determination R^2 for the linear fit
    y_pred = slope * x_data + intercept
    ss_res = sum((y_data - y_pred) ** 2)
    ss_tot = sum((y_data - mean(y_data)) ** 2)
    r_squared = 1.0 - (ss_res / ss_tot)

    return slope, intercept, proportional_slope, r_squared


def interpolate_1d(x_nodes, y_nodes, x_eval, kind="cubic"):
    """
    Perform 1D interpolation on discrete data nodes (x_nodes, y_nodes)
    and evaluate at x_eval using scipy.interpolate.interp1d.
    """
    interpolator = interp1d(x_nodes, y_nodes, kind=kind, fill_value="extrapolate")
    return interpolator(x_eval)


def finite_difference_derivative(t_nodes, y_nodes):
    """
    Compute the numerical first derivative dy/dt on a uniform grid using
    vectorized finite differences (no for-loops):
      - Forward finite difference at the left boundary (i = 0)
      - Central finite differences at interior nodes (1 <= i <= N - 1)
      - Backward finite difference at the right boundary (i = N)
    """
    dt = t_nodes[1] - t_nodes[0]
    dy_dt = zeros_like(y_nodes, dtype=float)

    # Forward difference at the initial boundary (index 0)
    dy_dt[0] = (y_nodes[1] - y_nodes[0]) / dt

    # Vectorized central differences at all interior points (indices 1 to N-1)
    dy_dt[1:-1] = (y_nodes[2:] - y_nodes[:-2]) / (2.0 * dt)

    # Backward difference at the final boundary (index N)
    dy_dt[-1] = (y_nodes[-1] - y_nodes[-2]) / dt

    return dy_dt


def integrate_simpson(x_nodes, y_nodes):
    """
    Compute the definite integral of discrete samples y_nodes over x_nodes
    using Simpson's rule (scipy.integrate.simpson).
    """
    return float(simpson(y=y_nodes, x=x_nodes))


def integrate_trapezoidal(x_nodes, y_nodes):
    """
    Compute the definite integral of discrete samples y_nodes over x_nodes
    using the composite trapezoidal rule (scipy.integrate.trapezoid).
    """
    return float(trapezoid(y=y_nodes, x=x_nodes))


def find_root_newton(func, x0, tol=1e-10):
    """
    Find a root of the nonlinear scalar equation func(x) = 0 using
    the Newton-Raphson / secant method from scipy.optimize.newton.
    """
    return float(newton(func, x0=x0, tol=tol))


def find_root_bisection(func, a, b, tol=1e-10):
    """
    Find a root of the nonlinear scalar equation func(x) = 0 inside [a, b]
    using the bisection method from scipy.optimize.bisect.
    """
    return float(bisect(func, a=a, b=b, xtol=tol))
