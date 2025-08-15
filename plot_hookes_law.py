# Plotting Force vs. Displacement for a Linear Spring (Hooke's Law)

import numpy as np
import matplotlib.pyplot as plt

# 1. Define displacement array (from 0 to 0.1 meters)
x = np.linspace(0, 0.1, 50)  # 50 points for smooth curve

# 2. Define spring constant
k = 100  # Spring stiffness in N/m

# 3. Calculate force using Hooke's Law: F = k * x
F = k * x  # Force in Newtons corresponding to each displacement

# 4. Plotting
plt.plot(x, F, label='Force vs. Displacement', color='blue', linewidth=2)
plt.xlabel('Displacement (m)')       # x-axis label
plt.ylabel('Force (N)')              # y-axis label
plt.title('Hooke\'s Law for a Spring')  # Plot title
plt.legend()                         # Show legend
plt.grid(True)                        # Add grid lines for readability

# 5. Display the plot
plt.show()
