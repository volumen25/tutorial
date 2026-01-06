# -----------------------------
# Given data
# -----------------------------
tank_length = 10.0  # m
tank_width = 4.0  # m
tank_height = 6.0  # m
sounding_pipe = 5.0  # m (oil rises 5 m above the tank top in vent/pipe)

specific_gravity = 0.9
rho_oil = specific_gravity * 1000  # kg/m³
g = 9.81  # m/s²

# -----------------------------
# Calculated values
# -----------------------------
total_head = tank_height + sounding_pipe  # from bottom to oil surface

# End plate dimensions and force
end_height = tank_height  # m
end_width = tank_width  # m
area_end = end_height * end_width  # m²

# Depth of centroid of end plate below oil surface
h_centroid_end = sounding_pipe + (tank_height / 2)  # m

# Hydrostatic force on end plate
force_end_plate = rho_oil * g * h_centroid_end * area_end

# Bottom plate force
area_bottom = tank_length * tank_width  # m²
force_bottom = rho_oil * g * total_head * area_bottom

# -----------------------------
# Output results
# -----------------------------
print("=== Hydrostatic Loads on Oil Tank ===")
print(
    f"Tank dimensions       : {tank_length} m × {tank_width} m × "
    f"{tank_height} m (L×W×H)"
)
print(f"Oil rise in sounding pipe : {sounding_pipe} m")
print(f"Oil density           : {rho_oil} kg/m³")
print()
print(
    f"End plate (one wall)  : {end_height} m high × {end_width} m "
    f"wide = {area_end} m²"
)
print(
    f"Horizontal load on one end plate : {force_end_plate:,.0f} N = "
    f"{force_end_plate/1000:.0f} kN"
)
print()
print(
    f"Bottom plate          : {tank_length} m × {tank_width} m = "
    f"{area_bottom} m²"
)
print(
    f"Vertical load on bottom          : {force_bottom:,.0f} N = "
    f"{force_bottom/1000:.0f} kN"
)
