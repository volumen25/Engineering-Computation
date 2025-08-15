# Basic Usage of Pint
from pint import UnitRegistry

ureg = UnitRegistry()

# Define a quantity with units
length = 2.5 * ureg.meter

# Convert to another unit
length_in_feet = length.to(ureg.foot)
print(length_in_feet)  # Output: 8.202099737532808 foot