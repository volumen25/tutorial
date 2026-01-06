"""
Jet Impact Force Calculator

Calculates the force exerted by a water jet impacting a flat plate.
Uses the momentum equation to determine the force based on mass flow
rate and jet velocity.
"""

import math

# ===============================================
# INPUT PARAMETERS
# ===============================================

jet_diameter_m = 0.02  # Diameter of water jet in meters
jet_velocity_m_per_s = 21  # Velocity of water jet in m/s
water_density_kg_per_m3 = 1000  # Density of water in kg/m³

# ===============================================
# CROSS-SECTIONAL AREA AND FLOW RATE CALCULATIONS
# ===============================================

# Calculate cross-sectional area of the jet
jet_cross_sectional_area_m2 = math.pi * (jet_diameter_m**2) / 4

# Calculate volumetric flow rate using Q = A × v
volumetric_flow_rate_m3_per_s = jet_cross_sectional_area_m2 * jet_velocity_m_per_s

# Calculate mass flow rate using ṁ = ρ × Q
mass_flow_rate_kg_per_s = water_density_kg_per_m3 * volumetric_flow_rate_m3_per_s

# ===============================================
# FORCE CALCULATION USING MOMENTUM EQUATION
# ===============================================

# Calculate force on the plate using the momentum equation:
# F = ṁ × Δv
# For a jet hitting a flat plate normally and deflecting at 90°,
# the change in velocity in the normal direction equals the jet velocity:
# F = ṁ × v
force_on_plate_n = mass_flow_rate_kg_per_s * jet_velocity_m_per_s

# ===============================================
# OUTPUT RESULTS
# ===============================================

print(f"Mass flow rate (kg/s): {mass_flow_rate_kg_per_s:.4f}")
print(f"Force on plate (N): {force_on_plate_n:.4f}")
