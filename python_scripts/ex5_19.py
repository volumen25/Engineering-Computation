"""
Ex. 5.19 — Spring-Mass System with Spring Mass: Frequency and Kinetic Energy
"""

import math

# --- Inputs ---
k   = 532           # spring stiffness (N/m)
m   = 10            # attached mass (kg)
m_s = 6             # spring mass (kg)
A   = 40 / 1000     # amplitude (m)
x   = 30 / 1000     # displacement (m)

# --- Calculations ---
m_eff = m + m_s / 3                     # effective mass (kg)
omega = math.sqrt(k / m_eff)            # angular frequency (rad/s)
f     = omega / (2 * math.pi)           # frequency (Hz)
v     = omega * math.sqrt(A**2 - x**2)  # velocity at x (m/s)
KE    = 0.5 * m * v**2                  # kinetic energy at x (J)

# --- Output ---
print(f"m_eff = {m_eff:.4f} kg")
print(f"omega = {omega:.4f} rad/s")
print(f"f     = {f:.4f} Hz")
print(f"v     = {v:.4f} m/s")
print(f"KE    = {KE:.4f} J")