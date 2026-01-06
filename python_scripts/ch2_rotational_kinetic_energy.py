"""
Rotational Kinetic Energy Calculator

Calculates the rotational kinetic energy of a rotating body at different
angular velocities and determines the energy released during deceleration.
"""

import math

# ===============================
# INPUT PARAMETERS
# ===============================

rotating_mass_kg = 750  # Mass of rotating body in kilograms
radius_of_gyration_m = 0.46  # Radius of gyration in meters
initial_angular_velocity_rpm = 120  # Initial rotational speed in rpm
final_angular_velocity_rpm = 100  # Final rotational speed in rpm

# ===============================
# MOMENT OF INERTIA CALCULATION
# ===============================

# Calculate moment of inertia using I = m × k²
# where k is the radius of gyration
moment_of_inertia_kg_m2 = rotating_mass_kg * radius_of_gyration_m**2

# ===============================
# UNIT CONVERSIONS
# ===============================

# Convert initial angular velocity from rpm to rad/s
# ω (rad/s) = (rpm / 60) × 2π
initial_angular_velocity_rad_per_s = initial_angular_velocity_rpm * 2 * math.pi / 60

# Convert final angular velocity from rpm to rad/s
final_angular_velocity_rad_per_s = final_angular_velocity_rpm * 2 * math.pi / 60

# ===============================
# KINETIC ENERGY CALCULATIONS
# ===============================

# Calculate initial rotational kinetic energy using KE = ½Iω²
initial_kinetic_energy_j = (
    0.5 * moment_of_inertia_kg_m2 * initial_angular_velocity_rad_per_s**2
)

# Calculate final rotational kinetic energy
final_kinetic_energy_j = (
    0.5 * moment_of_inertia_kg_m2 * final_angular_velocity_rad_per_s**2
)

# Calculate energy released (change in kinetic energy)
energy_released_j = initial_kinetic_energy_j - final_kinetic_energy_j

# Convert energies from Joules to kilojoules
initial_kinetic_energy_kj = initial_kinetic_energy_j / 1e3
final_kinetic_energy_kj = final_kinetic_energy_j / 1e3
energy_released_kj = energy_released_j / 1e3

# ===============================
# OUTPUT RESULTS
# ===============================

print(f"I:                    {moment_of_inertia_kg_m2:.4f} kg·m²")
print(f"KE at 120 rpm:        {initial_kinetic_energy_kj:.4f} kJ")
print(f"KE at 100 rpm:        {final_kinetic_energy_kj:.4f} kJ")
print(f"Energy given out:     {energy_released_kj:.4f} kJ")
