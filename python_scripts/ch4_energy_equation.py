"""
Energy Equation Pressure Calculator

Calculates the pressure at a higher elevation in a pipe using the energy
equation. Accounts for changes in velocity, elevation, and pressure between
two sections of a pipe carrying water.
"""

import math

# ===========================================
# INPUT PARAMETERS
# ===========================================

volumetric_flow_rate_l_per_min = 2000.0  # Flow rate in liters per minute
diameter_lower_section_m = 0.10  # Pipe diameter at lower section in meters
diameter_upper_section_m = 0.03  # Pipe diameter at upper section in meters
elevation_lower_section_m = 30.0  # Elevation at lower section in meters
elevation_upper_section_m = 36.0  # Elevation at upper section in meters
pressure_lower_section_pa = 6.5e6  # Pressure at lower section in Pascals
water_density_kg_per_m3 = 1000.0  # Density of water in kg/m³
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ===========================================
# UNIT CONVERSIONS
# ===========================================

# Convert volumetric flow rate from L/min to m³/s
# (1 L = 0.001 m³, 1 min = 60 s)
volumetric_flow_rate_m3_per_s = volumetric_flow_rate_l_per_min / 60000.0

# ===========================================
# CROSS-SECTIONAL AREA CALCULATIONS
# ===========================================

# Calculate cross-sectional area at lower section
area_lower_section_m2 = math.pi * (diameter_lower_section_m / 2.0) ** 2

# Calculate cross-sectional area at upper section
area_upper_section_m2 = math.pi * (diameter_upper_section_m / 2.0) ** 2

# ===========================================
# VELOCITY CALCULATIONS
# ===========================================

# Calculate velocity at lower section using continuity equation: v = Q / A
velocity_lower_section_m_per_s = volumetric_flow_rate_m3_per_s / area_lower_section_m2

# Calculate velocity at upper section using continuity equation: v = Q / A
velocity_upper_section_m_per_s = volumetric_flow_rate_m3_per_s / area_upper_section_m2

# ===========================================
# PRESSURE CALCULATION USING ENERGY EQUATION
# ===========================================

# Apply the energy equation between lower and upper sections:
# P₁ + ½ρv₁² + ρgz₁ = P₂ + ½ρv₂² + ρgz₂
# Solving for P₂:
# P₂ = P₁ + ½ρ(v₁² - v₂²) + ρg(z₁ - z₂)

pressure_upper_section_pa = (
    pressure_lower_section_pa
    + 0.5
    * water_density_kg_per_m3
    * (velocity_lower_section_m_per_s**2 - velocity_upper_section_m_per_s**2)
    + water_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * (elevation_lower_section_m - elevation_upper_section_m)
)

# Convert pressure to MPa for output
pressure_upper_section_mpa = pressure_upper_section_pa / 1e6

# ===========================================
# OUTPUT RESULTS
# ===========================================

print(f"Flow rate: {volumetric_flow_rate_m3_per_s:.5f} m³/s")
print(f"Area 1: {area_lower_section_m2:.6f} m²")
print(f"Area 2: {area_upper_section_m2:.6f} m²")
print(f"Velocity 1: {velocity_lower_section_m_per_s:.4f} m/s")
print(f"Velocity 2: {velocity_upper_section_m_per_s:.4f} m/s")
print(
    f"Pressure at {elevation_upper_section_m} m elevation: "
    f"{pressure_upper_section_mpa:.4f} MPa"
)
