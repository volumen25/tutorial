"""
Hydrostatic Load Calculator

Calculates the total hydrostatic force on a vertical rectangular bulkhead
submerged in water. The force acts at the centroid of the pressure
distribution.
"""

# ====================================
# INPUT PARAMETERS
# ====================================

bulkhead_width_m = 7.0  # Horizontal width of bulkhead in meters
water_depth_m = 6.0  # Depth of water on one side in meters
water_density_kg_per_m3 = 1000.0  # Density of fresh water (kg/m³)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ====================================
# CALCULATIONS
# ====================================

# Calculate submerged area of bulkhead
submerged_area_m2 = bulkhead_width_m * water_depth_m

# Calculate depth to centroid of pressure distribution
# (for rectangular area, centroid is at half the water depth)
centroid_depth_m = water_depth_m / 2

# Calculate total hydrostatic force using:
# F = ρ · g · h_c · A
# where ρ = water density, g = gravity, h_c = centroid depth, A = area
hydrostatic_force_n = (
    water_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * centroid_depth_m
    * submerged_area_m2
)

# Convert force from Newtons to kilonewtons
hydrostatic_force_kn = hydrostatic_force_n / 1000

# Convert force from kilonewtons to meganewtons for additional output
hydrostatic_force_mn = hydrostatic_force_kn / 1000

# ====================================
# OUTPUT RESULTS
# ====================================

print("=== Hydrostatic Load on Bulkhead ===")
print(f"Bulkhead width         : {bulkhead_width_m} m")
print(f"Water depth            : {water_depth_m} m")
print(f"Submerged area         : {submerged_area_m2:.1f} m²")
print(f"Depth of centroid      : {centroid_depth_m} m")
print(
    f"Total water load       : {hydrostatic_force_kn:,.0f} kN  "
    f"({hydrostatic_force_mn:.3f} MN)"
)
