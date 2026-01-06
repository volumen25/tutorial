"""
Calculates the resultant speed and direction of a ship moving through
a current using vector addition and the law of cosines.
"""

import math

# =============================================================================
# INPUT PARAMETERS
# =============================================================================

# Ship velocity (due east)
ship_velocity_knots = 18  # knots

# Current velocity
current_velocity_knots = 3  # knots

# Angle between ship heading and current direction
angle_between_vectors_deg = 50  # degrees

# =============================================================================
# VECTOR CALCULATION
# =============================================================================

# Convert angle from degrees to radians for trigonometric calculations
angle_between_vectors_rad = math.radians(angle_between_vectors_deg)

# Calculate resultant velocity magnitude using the law of cosines
# R² = V₁² + V₂² + 2·V₁·V₂·cos(θ)
resultant_velocity_knots = math.sqrt(
    ship_velocity_knots**2
    + current_velocity_knots**2
    + 2
    * ship_velocity_knots
    * current_velocity_knots
    * math.cos(angle_between_vectors_rad)
)

# Calculate resultant direction using the law of sines
# sin(α) / V₂ = sin(θ) / R
direction_offset_rad = math.asin(
    (current_velocity_knots * math.sin(angle_between_vectors_rad))
    / resultant_velocity_knots
)
direction_offset_deg = math.degrees(direction_offset_rad)

# =============================================================================
# DIRECTION CONVERSION (Degrees, Minutes, Seconds)
# =============================================================================

# Extract whole degrees
degrees_component = int(direction_offset_deg)

# Calculate minutes (fractional degrees × 60)
minutes_component_float = (direction_offset_deg - degrees_component) * 60
minutes_component = int(minutes_component_float)

# Calculate seconds (fractional minutes × 60)
seconds_component = (minutes_component_float - minutes_component) * 60

# =============================================================================
# OUTPUT RESULTS
# =============================================================================

print(f"Resultant speed: {resultant_velocity_knots:.4f} knots")
print(f"Direction: {direction_offset_deg:.4f}° north of east")
print(
    f"Direction (DMS): {degrees_component}° {minutes_component}' "
    f'{seconds_component:.0f}" north of east'
)
