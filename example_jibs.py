import math

"""
Static Force Analysis of a Crane Jib-Tie-Post System

This script calculates the internal angles and member forces in a planar
triangular structure consisting of a jib, tie, and post supporting a vertical
load. The system is modeled as a three-bar truss in equilibrium.

Given dimensions:
- Post (vertical member): 8 m
- Jib (horizontal or inclined member): 13 m
- Tie (diagonal member): 9 m
- Vertical load applied at the jib-tip joint: 20 kN

The law of cosines is used to determine the internal angles, followed by the
law of sines to compute the axial forces in the jib and tie (post force can
be found by vertical equilibrium if needed).
"""

# =============================================================================
# Input Parameters
# =============================================================================

length_post_meters = 8.0  # Length of post (vertical member)
length_jib_meters = 13.0  # Length of jib
length_tie_meters = 9.0  # Length of tie (diagonal)
load_kilonewtons = 20.0  # Vertical load at jib-tip joint

# =============================================================================
# Angle Calculations Using Law of Cosines
# =============================================================================

# Angle opposite the post (at jib-tip joint)
angle_opposite_post_radians = math.acos(
    (length_jib_meters**2 + length_tie_meters**2 - length_post_meters**2)
    / (2 * length_jib_meters * length_tie_meters)
)

# Angle opposite the tie (at base joint)
angle_opposite_tie_radians = math.acos(
    (length_jib_meters**2 + length_post_meters**2 - length_tie_meters**2)
    / (2 * length_jib_meters * length_post_meters)
)

# Angle opposite the jib (at top joint); sum of angles in triangle = π radians
angle_opposite_jib_radians = (
    math.pi - angle_opposite_post_radians - angle_opposite_tie_radians
)

# Convert angles to degrees for reporting
angle_opposite_post_degrees = math.degrees(angle_opposite_post_radians)
angle_opposite_tie_degrees = math.degrees(angle_opposite_tie_radians)
angle_opposite_jib_degrees = math.degrees(angle_opposite_jib_radians)

# =============================================================================
# Force Calculations Using Law of Sines
# =============================================================================

# Force in jib (member opposite angle at top joint)
force_jib_kilonewtons = (
    load_kilonewtons
    * math.sin(angle_opposite_jib_radians)
    / math.sin(angle_opposite_post_radians)
)

# Force in tie (member opposite angle at base joint)
force_tie_kilonewtons = (
    load_kilonewtons
    * math.sin(angle_opposite_tie_radians)
    / math.sin(angle_opposite_post_radians)
)

# =============================================================================
# Output Results
# =============================================================================

print(f"Angle opposite post: {angle_opposite_post_degrees:.4f} degrees")
print(f"Angle opposite tie:  {angle_opposite_tie_degrees:.4f} degrees")
print(f"Angle opposite jib:  {angle_opposite_jib_degrees:.4f} degrees")
print()
print(f"Force in jib (F_J): {force_jib_kilonewtons:.4f} kN")
print(f"Force in tie (F_T): {force_tie_kilonewtons:.4f} kN")
