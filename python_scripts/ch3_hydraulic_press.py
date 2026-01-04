"""
Hydraulic Press Calculator

Calculates the load capacity of a hydraulic press using Pascal's principle.
Given the force applied to a small piston and the areas of both pistons,
determines the system pressure and the load that can be lifted by the
larger piston.
"""

# ===============================
# INPUT PARAMETERS
# ===============================

small_piston_area_mm2 = 25.0  # Area of small piston in mm²
large_piston_area_mm2 = 100.0  # Area of large piston in mm²
force_on_small_piston_n = 150.0  # Force applied to small piston in N

# ===============================
# UNIT CONVERSIONS
# ===============================

# Convert piston areas from mm² to m² (1 mm² = 10⁻⁶ m²)
small_piston_area_m2 = small_piston_area_mm2 * 1e-6
large_piston_area_m2 = large_piston_area_mm2 * 1e-6

# ===============================
# HYDRAULIC SYSTEM CALCULATIONS
# ===============================

# Calculate system pressure using P = F / A (Pascal's principle)
# Pressure is uniform throughout the hydraulic fluid
system_pressure_pa = force_on_small_piston_n / small_piston_area_m2

# Calculate load carried by large piston using F = P · A
load_on_large_piston_n = system_pressure_pa * large_piston_area_m2

# Convert pressure to MPa for additional output
system_pressure_mpa = system_pressure_pa / 1e6

# ===============================
# OUTPUT RESULTS
# ===============================

print(
    f"System pressure: {system_pressure_pa:.2f} Pa "
    f"(or {system_pressure_mpa:.1f} MPa)"
)
print(f"Load carried by larger piston: {load_on_large_piston_n:.1f} N")
