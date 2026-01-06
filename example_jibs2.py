"""
Crane Force Analysis - Triangle Force Resolution

Calculates the forces in a crane's jib and tie cable given the geometry
and load using the law of cosines and law of sines.
"""

import math

# =============================================================================
# INPUT PARAMETERS - CRANE GEOMETRY AND LOAD
# =============================================================================

# Triangle side lengths (crane structure)
post_length_m = 8  # meters (vertical post)
jib_length_m = 13  # meters (angled support beam)
tie_length_m = 9  # meters (cable connecting jib to post)

# Applied load at the end of the jib
load_force_kn = 20  # kilonewtons

# =============================================================================
# ANGLE CALCULATIONS USING LAW OF COSINES
# =============================================================================

# Calculate angle at the post (opposite to post side)
# Using: cos(θ) = (b² + c² - a²) / (2bc)
angle_at_post_rad = math.acos(
    (jib_length_m**2 + tie_length_m**2 - post_length_m**2)
    / (2 * jib_length_m * tie_length_m)
)

# Calculate angle at the tie connection (opposite to tie side)
angle_at_tie_rad = math.acos(
    (jib_length_m**2 + post_length_m**2 - tie_length_m**2)
    / (2 * jib_length_m * post_length_m)
)

# Calculate angle at the jib tip (opposite to jib side)
# Sum of angles in a triangle equals π radians (180 degrees)
angle_at_jib_rad = math.pi - angle_at_post_rad - angle_at_tie_rad

# =============================================================================
# FORCE CALCULATIONS USING LAW OF SINES
# =============================================================================

# Calculate force in the jib using the law of sines
# F_jib / sin(angle_at_jib) = W / sin(angle_at_post)
force_in_jib_kn = (
    load_force_kn * math.sin(angle_at_jib_rad) / math.sin(angle_at_post_rad)
)

# Calculate force in the tie cable using the law of sines
# F_tie / sin(angle_at_tie) = W / sin(angle_at_post)
force_in_tie_kn = (
    load_force_kn * math.sin(angle_at_tie_rad) / math.sin(angle_at_post_rad)
)

# =============================================================================
# CONVERT ANGLES TO DEGREES FOR OUTPUT
# =============================================================================

angle_at_post_deg = math.degrees(angle_at_post_rad)
angle_at_tie_deg = math.degrees(angle_at_tie_rad)
angle_at_jib_deg = math.degrees(angle_at_jib_rad)

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print("Angle Measurements:")
print(f"  Angle at post (θ_p): {angle_at_post_deg:.4f}°")
print(f"  Angle at tie (θ_t):  {angle_at_tie_deg:.4f}°")
print(f"  Angle at jib (θ_j):  {angle_at_jib_deg:.4f}°")
print()
print("Force Analysis:")
print(f"  Force in jib (F_J): {force_in_jib_kn:.4f} kN")
print(f"  Force in tie (F_T): {force_in_tie_kn:.4f} kN")
