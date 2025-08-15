# unit_converter.py
from pint import UnitRegistry, UndefinedUnitError, DimensionalityError
import sys

# Common unit aliases for applied mechanics
unit_aliases = {
    # Length / distance
    "m": "meter",
    "meter": "meter",
    "meters": "meter",
    "cm": "centimeter",
    "mm": "millimeter",
    "km": "kilometer",
    "ft": "foot",
    "inch": "inch",
    "in": "inch",
    "mi": "mile",

    # Force
    "n": "newton",
    "newton": "newton",
    "kgf": "kilogram_force",
    "kg_f": "kilogram_force",
    "lbf": "pound_force",
    "lb_f": "pound_force",

    # Pressure / stress
    "pa": "pascal",
    "kpa": "kPa",
    "mpa": "MPa",
    "bar": "bar",
    "psi": "psi",
    "atm": "atm",

    # Energy / work
    "j": "joule",
    "kj": "kilojoule",
    "cal": "calorie",
    "kcal": "kilocalorie",
    "ev": "electronvolt",
    "eV": "electronvolt",

    # Power
    "w": "watt",
    "kw": "kilowatt",
    "hp": "horsepower",

    # Mass
    "kg": "kilogram",
    "g": "gram",
    "lb": "pound",
    "lbs": "pound",
    "t": "ton",
    "slug": "slug",

    # Acceleration
    "m/s^2": "meter/second**2",
    "ft/s^2": "foot/second**2",
    "g": "9.80665*m/s**2",  # gravity acceleration  # noqa: F601

    # Torque / Moment
    "n*m": "newton*meter",
    "lbf*ft": "pound_force*foot",
    "kgf*m": "kilogram_force*meter",

    # Speed / velocity
    "m/s": "meter/second",
    "km/h": "km/h",
    "kph": "km/h",
    "mph": "mile/hour",
    "ft/s": "foot/second",
    "knot": "knot",

    # Temperature
    "degc": "degC",
    "degf": "degF",
    "celsius": "degC",
    "fahrenheit": "degF",
    "k": "kelvin",
    "delta_degC": "delta_degC",
    "delta_degF": "delta_degF"
}

def main():
    ureg = UnitRegistry()
    
    if len(sys.argv) != 4:
        print("Usage: python unit_converter.py <value> <from_unit> <to_unit>\n")
        print("Examples:")
        print("  python unit_converter.py 100 km/h mph")
        print("  python unit_converter.py 16 knot km/h")
        print("  python unit_converter.py 3 m^3/min l/s")
        print("  python unit_converter.py 1000 kg/m^3 g/cm^3")
        print("  python unit_converter.py 7 bar psi")
        print("  python unit_converter.py 12 bar MPa")
        print("  python unit_converter.py 3000 kw hp")
        sys.exit(1)
    
    try:
        value = float(sys.argv[1])
        from_unit = sys.argv[2]
        to_unit = sys.argv[3]
        
        # Apply aliases if any
        from_unit = unit_aliases.get(from_unit.lower(), from_unit)
        to_unit = unit_aliases.get(to_unit.lower(), to_unit)
        
        # Use Quantity for proper temperature and unit handling
        quantity = ureg.Quantity(value, from_unit)
        converted = quantity.to(to_unit)
        
        # Rounded output
        print(f"{value} {from_unit} is {round(converted.magnitude, 4)} {to_unit}")
    
    except (UndefinedUnitError, DimensionalityError) as e:
        print(f"Error: {e}")
        print("Ensure units are valid and compatible (e.g., length to length, pressure to pressure).")
    except ValueError:
        print("Error: The value must be a number.")

if __name__ == "__main__":
    main()