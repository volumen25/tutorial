"""
Rope Tension Calculator (Law of Sines)

Calculates tensions in two ropes supporting a load using the law of sines.
The system forms a triangle where the angles and load are known.
"""

import math

# =============================================================================
# INPUT PARAMETERS
# =============================================================================

vertical_load_kn = 25  # Total vertical load in kilonewtons
angle_opposite_rope2_deg = 32  # Angle opposite to tension T2 (degrees)
angle_opposite_rope1_deg = 42  # Angle opposite to tension T1 (degrees)

# Calculate the third angle of the triangle (angles sum to 180°)
angle_opposite_load_deg = 180 - (angle_opposite_rope2_deg + angle_opposite_rope1_deg)

# =============================================================================
# CALCULATIONS
# =============================================================================

# Convert all angles from degrees to radians for trigonometric functions
angle_opposite_rope2_rad = math.radians(angle_opposite_rope2_deg)
angle_opposite_rope1_rad = math.radians(angle_opposite_rope1_deg)
angle_opposite_load_rad = math.radians(angle_opposite_load_deg)

# Apply the law of sines to find tensions:
# T1 / sin(θ1) = T2 / sin(θ2) = W / sin(θ3)
# where θ1 is opposite T1, θ2 is opposite T2, θ3 is opposite W

# Tension in rope 1 (opposite to angle_opposite_rope1)
tension_rope1_kn = (
    vertical_load_kn
    * math.sin(angle_opposite_rope1_rad)
    / math.sin(angle_opposite_load_rad)
)

# Tension in rope 2 (opposite to angle_opposite_rope2)
tension_rope2_kn = (
    vertical_load_kn
    * math.sin(angle_opposite_rope2_rad)
    / math.sin(angle_opposite_load_rad)
)

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print(f"Tension in rope 1: {tension_rope1_kn:.4f} kN")
print(f"Tension in rope 2: {tension_rope2_kn:.4f} kN")
