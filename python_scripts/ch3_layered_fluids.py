"""
Layered Fluid Pressure Calculator

Calculates the hydrostatic pressure at the bottom of a tank containing
two immiscible fluid layers (oil on top of seawater). Computes both
gauge pressure and absolute pressure.
"""

# ===============================
# INPUT PARAMETERS
# ===============================

oil_density_g_per_cm3 = 0.85  # Density of oil in g/cm³
oil_layer_height_m = 10.0  # Height of oil layer in meters
seawater_density_t_per_m3 = 1.02  # Density of seawater in t/m³
seawater_layer_height_m = 4.0  # Height of seawater layer in meters
atmospheric_pressure_kpa = 101.3  # Atmospheric pressure in kPa
gravitational_acceleration_m_per_s2 = 9.81  # Acceleration due to gravity

# ===============================
# UNIT CONVERSIONS
# ===============================

# Convert oil density from g/cm³ to kg/m³
oil_density_kg_per_m3 = oil_density_g_per_cm3 * 1000

# Convert seawater density from t/m³ to kg/m³
seawater_density_kg_per_m3 = seawater_density_t_per_m3 * 1000

# =================================
# HYDROSTATIC PRESSURE CALCULATIONS
# =================================

# Pressure contribution from oil layer using P = ρ · g · h
pressure_from_oil_kpa = (
    oil_density_kg_per_m3 * gravitational_acceleration_m_per_s2 * oil_layer_height_m
) / 1000  # Convert Pa to kPa

# Pressure contribution from seawater layer using P = ρ · g · h
pressure_from_seawater_kpa = (
    seawater_density_kg_per_m3
    * gravitational_acceleration_m_per_s2
    * seawater_layer_height_m
) / 1000  # Convert Pa to kPa

# Total gauge pressure (pressure above atmospheric)
total_gauge_pressure_kpa = pressure_from_oil_kpa + pressure_from_seawater_kpa

# Absolute pressure (gauge pressure plus atmospheric pressure)
absolute_pressure_kpa = atmospheric_pressure_kpa + total_gauge_pressure_kpa

# ===============================
# OUTPUT RESULTS
# ===============================

print(f"Pressure due to oil layer       : {pressure_from_oil_kpa:.4f} kPa")
print(f"Pressure due to seawater layer  : " f"{pressure_from_seawater_kpa:.4f} kPa")
print(f"Total gauge pressure            : {total_gauge_pressure_kpa:.4f} kPa")
print(f"Absolute pressure at the bottom : {absolute_pressure_kpa:.4f} kPa")
