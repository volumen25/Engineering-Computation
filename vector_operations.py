# Vector Operations using NumPy
import numpy as np

# Define two force vectors in 3D space (units: Newtons)
force1 = np.array([10, 20, 0])  # Force vector 1 along x and y directions
force2 = np.array([5, -10, 15]) # Force vector 2 along x, y, and z directions

# 1. Resultant Force
# Vector addition gives the combined effect of both forces
resultant = force1 + force2
print("Resultant Force:", resultant)
# Output: [15 10 15]

# 2. Dot Product
# Measures how much one vector acts in the direction of another
# Often interpreted as work done if one vector is force and the other is displacement
work = np.dot(force1, force2)
print("Dot Product (Work):", work)
# Output: -150

# 3. Cross Product
# Produces a vector perpendicular to both input vectors
# Often used to calculate torque (moment) vector
torque = np.cross(force1, force2)
print("Cross Product (Torque):", torque)
# Output: [ 300 -150 -200]
