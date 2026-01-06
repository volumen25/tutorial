"""
Structural Force Calculator

Calculates forces in a triangular structure (post, jib, tie) given the
member lengths and applied load. Uses law of cosines to find angles,
then law of sines to determine member forces.
"""

import math

# =============================================================================
# INPUT PARAMETERS
# =============================================================================

post_length_m = 8  # Length of post member in meters
jib_length_m = 13  # Length of jib member in meters
tie_length_m = 9  # Length of tie member in meters
applied_load_kn = 20  # Applied vertical load in kilonewtons

# =============================================================================
# ANGLE CALCULATIONS (LAW OF COSINES)
# =============================================================================

# Calculate angle opposite to post using law of cosines:
# cos(θ_p) = (J² + T² - P²) / (2·J·T)
angle_opposite_post_rad = math.acos(
    (jib_length_m**2 + tie_length_m**2 - post_length_m**2)
    / (2 * jib_length_m * tie_length_m)
)

# Calculate angle opposite to tie using law of cosines:
# cos(θ_t) = (J² + P² - T²) / (2·J·P)
angle_opposite_tie_rad = math.acos(
    (jib_length_m**2 + post_length_m**2 - tie_length_m**2)
    / (2 * jib_length_m * post_length_m)
)

# Calculate angle opposite to jib (angles in triangle sum to π radians)
angle_opposite_jib_rad = math.pi - angle_opposite_post_rad - angle_opposite_tie_rad

# =============================================================================
# FORCE CALCULATIONS (LAW OF SINES)
# =============================================================================

# Apply law of sines to find member forces:
# F_jib / sin(θ_jib) = F_tie / sin(θ_tie) = W / sin(θ_post)

# Force in jib member
force_jib_kn = (
    applied_load_kn
    * math.sin(angle_opposite_jib_rad)
    / math.sin(angle_opposite_post_rad)
)

# Force in tie member
force_tie_kn = (
    applied_load_kn
    * math.sin(angle_opposite_tie_rad)
    / math.sin(angle_opposite_post_rad)
)

# =============================================================================
# CONVERT ANGLES TO DEGREES FOR OUTPUT
# =============================================================================

angle_opposite_post_deg = math.degrees(angle_opposite_post_rad)
angle_opposite_tie_deg = math.degrees(angle_opposite_tie_rad)
angle_opposite_jib_deg = math.degrees(angle_opposite_jib_rad)

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print(f"theta_p = {angle_opposite_post_deg:.4f} degrees")
print(f"theta_t = {angle_opposite_tie_deg:.4f} degrees")
print(f"theta_j = {angle_opposite_jib_deg:.4f} degrees")
print()
print(f"Force in jib (F_J): {force_jib_kn:.4f} kN")
print(f"Force in tie (F_T): {force_tie_kn:.4f} kN")
