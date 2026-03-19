"""
Ex. 5.18 — Spring-Mass System: Periodic Time and Frequency
"""

import math

# --- Inputs ---
k = 1400        # spring stiffness (N/m)
m = 10          # mass (kg)

# --- Calculations ---
omega = math.sqrt(k / m)    # angular velocity (rad/s)
T     = 2 * math.pi / omega # periodic time (s)
f     = 1 / T               # frequency (Hz)

# --- Output ---
print(f"omega = {omega:.4f} rad/s")
print(f"T     = {T:.4f} s")
print(f"f     = {f:.4f} Hz")