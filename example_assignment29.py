# -----------------------------
# Given data
# -----------------------------
oil_density_g_per_cm3 = 0.85  # Density of oil in g/cm³
oil_height_m = 10.0  # Height of oil layer in meters
seawater_density_t_per_m3 = 1.02  # Density of seawater in t/m³
seawater_height_m = 4.0  # Height of seawater layer in meters
atmospheric_pressure_kPa = 101.3  # Atmospheric pressure in kPa
g = 9.81  # Acceleration due to gravity (m/s²)

# -----------------------------
# Convert densities to kg/m³
# -----------------------------
oil_density = oil_density_g_per_cm3 * 1000  # g/cm³ → kg/m³
seawater_density = seawater_density_t_per_m3 * 1000  # t/m³ → kg/m³

# -----------------------------
# Hydrostatic pressure calculations
# -----------------------------
pressure_oil_kPa = (oil_density * g * oil_height_m) / 1000
pressure_seawater_kPa = (seawater_density * g * seawater_height_m) / 1000

# Total gauge and absolute pressure
gauge_pressure_kPa = pressure_oil_kPa + pressure_seawater_kPa
absolute_pressure_kPa = atmospheric_pressure_kPa + gauge_pressure_kPa

# -----------------------------
# Output results
# -----------------------------
print(f"Pressure due to oil layer       : {pressure_oil_kPa:.4f} kPa")
print(f"Pressure due to seawater layer  : {pressure_seawater_kPa:.4f} kPa")
print(f"Total gauge pressure            : {gauge_pressure_kPa:.4f} kPa")
print(f"Absolute pressure at the bottom : {absolute_pressure_kPa:.4f} kPa")
