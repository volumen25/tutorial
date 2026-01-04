#!/usr/bin/env python3
"""
Jib and Tie Force Calculator

Calculates forces in a jib and tie member supporting a vertical load.
Uses the law of sines to solve the force triangle.
"""

import math

# =============================================================================
# INPUT PARAMETERS
# =============================================================================

vertical_load_kn = 15  # Total vertical load in kilonewtons
angle_jib_to_vertical_deg = 40  # Angle between jib and vertical (degrees)
angle_jib_to_tie_deg = 45  # Angle between jib and tie (degrees)

# Calculate the third angle in the force triangle (angles sum to 180°)
angle_tie_to_load_deg = 180 - angle_jib_to_vertical_deg - angle_jib_to_tie_deg

# =============================================================================
# CALCULATIONS
# =============================================================================

# Convert all angles from degrees to radians for trigonometric functions
angle_jib_to_vertical_rad = math.radians(angle_jib_to_vertical_deg)
angle_jib_to_tie_rad = math.radians(angle_jib_to_tie_deg)
angle_tie_to_load_rad = math.radians(angle_tie_to_load_deg)

# Apply the law of sines to find forces in jib and tie:
# F_jib / sin(θ_opposite_jib) = F_tie / sin(θ_opposite_tie) = W / sin(θ_ref)
# where the reference angle is the angle between jib and tie

# Force in jib (compression or tension depending on configuration)
force_jib_kn = (
    vertical_load_kn * math.sin(angle_tie_to_load_rad) / math.sin(angle_jib_to_tie_rad)
)

# Force in tie (tension)
force_tie_kn = (
    vertical_load_kn
    * math.sin(angle_jib_to_vertical_rad)
    / math.sin(angle_jib_to_tie_rad)
)

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print(f"Force in jib: {force_jib_kn:.4f} kN")
print(f"Force in tie: {force_tie_kn:.4f} kN")
