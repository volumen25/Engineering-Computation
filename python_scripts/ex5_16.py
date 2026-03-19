"""
Ex. 5.16 — Simple Harmonic Motion: Accelerating Forces
"""

import math

# --- Inputs ---
m   = 2.25          # mass (kg)
A   = 380 / 1000    # amplitude (m)
f   = 120 / 60      # frequency (Hz)
x   = 250 / 1000    # displacement (m)

# --- Calculations ---
omega = 2 * math.pi * f         # angular velocity (rad/s)
a_max = omega**2 * A            # maximum acceleration (m/s^2)
F_max = m * a_max               # maximum accelerating force (N)
a_x   = omega**2 * x            # acceleration at x (m/s^2)
F_x   = m * a_x                 # accelerating force at x (N)

# --- Output ---
print(f"omega  = {omega:.4f} rad/s")
print(f"a_max  = {a_max:.4f} m/s^2")
print(f"F_max  = {F_max:.4f} N")
print(f"a_x    = {a_x:.4f} m/s^2")
print(f"F_x    = {F_x:.4f} N")