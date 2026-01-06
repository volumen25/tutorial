"""
Venturi Meter Flow Calculator

Calculates the flow rate through a Venturi meter using Bernoulli's
equation. Determines throat velocity and volumetric/mass flow rates
from the pressure differential between inlet and throat sections.
"""

import math

# ===============================================
# INPUT PARAMETERS
# ===============================================

inlet_diameter_m = 0.450  # Inlet diameter in meters
throat_diameter_m = 0.225  # Throat diameter in meters
pressure_head_difference_m = 0.381  # Pressure head difference in meters
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity
water_density_kg_per_m3 = 1000  # Density of water in kg/m³

# ===============================================
# CROSS-SECTIONAL AREA CALCULATIONS
# ===============================================

# Calculate cross-sectional area at inlet
inlet_area_m2 = math.pi * (inlet_diameter_m / 2) ** 2

# Calculate cross-sectional area at throat
throat_area_m2 = math.pi * (throat_diameter_m / 2) ** 2

# ===============================================
# VELOCITY CALCULATION USING BERNOULLI'S EQUATION
# ===============================================

# Compute the squared area ratio (A_throat / A_inlet)²
area_ratio_squared = (throat_area_m2 / inlet_area_m2) ** 2

# Calculate throat velocity using Bernoulli's equation for a Venturi meter:
# c₂ = √[2gh / (1 - (A₂/A₁)²)]
# where h is the pressure head difference
throat_velocity_m_per_s = math.sqrt(
    (2 * gravitational_acceleration_m_per_s2 * pressure_head_difference_m)
    / (1 - area_ratio_squared)
)

# ===============================================
# FLOW RATE CALCULATIONS
# ===============================================

# Calculate volumetric flow rate using Q = A · v at throat section
volumetric_flow_rate_m3_per_s = throat_area_m2 * throat_velocity_m_per_s

# Calculate mass flow rate using ṁ = ρ · Q
mass_flow_rate_kg_per_s = water_density_kg_per_m3 * volumetric_flow_rate_m3_per_s

# ===============================================
# OUTPUT RESULTS
# ===============================================

print(f"Entrance area: {inlet_area_m2:.6f} m²")
print(f"Throat area: {throat_area_m2:.6f} m²")
print(f"Throat velocity: {throat_velocity_m_per_s:.4f} m/s")
print(f"Volumetric flow rate: {volumetric_flow_rate_m3_per_s:.4f} m³/s")
print(f"Mass flow rate: {mass_flow_rate_kg_per_s:.4f} kg/s")
