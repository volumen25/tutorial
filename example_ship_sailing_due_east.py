import math

"""
Calculation of Resultant Velocity of a Ship Affected by Current

This script computes the resultant speed and direction of a ship traveling due east
at 18 knots in the presence of a 3-knot current acting at a 50° angle relative to the
ship's heading. The solution employs the law of cosines to find the magnitude of the
resultant vector and the law of sines to determine the deviation angle from the ship's
course.

Assumptions:
- Ship velocity: 18 knots due east
- Current velocity: 3 knots at 50° from the ship's heading
- Positive angle measured toward north (standard navigation convention)
"""

# =============================================================================
# Input Parameters
# =============================================================================

ship_speed_knots = 18.0  # Ship's speed through the water (knots)
current_speed_knots = 3.0  # Current speed (knots)
angle_degrees = 50.0  # Angle between ship heading and current (degrees)

# =============================================================================
# Vector Calculations
# =============================================================================

# Convert angle to radians for trigonometric functions
angle_radians = math.radians(angle_degrees)

# Magnitude of resultant velocity using the law of cosines:
# R² = ship² + current² + 2 * ship * current * cos(angle)
resultant_speed_knots = math.sqrt(
    ship_speed_knots**2
    + current_speed_knots**2
    + 2 * ship_speed_knots * current_speed_knots * math.cos(angle_radians)
)

# Deviation angle (theta) using the law of sines:
# sin(theta) / current = sin(angle) / R
# theta = arcsin((current * sin(angle)) / R)
theta_radians = math.asin(
    (current_speed_knots * math.sin(angle_radians)) / resultant_speed_knots
)
theta_degrees = math.degrees(theta_radians)

# =============================================================================
# Direction Conversion to Degrees, Minutes, Seconds (DMS)
# =============================================================================

# Integer degrees
degrees = int(theta_degrees)

# Fractional part converted to minutes
minutes_float = (theta_degrees - degrees) * 60
minutes = int(minutes_float)

# Remaining fractional minutes converted to seconds
seconds = (minutes_float - minutes) * 60

# =============================================================================
# Output Results
# =============================================================================

print(f"Resultant speed: {resultant_speed_knots:.4f} knots")
print(f"Direction: {theta_degrees:.4f}° north of east")
print(f"Direction (DMS): {degrees}° {minutes}' {seconds:.0f}\" north of east")
