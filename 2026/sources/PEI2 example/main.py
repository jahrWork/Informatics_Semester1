# ****************************************************************************
# MISSION ICARO - EXERCISE 1: MAIN ENTRY POINT
# Module: main.py
# Description: Entry point that runs the mathematical and physical telemetry
#              analysis (physics.py), prints the physical interpretation report
#              to the console, and launches the interactive Matplotlib GUI
#              dashboard (gui.py).
# ****************************************************************************

import physics
import gui


def main():
    """
    Execute the complete Mission ICARO analysis, print the physical report
    with SI units and engineering interpretation, and open the interactive GUI.
    """
    results = physics.run_full_mission_analysis()
    physics.print_physical_report(results)
    gui.launch_dashboard(results)


if __name__ == "__main__":
    main()
