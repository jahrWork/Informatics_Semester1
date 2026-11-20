# ****************************************************************************
# MISSION ICARO - EXERCISE 1: FUNCTIONAL UNIT TESTS (MATHEMATICS)
# Module: test_math.py
# Description: Functional unit test suite (no classes) validating the
#              mathematical numerical methods in my_math.py.
# ****************************************************************************

from numpy import array, linspace
from numpy.testing import assert_allclose

import my_math


def test_solve_linear_system():
    """
    Verify linear system solver A * x = b on a 2x2 test case.
    """
    matrix_a = array([[2.0, 1.0], [1.0, 3.0]])
    vector_b = array([5.0, 5.0])
    sol = my_math.solve_linear_system(matrix_a, vector_b)
    assert_allclose(sol, array([2.0, 1.0]), rtol=1e-10, atol=1e-10)


def test_linear_regression_fit():
    """
    Verify ordinary and proportional linear regression on exact linear data.
    """
    x_data = array([1.0, 2.0, 3.0, 4.0])
    y_data = 2.0 * x_data + 3.0
    slope, intercept, _, r_squared = my_math.linear_regression_fit(x_data, y_data)
    assert abs(slope - 2.0) < 1e-10
    assert abs(intercept - 3.0) < 1e-10
    assert abs(r_squared - 1.0) < 1e-10

    _, _, prop_slope, _ = my_math.linear_regression_fit(x_data, 2.5 * x_data)
    assert abs(prop_slope - 2.5) < 1e-10


def test_interpolate_1d():
    """
    Verify 1D cubic interpolation on a quadratic polynomial y = x^2.
    """
    x_nodes = array([0.0, 1.0, 2.0, 3.0])
    y_nodes = x_nodes ** 2
    val = float(my_math.interpolate_1d(x_nodes, y_nodes, 1.5, kind="cubic"))
    assert abs(val - 2.25) < 1e-10


def test_finite_difference_derivative():
    """
    Verify finite-difference derivative across boundaries and interior nodes.
    """
    t_nodes = linspace(0.0, 4.0, 9)
    y_nodes = 3.0 * t_nodes + 2.0
    dy_dt = my_math.finite_difference_derivative(t_nodes, y_nodes)
    assert_allclose(dy_dt, 3.0, rtol=1e-10, atol=1e-10)


def test_numerical_integration():
    """
    Verify Simpson and Trapezoidal integration of y = 3 * x^2 over [0, 1].
    """
    x_nodes = linspace(0.0, 1.0, 11)
    y_nodes = 3.0 * (x_nodes ** 2)
    integral_simpson = my_math.integrate_simpson(x_nodes, y_nodes)
    integral_trapezoid = my_math.integrate_trapezoidal(x_nodes, y_nodes)
    assert abs(integral_simpson - 1.0) < 1e-10
    assert abs(integral_trapezoid - 1.0) < 1e-2


def test_root_finding():
    """
    Verify Newton-Raphson and Bisection root finders on f(x) = x^2 - 4.
    """
    func = lambda x: x ** 2 - 4.0
    root_newton = my_math.find_root_newton(func, x0=1.5, tol=1e-10)
    root_bisect = my_math.find_root_bisection(func, a=0.0, b=3.0, tol=1e-10)
    assert abs(root_newton - 2.0) < 1e-8
    assert abs(root_bisect - 2.0) < 1e-8


def run_all_tests():
    """
    Execute all functional mathematical tests sequentially and print a pass summary.
    """
    test_functions = (
        test_solve_linear_system,
        test_linear_regression_fit,
        test_interpolate_1d,
        test_finite_difference_derivative,
        test_numerical_integration,
        test_root_finding,
    )

    for test_fn in test_functions:
        test_fn()
        print(f"[PASS] {test_fn.__name__}")

    print(f"\nAll {len(test_functions)} math functional tests passed successfully.")


if __name__ == "__main__":
    run_all_tests()
