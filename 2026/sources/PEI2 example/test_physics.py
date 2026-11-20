# ****************************************************************************
# MISSION ICARO - EXERCISE 1: FUNCTIONAL UNIT TESTS (PHYSICS)
# Module: test_physics.py
# Description: Functional unit test suite (no classes) validating the
#              physical telemetry calculations in physics.py.
# ****************************************************************************

from numpy import dot
from numpy.testing import assert_allclose

import physics


def test_section_1_linear_system_calibration():
    """
    Verify that the decoupled acceleration vector satisfies M_calib * a = V_medido.
    """
    raw = physics.get_mission_icaro_raw_data()
    accel_vec, accel_norm = physics.calibrate_launch_accelerometer(
        raw["m_calib"], raw["v_medido"]
    )
    reconstructed_v = dot(raw["m_calib"], accel_vec)
    assert_allclose(reconstructed_v, raw["v_medido"], rtol=1e-10, atol=1e-10)
    assert accel_norm > 90.0


def test_section_2_aerodynamic_regression():
    """
    Verify the least-squares aerodynamic drag area parameter (C_D * A) and R^2.
    """
    raw = physics.get_mission_icaro_raw_data()
    reg = physics.characterize_aerodynamic_drag(raw["q_tunel"], raw["f_drag_tunel"])
    assert abs(reg["cd_area"] - 0.025270) < 1e-5
    assert reg["r_squared"] > 0.999


def test_section_3_isa_interpolation():
    """
    Verify that interpolated air density at h = 405 m lies between 0 m and 500 m ISA values.
    """
    raw = physics.get_mission_icaro_raw_data()
    isa = physics.estimate_apogee_air_density(
        raw["altitudes_isa"], raw["densidades_isa"], h_query=405.0
    )
    assert isa["rho_apogee"] < 1.225
    assert isa["rho_apogee"] > 1.167
    assert abs(isa["rho_apogee"] - 1.1778) < 1e-3


def test_section_4_finite_difference_kinematics():
    """
    Verify vectorized finite-difference velocity calculation and zero vertical speed at apogee.
    """
    raw = physics.get_mission_icaro_raw_data()
    kin = physics.compute_flight_kinematics(raw["t_tel"], raw["x_tel"], raw["y_tel"])
    # At apogee index 9 (t = 4.5 s, y = 405 m), symmetric neighbours y[8]=400 and y[10]=400 give vy = 0
    assert abs(kin["vy"][9]) < 1e-10
    assert len(kin["speed"]) == len(raw["t_tel"])


def test_section_5_dissipated_energy_integration():
    """
    Verify Simpson and Trapezoidal numerical integration of aerodynamic drag power.
    """
    results = physics.run_full_mission_analysis()
    w_simpson = results["sec5"]["work_simpson"]
    w_trapezoid = results["sec5"]["work_trapezoid"]
    assert w_simpson > 1.0e5
    assert abs(w_simpson - w_trapezoid) / w_simpson < 0.05


def test_section_6_impact_root_finding():
    """
    Verify that Newton-Raphson and Bisection converge to the same root y(t_impact) = 0.
    """
    impact = physics.predict_ground_impact_time(v_descent=35.0)
    t_n = impact["t_impact_newton"]
    t_b = impact["t_impact_bisect"]
    assert abs(t_n - t_b) < 1e-7
    assert abs(physics.altitude_descent_model(t_n, 35.0)) < 1e-8


def run_all_tests():
    """
    Execute all functional physics tests sequentially and print a pass summary.
    """
    test_functions = (
        test_section_1_linear_system_calibration,
        test_section_2_aerodynamic_regression,
        test_section_3_isa_interpolation,
        test_section_4_finite_difference_kinematics,
        test_section_5_dissipated_energy_integration,
        test_section_6_impact_root_finding,
    )

    for test_fn in test_functions:
        test_fn()
        print(f"[PASS] {test_fn.__name__}")

    print(f"\nAll {len(test_functions)} physics functional tests passed successfully.")


if __name__ == "__main__":
    run_all_tests()
