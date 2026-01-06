"""
Rotational Deceleration Calculator

Calculates the time and number of revolutions required to bring a
rotating body to rest under a constant braking torque. Uses rotational
kinematics and dynamics equations.
"""

import math

# =================================
# INPUT PARAMETERS
# =================================

braking_torque_n_m = 317.0  # Braking torque in Newton-meters
rotating_mass_kg = 1.59 * 1000  # Mass of rotating body in kilograms
radius_of_gyration_m = 0.686  # Radius of gyration in meters
initial_angular_velocity_rpm = 1920.0  # Initial rotational speed in rpm

# =================================
# MOMENT OF INERTIA CALCULATION
# =================================

# Calculate moment of inertia using I = m × k²
# where k is the radius of gyration
moment_of_inertia_kg_m2 = rotating_mass_kg * radius_of_gyration_m**2

# =================================
# UNIT CONVERSION
# =================================

# Convert initial angular velocity from rpm to rad/s
# ω (rad/s) = (rpm / 60) × 2π
initial_angular_velocity_rad_per_s = (
    (initial_angular_velocity_rpm / 60.0) * 2.0 * math.pi
)

# =================================
# ANGULAR DECELERATION CALCULATION
# =================================

# Calculate angular deceleration using τ = I × α
# Solving for α: α = τ / I
# (negative because it's deceleration, but using magnitude here)
angular_deceleration_rad_per_s2 = braking_torque_n_m / moment_of_inertia_kg_m2

# =================================
# TIME TO STOP CALCULATION
# =================================

# Calculate time to stop using ω_f = ω_0 - αt
# With ω_f = 0 (comes to rest): t = ω_0 / α
time_to_stop_s = initial_angular_velocity_rad_per_s / angular_deceleration_rad_per_s2

# Convert time to minutes
time_to_stop_min = time_to_stop_s / 60.0

# =================================
# ANGULAR DISPLACEMENT CALCULATION
# =================================

# Calculate total angular displacement using θ = ω_0t - ½αt²
# Or equivalently: θ = ½ω_0t (when final velocity is zero)
angular_displacement_rad = 0.5 * initial_angular_velocity_rad_per_s * time_to_stop_s

# Convert angular displacement from radians to revolutions
number_of_revolutions = angular_displacement_rad / (2.0 * math.pi)

# =================================
# OUTPUT RESULTS
# =================================

print(f"I (kg·m²):           {moment_of_inertia_kg_m2:.4f}")
print(f"omega0 (rad/s):       {initial_angular_velocity_rad_per_s:.4f}")
print(f"alpha (rad/s²):      {angular_deceleration_rad_per_s2:.6f}")
print(f"time to stop (s):     {time_to_stop_s:.4f}")
print(f"time to stop (min):   {time_to_stop_min:.4f}")
print(f"revolutions:          {number_of_revolutions:.4f}")
