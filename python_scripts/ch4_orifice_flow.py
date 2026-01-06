"""
Orifice Flow Calculator

Calculates the actual velocity and discharge rate of water escaping
through an orifice under a given head. Uses coefficient of velocity (Cv)
and coefficient of area (Ca) to account for real flow conditions.
"""

import math

# ================================
# INPUT PARAMETERS
# ================================

orifice_diameter_mm = 20  # Orifice diameter in millimeters
head_above_orifice_m = 3  # Height of water above orifice in meters
coefficient_of_velocity = 0.97  # Cv (accounts for velocity reduction)
coefficient_of_area = 0.64  # Ca (accounts for vena contracta)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity
water_density_kg_per_m3 = 1000  # Density of water in kg/m³

# ================================
# UNIT CONVERSIONS AND GEOMETRY
# ================================

# Convert orifice diameter from millimeters to meters
orifice_diameter_m = orifice_diameter_mm / 1000

# Calculate orifice radius
orifice_radius_m = orifice_diameter_m / 2

# Calculate cross-sectional area of orifice
orifice_area_m2 = math.pi * orifice_radius_m**2

# ================================
# VELOCITY CALCULATIONS
# ================================

# Calculate theoretical velocity using Torricelli's theorem: v = √(2gh)
theoretical_velocity_m_per_s = math.sqrt(
    2 * gravitational_acceleration_m_per_s2 * head_above_orifice_m
)

# Calculate actual velocity accounting for friction losses
actual_velocity_m_per_s = coefficient_of_velocity * theoretical_velocity_m_per_s

# ================================
# FLOW RATE CALCULATIONS
# ================================

# Calculate actual volumetric flow rate: Q = Ca · A · v
# (Ca accounts for contraction of jet at vena contracta)
volumetric_flow_rate_m3_per_s = (
    coefficient_of_area * orifice_area_m2 * actual_velocity_m_per_s
)

# Calculate mass flow rate: ṁ = ρ · Q
mass_flow_rate_kg_per_s = water_density_kg_per_m3 * volumetric_flow_rate_m3_per_s

# Convert mass flow rate to per-hour basis
mass_flow_rate_kg_per_hour = mass_flow_rate_kg_per_s * 3600

# Convert mass flow rate to tonnes per hour
mass_flow_rate_tonnes_per_hour = mass_flow_rate_kg_per_hour / 1000

# ================================
# OUTPUT RESULTS
# ================================

print(f"(i) Actual velocity of the water jet: " f"{actual_velocity_m_per_s:.3f} m/s")
print("\n(ii) Quantity of water escaping per hour:")
print(f"    Volume flow rate: {volumetric_flow_rate_m3_per_s:.6f} m³/s")
print(f"    Mass flow rate: {mass_flow_rate_kg_per_s:.4f} kg/s")
print(f"    Mass per hour: {mass_flow_rate_kg_per_hour:.4f} kg/hour")
print(f"    Mass per hour: {mass_flow_rate_tonnes_per_hour:.4f} tonnes/hour")
