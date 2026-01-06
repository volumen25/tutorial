"""
Hydrostatic Thrust Calculator for Gate

Calculates the net horizontal thrust on a vertical gate separating two
different water levels. The net thrust is the difference between forces
from the high and low sides.
"""

# ====================================
# INPUT PARAMETERS
# ====================================

gate_width_m = 4.0  # Width of gate in meters
water_depth_high_side_m = 5.5  # Water depth on higher side in meters
water_depth_low_side_m = 3.5  # Water depth on lower side in meters
water_density_kg_per_m3 = 1000.0  # Density of water (kg/m³)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ====================================
# CALCULATIONS - HIGH SIDE
# ====================================

# Area of gate submerged on high side
area_high_side_m2 = water_depth_high_side_m * gate_width_m

# Depth to centroid of pressure distribution on high side
# (for rectangular area, centroid is at half the water depth)
centroid_depth_high_side_m = water_depth_high_side_m / 2

# Hydrostatic force from high side using F = ρ · g · h_c · A
force_high_side_n = (
    water_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * centroid_depth_high_side_m
    * area_high_side_m2
)

# ====================================
# CALCULATIONS - LOW SIDE
# ====================================

# Area of gate submerged on low side
area_low_side_m2 = water_depth_low_side_m * gate_width_m

# Depth to centroid of pressure distribution on low side
centroid_depth_low_side_m = water_depth_low_side_m / 2

# Hydrostatic force from low side using F = ρ · g · h_c · A
force_low_side_n = (
    water_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * centroid_depth_low_side_m
    * area_low_side_m2
)

# ====================================
# NET THRUST CALCULATION
# ====================================

# Net horizontal thrust (force from high side minus force from low side)
net_thrust_n = force_high_side_n - force_low_side_n

# ====================================
# OUTPUT RESULTS
# ====================================

print("=== Hydrostatic Thrust Calculation ===")
print(
    f"Force from higher side ({water_depth_high_side_m} m): "
    f"{force_high_side_n:.0f} N"
)
print(
    f"Force from lower side  ({water_depth_low_side_m} m): " f"{force_low_side_n:.0f} N"
)
print(f"Net horizontal thrust on gate: {net_thrust_n:.0f} N")
