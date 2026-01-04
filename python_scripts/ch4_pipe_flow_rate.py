"""
Pipe Flow Rate Calculator for Oil

Determines the volumetric and mass flow rates in a pipe carrying oil,
given the internal diameter, fluid velocity, and relative density.
"""

import math

# ==============================
# INPUT PARAMETERS
# ==============================

pipe_internal_diameter_mm = 75.0  # Pipe internal diameter in millimeters
oil_velocity_m_per_s = 1.2  # Average velocity of oil in m/s
oil_relative_density = 0.9  # Specific gravity of oil (relative to water)
water_density_kg_per_m3 = 1000.0  # Density of water in kg/m³

# ==============================
# UNIT CONVERSIONS AND GEOMETRY
# ==============================

# Convert pipe diameter from millimeters to meters
pipe_internal_diameter_m = pipe_internal_diameter_mm / 1000.0

# Calculate pipe radius
pipe_radius_m = pipe_internal_diameter_m / 2.0

# Calculate cross-sectional area of the pipe (circular)
pipe_cross_sectional_area_m2 = math.pi * pipe_radius_m**2

# ==============================
# FLOW RATE CALCULATIONS
# ==============================

# Calculate volumetric flow rate using Q = A · v
volumetric_flow_rate_m3_per_s = pipe_cross_sectional_area_m2 * oil_velocity_m_per_s

# Calculate oil density from relative density
oil_density_kg_per_m3 = oil_relative_density * water_density_kg_per_m3

# Calculate mass flow rate using ṁ = ρ · Q
mass_flow_rate_kg_per_s = oil_density_kg_per_m3 * volumetric_flow_rate_m3_per_s

# Convert mass flow rate to tonnes per hour
mass_flow_rate_tonnes_per_hour = mass_flow_rate_kg_per_s * 3600 / 1000

# ==============================
# OUTPUT RESULTS
# ==============================

print("Pipe Flow Analysis Results:")
print(f"  Volumetric flow rate : {volumetric_flow_rate_m3_per_s:.4f} m³/s")
print(f"  Mass flow rate       : {mass_flow_rate_tonnes_per_hour:.4f} " f"tonnes/hour")
