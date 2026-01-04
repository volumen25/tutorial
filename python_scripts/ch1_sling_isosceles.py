"""
Sling Tension Calculator

Calculates the tension in each sling of a two-sling system
supporting a vertical load, the slings and the beam form
an isosceles triangle.
"""

import math

# =============================================================================
# INPUT PARAMETERS
# =============================================================================

vertical_load_kn = 45  # Total vertical load in kilonewtons
sling_angle_degrees = 50  # Angle each sling makes with horizontal

# =============================================================================
# CALCULATIONS
# =============================================================================

# Convert angle from degrees to radians for trigonometric functions
sling_angle_radians = math.radians(sling_angle_degrees)

# Apply vertical equilibrium equation:
# Sum of vertical forces = 0
# 2 * T * sin(θ) = W
# where T is tension in each sling, θ is angle, W is vertical load
tension_per_sling_kn = vertical_load_kn / (2 * math.sin(sling_angle_radians))

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print(f"Tension in each sling: {tension_per_sling_kn:.4f} kN")
