# Simple Harmonic Motion (SHM) Simulation using ODE Integration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Define the differential equation for SHM
def shm(y, t, omega):
    """
    y: [position, velocity]
    Returns derivatives [dy/dt, dv/dt]
    dv/dt = -omega^2 * position
    """
    return [y[1], -omega**2 * y[0]]

# 2. Initial conditions
y0 = [1, 0]           # Initial position = 1 m, initial velocity = 0 m/s

# 3. Time array for simulation
t = np.linspace(0, 10, 100)  # 0 to 10 seconds, 100 points

# 4. Angular frequency
omega = 1  # rad/s

# 5. Solve the ODE
sol = odeint(shm, y0, t, args=(omega,))

# 6. Plot position vs. time
plt.plot(t, sol[:, 0], label='Position (m)', color='blue', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Simple Harmonic Motion')
plt.grid(True)
plt.legend()
plt.show()
