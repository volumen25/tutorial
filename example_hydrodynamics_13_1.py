import math

# -----------------------------
# Given data
# -----------------------------
internal_diameter_mm = 75  # mm (pipe internal diameter)
velocity_m_per_s = 1.2  # m/s (fluid velocity)
relative_density = 0.9  # relative to water
density_water_kg_per_m3 = 1000  # standard density of water (kg/m³)

# -----------------------------
# Convert units and calculate radius
# -----------------------------
internal_diameter_m = internal_diameter_mm / 1000  # mm → m
radius_m = internal_diameter_m / 2  # pipe radius (m)

# -----------------------------
# Cross-sectional area
# -----------------------------
area_m2 = math.pi * radius_m**2  # m²

# -----------------------------
# Volume and mass flow rates
# -----------------------------
volume_flow_rate_m3_per_s = area_m2 * velocity_m_per_s

# Density of oil (kg/m³)
density_oil_kg_per_m3 = relative_density * density_water_kg_per_m3

# Mass flow rate (kg/s)
mass_flow_rate_kg_per_s = density_oil_kg_per_m3 * volume_flow_rate_m3_per_s

# Mass flow rate in tonnes per hour
mass_flow_rate_tonnes_per_hour = (mass_flow_rate_kg_per_s * 3600) / 1000

# -----------------------------
# Output results
# -----------------------------
print(f"Volume flow rate, m³/s         : {volume_flow_rate_m3_per_s:.4f}")
print(f"Mass flow rate, tonnes/hour    : {mass_flow_rate_tonnes_per_hour:.4f}")
