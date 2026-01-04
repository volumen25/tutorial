"""
Dock Gate Hydrostatic Thrust Calculator

Calculates the net horizontal thrust on a vertical dock gate separating
two different water levels. Accounts for seawater density and provides
results in multiple units (N, kN, MN).
"""

# =====================================
# INPUT PARAMETERS
# =====================================

gate_width_m = 12.0  # Width of dock gate in meters
water_depth_deep_side_m = 9.0  # Water depth on deeper side in meters
water_depth_shallow_side_m = 4.5  # Water depth on shallower side in meters
seawater_density_kg_per_m3 = 1025.0  # Density of seawater (kg/m³)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# =====================================
# CALCULATIONS - DEEPER SIDE
# =====================================

# Area of gate submerged on deeper side
area_deep_side_m2 = water_depth_deep_side_m * gate_width_m

# Depth to centroid of pressure distribution on deeper side
# (for rectangular area, centroid is at half the water depth)
centroid_depth_deep_side_m = water_depth_deep_side_m / 2

# Hydrostatic force from deeper side using F = ρ · g · h_c · A
force_deep_side_n = (
    seawater_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * centroid_depth_deep_side_m
    * area_deep_side_m2
)

# =====================================
# CALCULATIONS - SHALLOWER SIDE
# =====================================

# Area of gate submerged on shallower side
area_shallow_side_m2 = water_depth_shallow_side_m * gate_width_m

# Depth to centroid of pressure distribution on shallower side
centroid_depth_shallow_side_m = water_depth_shallow_side_m / 2

# Hydrostatic force from shallower side using F = ρ · g · h_c · A
force_shallow_side_n = (
    seawater_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * centroid_depth_shallow_side_m
    * area_shallow_side_m2
)

# =====================================
# NET THRUST CALCULATION
# =====================================

# Net horizontal thrust (force from deep side minus force from shallow side)
net_thrust_n = force_deep_side_n - force_shallow_side_n

# Convert forces to additional units for output
force_deep_side_mn = force_deep_side_n / 1e6
force_shallow_side_mn = force_shallow_side_n / 1e6
net_thrust_kn = net_thrust_n / 1000
net_thrust_mn = net_thrust_n / 1e6

# =====================================
# OUTPUT RESULTS
# =====================================

print("=== Dock Gate Hydrostatic Thrust Calculation ===")
print(
    f"Force from {water_depth_deep_side_m} m side : "
    f"{force_deep_side_n:,.0f} N  ({force_deep_side_mn:.3f} MN)"
)
print(
    f"Force from {water_depth_shallow_side_m} m side : "
    f"{force_shallow_side_n:,.0f} N  ({force_shallow_side_mn:.3f} MN)"
)
print(
    f"Resultant horizontal thrust: {net_thrust_n:,.0f} N  "
    f"({net_thrust_kn:.1f} kN or {net_thrust_mn:.3f} MN)"
)
