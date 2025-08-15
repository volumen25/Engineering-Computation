# Plot a typical stress-strain curve for steel (elastic + plastic behavior)

import numpy as np
import matplotlib.pyplot as plt

# 1. Define strain array (dimensionless)
# Small values since steel deforms elastically up to ~0.2% strain
strain = np.linspace(0, 0.015, 100)  # 0 to 1.5% strain

# 2. Material properties
E = 200_000         # Young's modulus in MPa (elastic stiffness)
yield_strain = 0.002  # Approximate yield strain (0.2%)
yield_stress = E * yield_strain  # Stress at yield (MPa)

# 3. Stress-strain relationship
# Linear elastic region: stress = E * strain
# Plastic region: stress increases at lower slope (simplified hardening)
stress = np.where(
    strain <= yield_strain,
    E * strain,                       # Elastic region
    yield_stress + 10_000 * (strain - yield_strain)  # Plastic region with hardening
)

# 4. Plotting the curve
plt.plot(strain, stress, color='blue', linewidth=2, label='Steel Stress-Strain')
plt.xlabel('Strain (dimensionless)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve for Steel')

# Mark the yield point
plt.axvline(x=yield_strain, color='red', linestyle='--', label='Yield Point')

plt.legend()
plt.grid(True)  # Show grid for better readability
plt.show()
