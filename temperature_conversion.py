# Temperature Conversion

from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity # shorthand

# === Absolute temperature conversions require .to() on a Quantity object ===
t_c = Q_(10, ureg.degC)
t_k = t_c.to(ureg.K)
t_f = t_c.to(ureg.degF)

print("Initial temperature:")
print(f"{t_c} = {t_k} = {t_f:.2f}")

t_c = Q_(5, ureg.degC)
t_k = t_c.to(ureg.K)
t_f = t_c.to(ureg.degF)

print("\nFinal temperature:")
print(f"{t_c} = {t_k} = {t_f:.2f}")

# === Delta temperatures (for differences) ===
delta_c = Q_(5, ureg.delta_degC)
delta_k = delta_c.to(ureg.kelvin)          # Use kelvin for differences
delta_f = delta_c.to(ureg.delta_degF)

print("\nTemperature differences:")
print(f"{delta_c} = {delta_k} = {delta_f}")

# === Difference between two absolute temperatures ===
t1_c = Q_(10, ureg.degC)
t2_c = Q_(5, ureg.degC)

delta_abs_c = t1_c - t2_c                 # 5 degC
delta_abs_k = delta_abs_c.to(ureg.kelvin) # 5 K
delta_abs_f = delta_abs_c.to(ureg.delta_degF) # 9 delta_degF

print("\nOr difference between 10 °C and 5 °C:")
print(f"{delta_abs_c} = {delta_abs_k} = {delta_abs_f}")
