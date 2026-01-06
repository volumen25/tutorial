"""
Ship Mooring Drum Torque Calculator

Calculates the torque required at a mooring drum to accelerate a ship
from initial to final velocity. Accounts for friction forces, ship
acceleration, and drum rotational inertia.
"""

# ===============================
# INPUT PARAMETERS
# ===============================

ship_mass_tonnes = 1000  # Mass of ship in tonnes
drum_mass_tonnes = 4.5  # Mass of drum in tonnes
drum_diameter_m = 3.1  # Diameter of drum in meters
drum_radius_of_gyration_m = 1.0  # Radius of gyration in meters
friction_coefficient = 0.6  # Coefficient of friction (dimensionless)
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity
ship_initial_velocity_m_per_s = 0.1  # Initial velocity in m/s
ship_final_velocity_m_per_s = 0.3  # Final velocity in m/s
acceleration_time_s = 30  # Time duration in seconds

# ===============================
# UNIT CONVERSIONS
# ===============================

# Convert masses from tonnes to kilograms
ship_mass_kg = ship_mass_tonnes * 1000
drum_mass_kg = drum_mass_tonnes * 1000

# Calculate effective radius of drum (rope wraps at outer surface)
drum_effective_radius_m = drum_diameter_m / 2

# ===============================
# ACCELERATION CALCULATIONS
# ===============================

# Calculate linear acceleration of the ship using a = Δv / Δt
ship_linear_acceleration_m_per_s2 = (
    ship_final_velocity_m_per_s - ship_initial_velocity_m_per_s
) / acceleration_time_s

# Calculate angular acceleration of the drum using α = a / r
drum_angular_acceleration_rad_per_s2 = (
    ship_linear_acceleration_m_per_s2 / drum_effective_radius_m
)

# ===============================
# MOMENT OF INERTIA CALCULATION
# ===============================

# Calculate drum moment of inertia using I = m × k²
drum_moment_of_inertia_kg_m2 = drum_mass_kg * drum_radius_of_gyration_m**2

# ===============================
# FORCE CALCULATIONS
# ===============================

# Calculate friction force between ship and water: F_f = μ × m × g
friction_force_n = (
    friction_coefficient * ship_mass_kg * gravitational_acceleration_m_per_s2
)

# Calculate force required to accelerate the ship: F = m × a
ship_acceleration_force_n = ship_mass_kg * ship_linear_acceleration_m_per_s2

# ===============================
# TORQUE CALCULATIONS
# ===============================

# Torque required to overcome friction: T_f = F_f × r
torque_friction_n_m = friction_force_n * drum_effective_radius_m

# Torque required to accelerate the ship linearly: T_s = F_s × r
torque_ship_acceleration_n_m = ship_acceleration_force_n * drum_effective_radius_m

# Torque required to accelerate the drum rotationally: T_d = I × α
torque_drum_acceleration_n_m = (
    drum_moment_of_inertia_kg_m2 * drum_angular_acceleration_rad_per_s2
)

# Total torque required at the drum
total_torque_n_m = (
    torque_friction_n_m + torque_ship_acceleration_n_m + torque_drum_acceleration_n_m
)

# Convert total torque to meganewton-meters for output
total_torque_mn_m = total_torque_n_m / 1e6

# ===============================
# OUTPUT RESULTS
# ===============================

print(
    f"Angular acceleration of drum (rad/s²): "
    f"{drum_angular_acceleration_rad_per_s2:.4f}"
)
print(f"Torque required at the drum (MN·m): {total_torque_mn_m:.4f}")
