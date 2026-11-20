# ****************************************************************************
# MISSION ICARO - EXERCISE 1: INTERACTIVE DASHBOARD (GUI)
# Module: gui.py
# Description: Interactive Graphical User Interface built exclusively with
#              matplotlib and matplotlib.widgets, following the evaluation
#              rubric (Buttons navigation, dynamic Sliders, ax.text results,
#              scientific plots with SI units, grid, and legends).
# ****************************************************************************

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import physics


def launch_dashboard(results):
    """
    Create and display the single-window interactive Matplotlib dashboard
    for Mission ICARO with 6 navigation buttons and 2 real-time sliders.
    """
    fig, ax = plt.subplots(figsize=(12, 7.5))
    fig.canvas.manager.set_window_title("Misión ÍCARO - Dashboard de Telemetría y Dinámica de Vuelo")
    plt.subplots_adjust(left=0.27, right=0.96, top=0.90, bottom=0.22)

    # Mutable state dictionary holding current view index and dynamic parameters
    state = {
        "current_section": 1,
        "h_query": results["sec3"]["h_query"],
        "v_descent": results["sec6"]["v_descent"],
    }

    raw = results["raw"]

    def draw_current_section():
        """
        Clear and redraw the main axes according to the active section
        and current slider parameter values.
        """
        ax.clear()
        sec = state["current_section"]

        if sec == 1:
            # Section 1: 3D Accelerometer Calibration (Linear System)
            a_vec = results["sec1"]["accel_vec"]
            a_norm = results["sec1"]["accel_norm"]
            components = ["$a_x$ (Longitudinal)", "$a_y$ (Lateral)", "$a_z$ (Vertical)"]
            colors = ["#2b5c8f", "#d95f02", "#1b9e77"]

            bars = ax.bar(components, a_vec, color=colors, edgecolor="black", width=0.5, label="Aceleración desacoplada")
            ax.axhline(0.0, color="black", linewidth=0.8)
            ax.set_title("Apartado 1: Calibración de Plataforma de Lanzamiento ($M \\cdot \\vec{a} = \\vec{V}$)", fontsize=12, fontweight="bold")
            ax.set_xlabel("Componentes del Acelerómetro Triaxial", fontsize=11)
            ax.set_ylabel("Aceleración Inicial [$\\mathrm{m/s^2}$]", fontsize=11)
            ax.set_ylim(-20.0, 118.0)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper left")

            for bar, val in zip(bars, a_vec):
                offset = 3.0 if val >= 0 else -7.0
                ax.text(
                    bar.get_x() + bar.get_width() / 2.0,
                    val + offset,
                    f"{val:.2f} $\\mathrm{{m/s^2}}$",
                    ha="center",
                    va="bottom",
                    fontsize=10,
                    fontweight="bold"
                )

            info_text = (
                "RESULTADOS NUMÉRICOS (Sist. Lineal):\n"
                f"• $a_x = {a_vec[0]:.4f}\\ \\mathrm{{m/s^2}}$\n"
                f"• $a_y = {a_vec[1]:.4f}\\ \\mathrm{{m/s^2}}$\n"
                f"• $a_z = {a_vec[2]:.4f}\\ \\mathrm{{m/s^2}}$\n"
                f"• $|\\vec{{a}}| = {a_norm:.4f}\\ \\mathrm{{m/s^2}}$ ({a_norm / 9.81:.2f} g)\n\n"
                "INTERPRETACIÓN FÍSICA:\n"
                "Impulso vertical dominante (~9.8 g) en el\n"
                "lanzamiento con mínimo desvío lateral."
            )
            ax.text(
                0.03, 0.78, info_text,
                transform=ax.transAxes,
                fontsize=9.5,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#f0f4f8", "edgecolor": "#2b5c8f", "alpha": 0.95}
            )

        elif sec == 2:
            # Section 2: Wind Tunnel Aerodynamic Characterization (Linear Regression)
            sec2 = results["sec2"]
            ax.scatter(
                raw["q_tunel"], raw["f_drag_tunel"],
                color="#d95f02", s=65, zorder=5, label="Ensayos Túnel de Viento (Datos)"
            )
            ax.plot(
                sec2["q_fine"], sec2["f_drag_fit"],
                color="#1f77b4", linewidth=2.2,
                label=f"Ajuste Lineal: $F_D = (C_D A) \\cdot q$"
            )
            ax.set_title("Apartado 2: Caracterización Aerodinámica en Túnel de Viento (Regresión)", fontsize=12, fontweight="bold")
            ax.set_xlabel("Presión Dinámica $q = \\frac{1}{2}\\rho v^2$ [$\\mathrm{Pa}$]", fontsize=11)
            ax.set_ylabel("Fuerza de Resistencia Aerodinámica $F_D$ [$\\mathrm{N}$]", fontsize=11)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper left")

            info_text = (
                "RESULTADOS NUMÉRICOS (Mínimos Cuadrados):\n"
                f"• Área de resistencia $(C_D A) = {sec2['cd_area']:.6f}\\ \\mathrm{{m^2}}$\n"
                f"• Pendiente libre $m = {sec2['slope_linear']:.6f}\\ \\mathrm{{m^2}}$\n"
                f"• Ordenada origen $b = {sec2['intercept_linear']:.4f}\\ \\mathrm{{N}}$\n"
                f"• Coef. determinación $R^2 = {sec2['r_squared']:.6f}$\n\n"
                "INTERPRETACIÓN FÍSICA:\n"
                "Comportamiento lineal subsónico del freno\n"
                "aerodinámico pasivo ($C_D A \\approx 0.0253\\ \\mathrm{m^2}$)."
            )
            ax.text(
                0.03, 0.78, info_text,
                transform=ax.transAxes,
                fontsize=9.5,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#fff8f0", "edgecolor": "#d95f02", "alpha": 0.95}
            )

        elif sec == 3:
            # Section 3: Local ISA Atmospheric Model (1D Interpolation with dynamic h_query)
            sec3_dyn = physics.estimate_apogee_air_density(
                raw["altitudes_isa"], raw["densidades_isa"], h_query=state["h_query"]
            )
            ax.plot(
                sec3_dyn["h_fine"], sec3_dyn["rho_fine"],
                color="#1b9e77", linewidth=2.2, label="Interpolante Cúbico ISA $\\rho(h)$"
            )
            ax.scatter(
                raw["altitudes_isa"], raw["densidades_isa"],
                color="black", s=55, zorder=5, label="Tablas Estándar ISA (Nodos)"
            )
            ax.scatter(
                [sec3_dyn["h_query"]], [sec3_dyn["rho_apogee"]],
                color="#e41a1c", s=110, marker="*", zorder=6,
                label=f"Altitud seleccionada ($h = {sec3_dyn['h_query']:.0f}\\ \\mathrm{{m}}$)"
            )
            ax.axvline(sec3_dyn["h_query"], color="#e41a1c", linestyle=":", alpha=0.8)
            ax.axhline(sec3_dyn["rho_apogee"], color="#e41a1c", linestyle=":", alpha=0.8)

            ax.set_title("Apartado 3: Modelo Atmosférico Local ISA (Interpolación 1D Interactiva)", fontsize=12, fontweight="bold")
            ax.set_xlabel("Altitud Geopotencial $h$ [$\\mathrm{m}$]", fontsize=11)
            ax.set_ylabel("Densidad del Aire $\\rho$ [$\\mathrm{kg/m^3}$]", fontsize=11)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper right")

            info_text = (
                "RESULTADOS NUMÉRICOS (Interpolación 1D):\n"
                f"• Altitud consultada: $h = {sec3_dyn['h_query']:.1f}\\ \\mathrm{{m}}$\n"
                f"• Densidad (Cúbica): $\\rho = {sec3_dyn['rho_apogee']:.6f}\\ \\mathrm{{kg/m^3}}$\n"
                f"• Densidad (Lineal): $\\rho = {sec3_dyn['rho_apogee_linear']:.6f}\\ \\mathrm{{kg/m^3}}$\n"
                f"• En apogeo ($405\\ \\mathrm{{m}}$): $\\rho = {results['sec3']['rho_apogee']:.6f}\\ \\mathrm{{kg/m^3}}$\n\n"
                "INTERPRETACIÓN FÍSICA:\n"
                "Usa el Slider 'Altitud h [m]' inferior para\n"
                "explorar la caída de densidad troposférica."
            )
            ax.text(
                0.03, 0.48, info_text,
                transform=ax.transAxes,
                fontsize=9.5,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#f0fff8", "edgecolor": "#1b9e77", "alpha": 0.95}
            )

        elif sec == 4:
            # Section 4: Kinematics from Radar Telemetry (Numerical Differentiation)
            t_tel = raw["t_tel"]
            vx = results["sec4"]["vx"]
            vy = results["sec4"]["vy"]
            speed = results["sec4"]["speed"]

            ax.plot(t_tel, vx, "o--", color="#1f77b4", linewidth=1.8, label="Velocidad horizontal $v_x(t)$ [$\\mathrm{m/s}$]")
            ax.plot(t_tel, vy, "s--", color="#ff7f0e", linewidth=1.8, label="Velocidad vertical $v_y(t)$ [$\\mathrm{m/s}$]")
            ax.plot(t_tel, speed, "d-", color="#2ca02c", linewidth=2.4, label="Módulo velocidad $v(t) = \\sqrt{v_x^2 + v_y^2}$ [$\\mathrm{m/s}$]")
            ax.axhline(0.0, color="black", linewidth=0.8, linestyle=":")
            ax.axvline(4.5, color="#e41a1c", linewidth=1.2, linestyle="--", label="Instante de Apogeo ($t = 4.5\\ \\mathrm{s}$, $v_y = 0$)")

            ax.set_title("Apartado 4: Cinemática de la Sonda por Diferencias Finitas", fontsize=12, fontweight="bold")
            ax.set_xlabel("Tiempo de Telemetría $t$ [$\\mathrm{s}$]", fontsize=11)
            ax.set_ylabel("Velocidad [$\\mathrm{m/s}$]", fontsize=11)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper right", fontsize=9)

            info_text = (
                "RESULTADOS NUMÉRICOS (Diferencias Finitas):\n"
                f"• Velocidad inicial $v(0) = {speed[0]:.2f}\\ \\mathrm{{m/s}}$\n"
                f"  ($v_x(0) = {vx[0]:.1f}\\ \\mathrm{{m/s}}$, $v_y(0) = {vy[0]:.1f}\\ \\mathrm{{m/s}}$)\n"
                f"• Velocidad en apogeo ($t=4.5\\ \\mathrm{{s}}$): $v = {speed[9]:.2f}\\ \\mathrm{{m/s}}$\n"
                f"  ($v_x = {vx[9]:.1f}\\ \\mathrm{{m/s}}$, $v_y = {vy[9]:.1f}\\ \\mathrm{{m/s}}$)\n"
                f"• Velocidad en $t=8.0\\ \\mathrm{{s}}$: $v(8) = {speed[-1]:.2f}\\ \\mathrm{{m/s}}$\n\n"
                "INTERPRETACIÓN FÍSICA:\n"
                "$v_y$ se anula e invierte signo en el apogeo;\n"
                "$v_x$ decrece continuamente por el drag."
            )
            ax.text(
                0.03, 0.47, info_text,
                transform=ax.transAxes,
                fontsize=9.2,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#f4f8ff", "edgecolor": "#1f77b4", "alpha": 0.95}
            )

        elif sec == 5:
            # Section 5: Atmospheric Dissipated Energy (Numerical Integration)
            sec3_dyn = physics.estimate_apogee_air_density(
                raw["altitudes_isa"], raw["densidades_isa"], h_query=state["h_query"]
            )
            sec5_dyn = physics.compute_dissipated_drag_energy(
                raw["t_tel"],
                results["sec4"]["speed"],
                results["sec2"]["cd_area"],
                sec3_dyn["rho_apogee"]
            )
            t_tel = raw["t_tel"]
            power_kw = sec5_dyn["aero_power_t"] / 1000.0

            ax.plot(t_tel, power_kw, "o-", color="#9467bd", linewidth=2.2, label="Potencia disipada $P_D(t) = F_D(t)\\cdot v(t)$ [$\\mathrm{kW}$]")
            ax.fill_between(
                t_tel, 0.0, power_kw,
                color="#9467bd", alpha=0.25,
                label=f"Trabajo disipado $W_{{drag}} = \\int P_D(t)\\,dt = {sec5_dyn['work_simpson'] / 1e3:.2f}\\ \\mathrm{{kJ}}$"
            )
            ax.set_title("Apartado 5: Energía Disipada por la Atmósfera (Regla de Simpson y Trapecios)", fontsize=12, fontweight="bold")
            ax.set_xlabel("Tiempo de Vuelo $t$ [$\\mathrm{s}$]", fontsize=11)
            ax.set_ylabel("Potencia Aerodinámica Disipada $P_D$ [$\\mathrm{kW}$]", fontsize=11)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper right")

            info_text = (
                f"RESULTADOS NUMÉRICOS ($\\rho(h={state['h_query']:.0f}\\,\\mathrm{{m}}) = {sec3_dyn['rho_apogee']:.4f}\\,\\mathrm{{kg/m^3}}$):\n"
                f"• Trabajo (Simpson 1/3) : $W_{{drag}} = {sec5_dyn['work_simpson']:.2f}\\ \\mathrm{{J}}$ ({sec5_dyn['work_simpson'] / 1e3:.2f} kJ)\n"
                f"• Trabajo (Trapecios)   : $W_{{drag}} = {sec5_dyn['work_trapezoid']:.2f}\\ \\mathrm{{J}}$ ({sec5_dyn['work_trapezoid'] / 1e3:.2f} kJ)\n"
                f"• Valor nominal ($h=405\\,\\mathrm{{m}}$): ${results['sec5']['work_simpson']:.2f}\\ \\mathrm{{J}}$\n\n"
                "INTERPRETACIÓN FÍSICA:\n"
                "La mayor disipación ocurre en el lanzamiento ($v^3$).\n"
                "El Slider 'Altitud h [m]' actualiza $\\rho_{media}$ y $W_{drag}$."
            )
            ax.text(
                0.28, 0.78, info_text,
                transform=ax.transAxes,
                fontsize=9.3,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#f9f2ff", "edgecolor": "#9467bd", "alpha": 0.95}
            )

        elif sec == 6:
            # Section 6: Ground Impact Prediction (Nonlinear Root Finding with dynamic v_descent)
            sec6_dyn = physics.predict_ground_impact_time(v_descent=state["v_descent"])
            t_imp = sec6_dyn["t_impact_newton"]

            ax.plot(
                raw["t_tel"], raw["y_tel"],
                "o--", color="#1f77b4", alpha=0.75, label="Telemetría Radar $y_{tel}(t)$ ($0 \\leq t \\leq 8\\ \\mathrm{s}$)"
            )
            ax.plot(
                sec6_dyn["t_curve"], sec6_dyn["y_curve"],
                "-", color="#d62728", linewidth=2.4,
                label=f"Modelo descenso ($t > 5\\ \\mathrm{{s}}$, $v_{{desc}} = {state['v_descent']:.1f}\\ \\mathrm{{m/s}}$)"
            )
            ax.axhline(0.0, color="black", linewidth=1.1, linestyle="-")
            ax.scatter(
                [t_imp], [0.0],
                color="#d62728", s=120, zorder=6, marker="X",
                label=f"Impacto en suelo: $t_{{impacto}} = {t_imp:.4f}\\ \\mathrm{{s}}$"
            )
            ax.axvline(t_imp, color="#d62728", linestyle=":", alpha=0.8)

            ax.set_title("Apartado 6: Predicción del Instante de Impacto (Newton-Raphson / Bisección)", fontsize=12, fontweight="bold")
            ax.set_xlabel("Tiempo $t$ [$\\mathrm{s}$]", fontsize=11)
            ax.set_ylabel("Altitud de la Sonda $y(t)$ [$\\mathrm{m}$]", fontsize=11)
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend(loc="upper right", fontsize=9.2)

            info_text = (
                "RESULTADOS NUMÉRICOS (Búsqueda de Raíces $y(t)=0$):\n"
                f"• Parámetro Slider $v_{{desc}} = {state['v_descent']:.2f}\\ \\mathrm{{m/s}}$ (Nominal: $35.0\\ \\mathrm{{m/s}}$)\n"
                f"• Raíz Newton-Raphson ($t_0=15\\,\\mathrm{{s}}$) : $t_{{impacto}} = {sec6_dyn['t_impact_newton']:.6f}\\ \\mathrm{{s}}$\n"
                f"• Raíz Bisección ($[5.5, 50.0]\\,\\mathrm{{s}}$): $t_{{impacto}} = {sec6_dyn['t_impact_bisect']:.6f}\\ \\mathrm{{s}}$\n"
                f"• Impacto nominal ($v_{{desc}}=35\\,\\mathrm{{m/s}}$): $t_{{impacto}} = {results['sec6']['t_impact_newton']:.4f}\\ \\mathrm{{s}}$\n\n"
                "JUSTIFICACIÓN FÍSICA DEL PUNTO INICIAL:\n"
                "En $t=8\\,\\mathrm{s}$ la sonda aún está a $y>0$, y la asíntota lineal\n"
                "cruza el suelo en $t \\approx 5 + 400/35 = 16.43\\,\\mathrm{s}$ ($t_0 = 15\\,\\mathrm{s}$)."
            )
            ax.text(
                0.03, 0.46, info_text,
                transform=ax.transAxes,
                fontsize=9.0,
                verticalalignment="top",
                bbox={"boxstyle": "round,pad=0.5", "facecolor": "#fff0f0", "edgecolor": "#d62728", "alpha": 0.95}
            )

        fig.canvas.draw_idle()

    # ------------------------------------------------------------------------
    # Left Panel: Navigation Buttons for the 6 Sections
    # ------------------------------------------------------------------------
    button_labels = [
        (1, "1. Acelerómetro\n(Sistema Lineal)"),
        (2, "2. Túnel de Viento\n(Regresión Lineal)"),
        (3, "3. Atmósfera ISA\n(Interpolación 1D)"),
        (4, "4. Cinemática Radar\n(Derivación DF)"),
        (5, "5. Energía Disipada\n(Integración)"),
        (6, "6. Predicción Impacto\n(Raíces No Lineales)"),
    ]

    buttons = []
    for idx, (sec_num, label) in enumerate(button_labels):
        y_pos = 0.80 - idx * 0.115
        btn_ax = plt.axes([0.03, y_pos, 0.18, 0.095])
        btn = Button(btn_ax, label, color="#e6eef8", hovercolor="#b8d4f2")

        def make_callback(target_section):
            def on_click(event):
                state["current_section"] = target_section
                draw_current_section()
            return on_click

        btn.on_clicked(make_callback(sec_num))
        buttons.append(btn)

    # ------------------------------------------------------------------------
    # Bottom Panel: Interactive Sliders for Real-Time Recalculation
    # ------------------------------------------------------------------------
    ax_slider_h = plt.axes([0.33, 0.10, 0.58, 0.03], facecolor="#e8f8f0")
    slider_h = Slider(
        ax_slider_h,
        "Altitud h [m] (Ap. 3 y 5)",
        0.0,
        2500.0,
        valinit=state["h_query"],
        valstep=5.0,
        color="#1b9e77"
    )

    ax_slider_v = plt.axes([0.33, 0.04, 0.58, 0.03], facecolor="#fde8e8")
    slider_v = Slider(
        ax_slider_v,
        "Vel. Caída [m/s] (Ap. 6)",
        15.0,
        60.0,
        valinit=state["v_descent"],
        valstep=0.5,
        color="#d62728"
    )

    def on_slider_h_changed(val):
        state["h_query"] = float(val)
        if state["current_section"] not in (3, 5):
            state["current_section"] = 3
        draw_current_section()

    def on_slider_v_changed(val):
        state["v_descent"] = float(val)
        if state["current_section"] != 6:
            state["current_section"] = 6
        draw_current_section()

    slider_h.on_changed(on_slider_h_changed)
    slider_v.on_changed(on_slider_v_changed)

    # Initial render
    draw_current_section()
    plt.show()
