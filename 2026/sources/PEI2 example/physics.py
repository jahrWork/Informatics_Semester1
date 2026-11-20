# ****************************************************************************
# MISSION ICARO - EXERCISE 1: PHYSICAL MODEL & AEROSPACE TELEMETRY
# Module: physics.py
# Description: Physical formulation and engineering analysis of the Mission
#              ICARO ballistic trajectory problem (6 sections).
#              Uses numerical solvers imported from my_math.py.
#              No matplotlib imports are used in this module.
# ****************************************************************************

from numpy import array, exp, linspace, max, min, sqrt
from numpy.linalg import norm

from my_math import (
    find_root_bisection,
    find_root_newton,
    finite_difference_derivative,
    integrate_simpson,
    integrate_trapezoidal,
    interpolate_1d,
    linear_regression_fit,
    solve_linear_system,
)


def get_mission_icaro_raw_data():
    """
    Load the raw instrumentation datasets for the Mission ICARO test flight.
    All quantities are expressed in SI units (except sensor voltage in mV).
    """
    # 1. 3D accelerometer coupling matrix and measured voltages (mV)
    m_calib = array([
        [1.05, 0.02, -0.01],
        [0.01, 0.98, 0.03],
        [-0.02, 0.01, 1.02]
    ], dtype=float)
    v_medido = array([15.2, -4.5, 98.1], dtype=float)

    # 2. Wind tunnel test data: Dynamic pressure q (Pa) and Drag Force F_D (N)
    q_tunel = array([500, 1000, 1500, 2000, 2500, 3000], dtype=float)
    f_drag_tunel = array([12.1, 25.3, 37.8, 51.0, 62.5, 76.2], dtype=float)

    # 3. International Standard Atmosphere (ISA): Altitude (m) and Density (kg/m^3)
    altitudes_isa = array([0, 500, 1000, 1500, 2000, 2500], dtype=float)
    densidades_isa = array([1.225, 1.167, 1.112, 1.058, 1.007, 0.957], dtype=float)

    # 4. Radar telemetry: Time (s), Horizontal position X (m), Vertical altitude Y (m)
    t_tel = linspace(0, 8, 17)
    x_tel = array(
        [0, 48, 93, 137, 178, 218, 256, 292, 326, 359, 390, 419, 448, 474, 500, 524, 547],
        dtype=float
    )
    y_tel = array(
        [0, 85, 160, 225, 280, 325, 360, 385, 400, 405, 400, 385, 360, 325, 280, 225, 160],
        dtype=float
    )

    return {
        "m_calib": m_calib,
        "v_medido": v_medido,
        "q_tunel": q_tunel,
        "f_drag_tunel": f_drag_tunel,
        "altitudes_isa": altitudes_isa,
        "densidades_isa": densidades_isa,
        "t_tel": t_tel,
        "x_tel": x_tel,
        "y_tel": y_tel,
    }


def calibrate_launch_accelerometer(m_calib, v_medido):
    """
    Section 1: Launch Pad Calibration (Linear System M * a = V).
    Computes the decoupled initial 3D acceleration vector a = (a_x, a_y, a_z)^T in m/s^2.
    Physical validation: Since M_calib is diagonally dominant (~1.0 on diagonal),
    the resulting accelerations are close in magnitude to V_medido, with a_z ~ 96.5 m/s^2
    (~9.8 g vertical launch acceleration) and small lateral components.
    """
    accel_vector = solve_linear_system(m_calib, v_medido)
    accel_magnitude = float(norm(accel_vector))
    return accel_vector, accel_magnitude


def characterize_aerodynamic_drag(q_tunel, f_drag_tunel):
    """
    Section 2: Aerodynamic Characterization (Linear Regression F_D = (C_D * A) * q).
    Determines the aerodynamic drag area parameter (C_D * A) in m^2 from wind tunnel data.
    Physical validation: At q = 1000 Pa, F_D ~ 25.3 N, so C_D * A ~ 0.0253 m^2,
    which corresponds to a compact atmospheric probe of cross-sectional area ~0.05 m^2
    and drag coefficient C_D ~ 0.5.
    """
    slope, intercept, cd_area_prop, r_squared = linear_regression_fit(q_tunel, f_drag_tunel)
    q_fine = linspace(0.0, max(q_tunel) * 1.1, 100)
    f_drag_fit = cd_area_prop * q_fine
    return {
        "cd_area": float(cd_area_prop),
        "slope_linear": float(slope),
        "intercept_linear": float(intercept),
        "r_squared": float(r_squared),
        "q_fine": q_fine,
        "f_drag_fit": f_drag_fit,
    }


