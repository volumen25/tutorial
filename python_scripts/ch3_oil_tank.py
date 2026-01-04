"""
Oil Tank Hydrostatic Load Calculator

Calculates hydrostatic forces on the end plates and bottom plate of a
rectangular oil tank with a sounding pipe. The oil rises above the tank
top in the sounding pipe, increasing the pressure on all surfaces.
"""

# ==================================
# INPUT PARAMETERS
# ==================================

tank_length_m = 10.0  # Length of tank in meters
tank_width_m = 4.0  # Width of tank in meters
tank_height_m = 6.0  # Height of tank in meters
sounding_pipe_height_m = 5.0  # Oil rise above tank top in meters
oil_specific_gravity = 0.9  # Specific gravity of oil (unitless)
oil_density_kg_per_m3 = oil_specific_gravity * 1000  # Density in kg/m³
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ==================================
# CALCULATED VALUES
# ==================================

# Total head from tank bottom to oil surface in sounding pipe
total_head_m = tank_height_m + sounding_pipe_height_m

# End plate dimensions (vertical wall at short end of tank)
end_plate_height_m = tank_height_m
end_plate_width_m = tank_width_m
end_plate_area_m2 = end_plate_height_m * end_plate_width_m

# Depth of centroid of end plate below oil surface
# (centroid is at mid-height of plate, plus sounding pipe height)
end_plate_centroid_depth_m = sounding_pipe_height_m + (tank_height_m / 2)

# Hydrostatic force on one end plate using F = ρ · g · h_c · A
force_end_plate_n = (
    oil_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * end_plate_centroid_depth_m
    * end_plate_area_m2
)

# Bottom plate dimensions and force
bottom_plate_area_m2 = tank_length_m * tank_width_m

# Hydrostatic force on bottom plate using F = ρ · g · h · A
# (pressure at bottom is based on total head)
force_bottom_plate_n = (
    oil_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * total_head_m
    * bottom_plate_area_m2
)

# Convert forces from Newtons to kilonewtons
force_end_plate_kn = force_end_plate_n / 1000
force_bottom_plate_kn = force_bottom_plate_n / 1000

# ==================================
# OUTPUT RESULTS
# ==================================

print("=== Hydrostatic Loads on Oil Tank ===")
print(
    f"Tank dimensions       : {tank_length_m} m × {tank_width_m} m × "
    f"{tank_height_m} m (L×W×H)"
)
print(f"Oil rise in sounding pipe : {sounding_pipe_height_m} m")
print(f"Oil density           : {oil_density_kg_per_m3} kg/m³")
print()
print(
    f"End plate (one wall)  : {end_plate_height_m} m high × "
    f"{end_plate_width_m} m wide = {end_plate_area_m2} m²"
)
print(
    f"Horizontal load on one end plate : {force_end_plate_n:,.0f} N = "
    f"{force_end_plate_kn:.0f} kN"
)
print()
print(
    f"Bottom plate          : {tank_length_m} m × {tank_width_m} m = "
    f"{bottom_plate_area_m2} m²"
)
print(
    f"Vertical load on bottom          : {force_bottom_plate_n:,.0f} N = "
    f"{force_bottom_plate_kn:.0f} kN"
)
