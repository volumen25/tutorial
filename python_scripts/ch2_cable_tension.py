"""
Elevator Cable Tension Calculator

Calculates the tension in an elevator cable under different motion
conditions: constant velocity, upward acceleration, and upward
deceleration. Uses Newton's second law (F = ma).
"""

# ==============================================
# INPUT PARAMETERS
# ==============================================

elevator_mass_kg = 750  # Mass of elevator in kilograms
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# Accelerations for different motion conditions
acceleration_constant_velocity_m_per_s2 = 0  # No acceleration
acceleration_upward_m_per_s2 = 1.2  # Upward acceleration
acceleration_deceleration_m_per_s2 = -1.2  # Upward deceleration (negative)

# ==============================================
# TENSION CALCULATIONS USING NEWTON'S SECOND LAW
# ==============================================

# For an elevator, the cable tension is given by:
# T = m(g + a)
# where:
# - m is the mass
# - g is gravitational acceleration
# - a is the net acceleration (positive upward, negative downward)

# Case 1: Constant velocity (a = 0)
# Cable tension equals the weight of the elevator
tension_constant_velocity_n = elevator_mass_kg * (
    gravitational_acceleration_m_per_s2 + acceleration_constant_velocity_m_per_s2
)

# Case 2: Upward acceleration (a > 0)
# Cable tension is greater than weight due to upward acceleration
tension_upward_acceleration_n = elevator_mass_kg * (
    gravitational_acceleration_m_per_s2 + acceleration_upward_m_per_s2
)

# Case 3: Upward deceleration (a < 0)
# Cable tension is less than weight due to deceleration
tension_upward_deceleration_n = elevator_mass_kg * (
    gravitational_acceleration_m_per_s2 + acceleration_deceleration_m_per_s2
)

# ==============================================
# OUTPUT RESULTS
# ==============================================

print(f"Tension at constant velocity: {tension_constant_velocity_n:.4f} N")
print(f"Tension during upward acceleration: " f"{tension_upward_acceleration_n:.4f} N")
print(f"Tension during upward deceleration: " f"{tension_upward_deceleration_n:.4f} N")