def estimate_apogee_air_density(altitudes_isa, densidades_isa, h_query=405.0):
    """
    Section 3: Local Atmospheric Model (1D Interpolation).
    Estimates the ISA air density rho (kg/m^3) at the radar apogee altitude h = 405 m.
    Physical validation: Since 405 m lies between 0 m (1.225 kg/m^3) and 500 m (1.167 kg/m^3),
    the interpolated density must be ~1.178 kg/m^3.
    """
    rho_apogee_cubic = float(interpolate_1d(altitudes_isa, densidades_isa, h_query, kind="cubic"))
    rho_apogee_linear = float(interpolate_1d(altitudes_isa, densidades_isa, h_query, kind="linear"))
    h_fine = linspace(min(altitudes_isa), max(altitudes_isa), 200)
    rho_fine = interpolate_1d(altitudes_isa, densidades_isa, h_fine, kind="cubic")
    return {
        "h_query": float(h_query),
        "rho_apogee": rho_apogee_cubic,
        "rho_apogee_linear": rho_apogee_linear,
        "h_fine": h_fine,
        "rho_fine": rho_fine,
    }


def compute_flight_kinematics(t_tel, x_tel, y_tel):
    """
    Section 4: Kinematics from Radar Telemetry (Numerical Differentiation).
    Computes horizontal velocity v_x(t), vertical velocity v_y(t), and speed v(t) in m/s.
    Physical validation: Initial launch speed is ~194 m/s (subsonic, Mach ~0.57),
    and vertical velocity crosses zero at apogee (t = 4.5 s, y = 405 m).
    """
    vx = finite_difference_derivative(t_tel, x_tel)
    vy = finite_difference_derivative(t_tel, y_tel)
    speed = sqrt(vx ** 2 + vy ** 2)
    return {
        "vx": vx,
        "vy": vy,
        "speed": speed,
    }


def compute_dissipated_drag_energy(t_tel, speed, cd_area, rho_mean):
    """
    Section 5: Energy Dissipated by the Atmosphere (Numerical Integration).
    Computes W_drag = integral_0^{t_f} (0.5 * rho_mean * (C_D * A) * v(t)^3) dt in Joules (J)
    using both Simpson's rule and the Trapezoidal rule.
    Physical validation: With mean speed ~100 m/s over 8 s and F_D ~ 150 N,
    dissipated mechanical energy is on the order of ~1.35e5 J (~135 kJ).
    """
    drag_force_t = 0.5 * rho_mean * cd_area * (speed ** 2)
    aero_power_t = drag_force_t * speed
    work_simpson = integrate_simpson(t_tel, aero_power_t)
    work_trapezoid = integrate_trapezoidal(t_tel, aero_power_t)
    return {
        "drag_force_t": drag_force_t,
        "aero_power_t": aero_power_t,
        "work_simpson": work_simpson,
        "work_trapezoid": work_trapezoid,
    }


def altitude_descent_model(t, v_descent=35.0):
    """
    Section 6 analytical descent altitude model valid for t > 5 s:
    y(t) = 400 - v_descent * (t - 5) - 150 * exp(-0.2 * (t - 5))
    Default v_descent = 35.0 m/s as given in the problem statement.
    """
    return 400.0 - v_descent * (t - 5.0) - 150.0 * exp(-0.2 * (t - 5.0))


def predict_ground_impact_time(v_descent=35.0):
    """
    Section 6: Ground Impact Prediction (Nonlinear Root Finding y(t) = 0).
    Justification of initial guess and bracketing interval:
      - At t = 8 s (end of radar telemetry), y(8) = 400 - 105 - 150*exp(-0.6) ~ 212.7 m > 0.
      - Neglecting the decaying exponential term for large t, 400 - 35*(t - 5) = 0
        gives an upper asymptotic estimate t ~ 5 + 400/35 = 16.43 s, where y(16.43) < 0.
      - At t = 25 s, y(25) < 0 for all realistic descent speeds.
      - Therefore, the bracket [5.5, 40.0] s guarantees a sign change for Bisection,
        and t0 = 15.0 s is a well-conditioned initial guess for Newton-Raphson.
    """
    target_func = lambda t: altitude_descent_model(t, v_descent=v_descent)
    t_impact_newton = find_root_newton(target_func, x0=15.0, tol=1e-10)
    t_impact_bisect = find_root_bisection(target_func, a=5.5, b=50.0, tol=1e-10)

    t_curve = linspace(5.0, max([t_impact_newton * 1.15, 18.0]), 200)
    y_curve = altitude_descent_model(t_curve, v_descent=v_descent)

    return {
        "v_descent": float(v_descent),
        "t_impact_newton": t_impact_newton,
        "t_impact_bisect": t_impact_bisect,
        "t_curve": t_curve,
        "y_curve": y_curve,
    }


