"""
Venturi Meter with Mercury Manometer Calculator

Calculates the actual discharge through a Venturi meter using a mercury
manometer to measure pressure difference. Accounts for the coefficient
of discharge and converts mercury column height to equivalent water head.
"""

import math

# ==================================
# INPUT PARAMETERS
# ==================================

inlet_diameter_m = 0.3  # Inlet diameter in meters
throat_diameter_m = 0.1  # Throat diameter in meters
coefficient_of_discharge = 0.95  # Discharge coefficient (dimensionless)
mercury_column_height_m = 0.250  # Manometer reading in meters of mercury
mercury_specific_gravity = 13.6  # Specific gravity of mercury (water = 1)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ==================================
# CROSS-SECTIONAL AREA CALCULATIONS
# ==================================

# Calculate cross-sectional area at inlet
inlet_area_m2 = math.pi * (inlet_diameter_m**2) / 4

# Calculate cross-sectional area at throat
throat_area_m2 = math.pi * (throat_diameter_m**2) / 4

# ==================================
# EQUIVALENT WATER HEAD CALCULATION
# ==================================

# Convert mercury column height to equivalent water head
# The pressure difference measured by mercury must be converted to
# water equivalent by accounting for the density difference:
# h_water = h_mercury × (SG_mercury - 1)
equivalent_water_head_m = mercury_column_height_m * (mercury_specific_gravity - 1)

# ==================================
# DIAMETER RATIO CALCULATION
# ==================================

# Calculate diameter ratio (beta) for use in discharge equation
diameter_ratio = throat_diameter_m / inlet_diameter_m

# ==================================
# DISCHARGE CALCULATIONS
# ==================================

# Calculate theoretical discharge using Venturi meter equation:
# Q_theoretical = A₂ × √[2gh / (1 - β⁴)]
# where β = D₂/D₁ is the diameter ratio
theoretical_discharge_m3_per_s = throat_area_m2 * math.sqrt(
    (2 * gravitational_acceleration_m_per_s2 * equivalent_water_head_m)
    / (1 - diameter_ratio**4)
)

# Calculate actual discharge accounting for losses:
# Q_actual = Cd × Q_theoretical
actual_discharge_m3_per_s = coefficient_of_discharge * theoretical_discharge_m3_per_s

# ==================================
# OUTPUT RESULTS
# ==================================

print(f"Cross-sectional area at inlet (A1): {inlet_area_m2:.4f} m²")
print(f"Cross-sectional area at throat (A2): {throat_area_m2:.4f} m²")
print(f"Equivalent water head (h_eq): {equivalent_water_head_m:.4f} m")
print(f"Theoretical discharge: {theoretical_discharge_m3_per_s:.4f} m³/s")
print(f"Actual discharge: {actual_discharge_m3_per_s:.4f} m³/s")
