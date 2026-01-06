"""
Angular Momentum Conservation Calculator

Calculates the final angular velocity when two rotating bodies are coupled
together. Uses conservation of angular momentum to determine the combined
system's rotation speed.
"""

import math

# =================================
# INPUT PARAMETERS
# =================================

# Body 1 (initially rotating)
mass_body1_kg = 500  # Mass of body 1 in kilograms
radius_of_gyration_body1_m = 1.2  # Radius of gyration in meters
initial_angular_velocity_body1_rpm = 300  # Initial speed in rpm

# Body 2 (initially stationary)
mass_body2_kg = 2000  # Mass of body 2 in kilograms
radius_of_gyration_body2_m = 0.6  # Radius of gyration in meters

# =================================
# MOMENT OF INERTIA CALCULATIONS
# =================================

# Calculate moment of inertia for body 1 using I = m × k²
# where k is the radius of gyration
moment_of_inertia_body1_kg_m2 = mass_body1_kg * radius_of_gyration_body1_m**2

# Calculate moment of inertia for body 2
moment_of_inertia_body2_kg_m2 = mass_body2_kg * radius_of_gyration_body2_m**2

# =================================
# UNIT CONVERSION
# =================================

# Convert initial angular velocity from rpm to rad/s
# ω (rad/s) = (rpm / 60) × 2π
initial_angular_velocity_body1_rad_per_s = (
    (initial_angular_velocity_body1_rpm / 60) * 2 * math.pi
)

# =================================
# ANGULAR MOMENTUM CONSERVATION
# =================================

# Apply conservation of angular momentum:
# L_initial = L_final
# I₁ω₁ = (I₁ + I₂)ω_f
# Solving for final angular velocity:
# ω_f = (I₁ω₁) / (I₁ + I₂)

final_angular_velocity_rad_per_s = (
    moment_of_inertia_body1_kg_m2 * initial_angular_velocity_body1_rad_per_s
) / (moment_of_inertia_body1_kg_m2 + moment_of_inertia_body2_kg_m2)

# =================================
# UNIT CONVERSION FOR OUTPUT
# =================================

# Convert final angular velocity from rad/s to rpm
# rpm = (ω / 2π) × 60
final_angular_velocity_rpm = (final_angular_velocity_rad_per_s / (2 * math.pi)) * 60

# =================================
# OUTPUT RESULTS
# =================================

print(f"Final angular velocity (rad/s): " f"{final_angular_velocity_rad_per_s:.4f}")
print(f"Final angular velocity (rpm): {final_angular_velocity_rpm:.4f}")
