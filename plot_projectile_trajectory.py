# Simulate projectile motion under gravity using ODE integration

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Define the ODE system for projectile motion
def projectile(y, t, g, theta, v0):
    """
    y = [x, vx, y, vy]
    Returns derivatives [dx/dt, dvx/dt, dy/dt, dvy/dt]
    Assumes no air resistance, constant gravity.
    """
    return [y[1], 0, y[3], -g]  # dx/dt = vx, dvx/dt = 0, dy/dt = vy, dvy/dt = -g

# 2. Initial conditions
theta = np.radians(45)     # Launch angle in radians
v0 = 20                    # Initial speed in m/s
y0 = [0, v0 * np.cos(theta), 0, v0 * np.sin(theta)]  # [x0, vx0, y0, vy0]

# 3. Time array for simulation
t = np.linspace(0, 4, 100)  # 0 to 4 seconds

# 4. Gravity
g = 9.81  # m/s²

# 5. Solve the ODE
sol = odeint(projectile, y0, t, args=(g, theta, v0))

# 6. Plot trajectory (x vs. y)
plt.plot(sol[:, 0], sol[:, 2], color='blue', linewidth=2)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Trajectory')
plt.grid(True)
plt.show()
