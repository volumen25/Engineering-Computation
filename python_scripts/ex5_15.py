"""
Ex. 5.15 — Simple Harmonic Motion: Reciprocating Engine Piston
===============================================================
Given the stroke, crank angle, and engine speed, calculate the
velocity and acceleration of the piston (neglecting connecting-rod
angularity).

Formulae
--------
    r       = stroke / 2
    omega   = 2 * pi * rpm / 60
    Vp      = omega * r * sin(theta)
    ap      = omega^2 * r * cos(theta)
"""

import math


def piston_kinematics(
    stroke_mm: float,
    theta_deg: float,
    rpm: float,
) -> dict:
    """
    Calculate piston velocity and acceleration assuming SHM
    (i.e. negligible connecting-rod angularity).

    Parameters
    ----------
    stroke_mm : float
        Full stroke of the piston (mm).
    theta_deg : float
        Crank angle past top dead centre (degrees).
    rpm : float
        Engine speed (rev/min).

    Returns
    -------
    dict with keys:
        r_mm        : crank radius (mm)
        r_m         : crank radius (m)
        omega       : angular velocity (rad/s)
        theta_deg   : crank angle (deg)
        velocity    : piston velocity (m/s)
        acceleration: piston acceleration (m/s^2)
    """
    r_mm      = stroke_mm / 2
    r_m       = r_mm / 1000
    omega     = (2 * math.pi * rpm) / 60
    theta_rad = math.radians(theta_deg)
    velocity  = omega * r_m * math.sin(theta_rad)
    accel     = omega ** 2 * r_m * math.cos(theta_rad)

    return {
        "r_mm":         r_mm,
        "r_m":          r_m,
        "omega":        omega,
        "theta_deg":    theta_deg,
        "velocity":     velocity,
        "acceleration": accel,
    }


def print_solution(results: dict) -> None:
    """Print a formatted step-by-step solution."""
    print("=" * 55)
    print("  Ex. 5.15 — Piston Kinematics (SHM)")
    print("=" * 55)

    print(f"\nStep 1 — Crank Radius")
    print(f"  r = stroke / 2 = {results['r_mm'] * 2:.0f} / 2")
    print(f"  r = {results['r_mm']:.1f} mm  ({results['r_m']:.4f} m)")

    print(f"\nStep 2 — Angular Velocity")
    print(f"  omega = 2 * pi * rpm / 60")
    print(f"  omega = {results['omega']:.2f} rad/s")

    print(f"\nStep 3 — Piston Velocity")
    print(f"  Vp = omega * r * sin(theta)")
    print(f"     = {results['omega']:.2f} * {results['r_m']:.4f} * sin({results['theta_deg']:.1f}°)")
    print(f"  Vp = {results['velocity']:.2f} m/s")

    print(f"\nStep 4 — Piston Acceleration")
    print(f"  ap = omega^2 * r * cos(theta)")
    print(f"     = {results['omega']:.2f}^2 * {results['r_m']:.4f} * cos({results['theta_deg']:.1f}°)")
    print(f"  ap = {results['acceleration']:.2f} m/s^2")

    print("\n" + "=" * 55)


if __name__ == "__main__":

    # --- Problem inputs ---
    STROKE_MM = 500      # mm
    THETA_DEG = 30       # degrees past TDC
    RPM       = 750      # rev/min

    results = piston_kinematics(
        stroke_mm = STROKE_MM,
        theta_deg = THETA_DEG,
        rpm       = RPM,
    )

    print_solution(results)