def run_full_mission_analysis():
    """
    Execute all 6 sections of the Mission ICARO ballistic and aerodynamic analysis
    and return a structured dictionary with all numerical results.
    """
    raw = get_mission_icaro_raw_data()

    # Section 1: Launch accelerometer calibration
    accel_vec, accel_norm = calibrate_launch_accelerometer(raw["m_calib"], raw["v_medido"])

    # Section 2: Wind tunnel aerodynamic drag regression
    aero_reg = characterize_aerodynamic_drag(raw["q_tunel"], raw["f_drag_tunel"])

    # Section 3: ISA atmospheric density interpolation at apogee (h = 405 m)
    apogee_alt = float(max(raw["y_tel"]))
    isa_interp = estimate_apogee_air_density(raw["altitudes_isa"], raw["densidades_isa"], h_query=apogee_alt)

    # Section 4: Radar telemetry kinematics via finite differences
    kinematics = compute_flight_kinematics(raw["t_tel"], raw["x_tel"], raw["y_tel"])

    # Section 5: Atmospheric drag dissipated energy via Simpson and Trapezoidal rules
    energy = compute_dissipated_drag_energy(
        raw["t_tel"],
        kinematics["speed"],
        aero_reg["cd_area"],
        isa_interp["rho_apogee"]
    )

    # Section 6: Impact time prediction via Newton-Raphson and Bisection
    impact = predict_ground_impact_time(v_descent=35.0)

    return {
        "raw": raw,
        "sec1": {"accel_vec": accel_vec, "accel_norm": accel_norm},
        "sec2": aero_reg,
        "sec3": isa_interp,
        "sec4": kinematics,
        "sec5": energy,
        "sec6": impact,
    }


def print_physical_report(results):
    """
    Print a formatted engineering report to the console interpreting the physical
    meaning, SI units, and order of magnitude of each numerical result.
    """
    a_vec = results["sec1"]["accel_vec"]
    a_norm = results["sec1"]["accel_norm"]
    cd_a = results["sec2"]["cd_area"]
    r2 = results["sec2"]["r_squared"]
    h_ap = results["sec3"]["h_query"]
    rho_ap = results["sec3"]["rho_apogee"]
    v0 = results["sec4"]["speed"][0]
    v_min = min(results["sec4"]["speed"])
    w_simp = results["sec5"]["work_simpson"]
    w_trap = results["sec5"]["work_trapezoid"]
    t_imp_n = results["sec6"]["t_impact_newton"]
    t_imp_b = results["sec6"]["t_impact_bisect"]

    print("=" * 78)
    print(" MISSION ICARO - FLIGHT DYNAMICS & TELEMETRY ENGINEERING REPORT")
    print("=" * 78)
    print(
        f"[Section 1 - Accelerometer Calibration (Linear System)]\n"
        f"  Decoupled initial acceleration: a = [{a_vec[0]:.4f}, {a_vec[1]:.4f}, {a_vec[2]:.4f}] m/s^2\n"
        f"  Total acceleration magnitude  : |a| = {a_norm:.4f} m/s^2 (~{a_norm / 9.81:.2f} g).\n"
        f"  Physical interpretation       : The probe experiences a strong vertical launch impulse\n"
        f"                                  along Z with minor lateral parasitic accelerations.\n"
    )
    print(
        f"[Section 2 - Aerodynamic Characterization (Linear Regression)]\n"
        f"  Drag area parameter (C_D * A) : {cd_a:.6f} m^2 (R^2 = {r2:.6f})\n"
        f"  Physical interpretation       : Confirming linear dependence of drag on dynamic pressure\n"
        f"                                  in the subsonic regime for the passive aerodynamic brake.\n"
    )
    print(
        f"[Section 3 - Local ISA Atmospheric Model (1D Interpolation)]\n"
        f"  Air density at apogee ({h_ap:.1f} m): rho = {rho_ap:.6f} kg/m^3\n"
        f"  Physical interpretation       : Air density drops by ~3.8% relative to sea level (1.225 kg/m^3),\n"
        f"                                  consistent with the tropospheric scale height.\n"
    )
    print(
        f"[Section 4 - Radar Telemetry Kinematics (Finite Differences)]\n"
        f"  Launch speed v(0)             : {v0:.2f} m/s | Minimum speed near apogee: {v_min:.2f} m/s\n"
        f"  Physical interpretation       : Vertical velocity v_y vanishes at t = 4.5 s (apogee y = 405 m),\n"
        f"                                  while horizontal velocity v_x decays monotonically due to drag.\n"
    )
    print(
        f"[Section 5 - Atmospheric Dissipated Energy (Numerical Integration)]\n"
        f"  Dissipated work (Simpson)     : {w_simp:.2f} J ({w_simp / 1e3:.2f} kJ)\n"
        f"  Dissipated work (Trapezoidal) : {w_trap:.2f} J ({w_trap / 1e3:.2f} kJ)\n"
        f"  Physical interpretation       : The passive aerodynamic brake dissipates ~{w_simp / 1e3:.1f} kJ of\n"
        f"                                  kinetic energy into atmospheric heat during the first 8 s.\n"
    )
    print(
        f"[Section 6 - Ground Impact Prediction (Nonlinear Root Finding)]\n"
        f"  Predicted impact time (Newton): t_impact = {t_imp_n:.6f} s\n"
        f"  Predicted impact time (Bisect): t_impact = {t_imp_b:.6f} s\n"
        f"  Justification of initial guess: Bracket [5.5, 50.0] s encloses the root because y(8) > 0\n"
        f"                                  and the linear asymptote crosses zero at t ~ 16.43 s (t0 = 15.0 s).\n"
    )
    print("=" * 78)
