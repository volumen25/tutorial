"""
Pipe Flow Velocity Calculator

Calculates the mass flow rate and velocities in pipes of different
diameters carrying water at a constant volumetric flow rate. Uses
continuity equation to determine flow velocities.
"""

import math

# ==================================
# INPUT PARAMETERS
# ==================================

volumetric_flow_rate_kl_per_min = 18.4  # Flow rate in kiloliters/min
large_pipe_diameter_mm = 300  # Diameter of larger pipe in millimeters
small_pipe_diameter_mm = 200  # Diameter of smaller pipe in millimeters
water_density_kg_per_m3 = 1000  # Density of water in kg/m³

# ==================================
# UNIT CONVERSIONS
# ==================================

# Convert volumetric flow rate from kL/min to m³/s
# (1 kL = 1 m³, and 1 min = 60 s)
volumetric_flow_rate_m3_per_s = volumetric_flow_rate_kl_per_min / 60

# Convert pipe diameters from millimeters to meters
large_pipe_diameter_m = large_pipe_diameter_mm / 1000
small_pipe_diameter_m = small_pipe_diameter_mm / 1000

# Calculate pipe radii
large_pipe_radius_m = large_pipe_diameter_m / 2
small_pipe_radius_m = small_pipe_diameter_m / 2

# ==================================
# CROSS-SECTIONAL AREA CALCULATIONS
# ==================================

# Calculate cross-sectional area of larger pipe
large_pipe_area_m2 = math.pi * large_pipe_radius_m**2

# Calculate cross-sectional area of smaller pipe
small_pipe_area_m2 = math.pi * small_pipe_radius_m**2

# ==================================
# VELOCITY CALCULATIONS
# ==================================

# Calculate velocity in larger pipe using continuity equation: v = Q / A
velocity_large_pipe_m_per_s = volumetric_flow_rate_m3_per_s / large_pipe_area_m2

# Calculate velocity in smaller pipe using continuity equation: v = Q / A
velocity_small_pipe_m_per_s = volumetric_flow_rate_m3_per_s / small_pipe_area_m2

# ==================================
# MASS FLOW RATE CALCULATION
# ==================================

# Calculate mass flow rate using ṁ = ρ · Q
mass_flow_rate_kg_per_s = water_density_kg_per_m3 * volumetric_flow_rate_m3_per_s

# ==================================
# OUTPUT RESULTS
# ==================================

print(f"Mass flow rate: {mass_flow_rate_kg_per_s:.4f} kg/s")
print(
    f"Velocity in larger pipe ({large_pipe_diameter_mm} mm): "
    f"{velocity_large_pipe_m_per_s:.4f} m/s"
)
print(
    f"Velocity in smaller pipe ({small_pipe_diameter_mm} mm): "
    f"{velocity_small_pipe_m_per_s:.4f} m/s"
)
