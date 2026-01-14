"""
Heat Transfer Through Brick Wall

Q/A = k * (T1 - T2) / s

Where:
- Q/A = heat transfer rate per unit area (W/m²)
- k = thermal conductivity (W/mK)
- T1 = inner surface temperature (°C)
- T2 = outer surface temperature (°C)
- s = wall thickness (m)
"""

# Given data
T_inner = 40  # Inner surface temperature in °C
T_outer = 20  # Outer surface temperature in °C
thickness_mm = 250  # Wall thickness in mm
k = 0.52  # Thermal conductivity in W/mK

# Convert thickness to meters
thickness_m = thickness_mm / 1000

# Calculate temperature difference
delta_T = T_inner - T_outer

# Apply Fourier's Law: Q/A = k * ΔT / L
heat_transfer_rate = k * delta_T / thickness_m

# Display results
print("=" * 60)
print("HEAT TRANSFER THROUGH BRICK WALL")
print("=" * 60)
print("\nGiven Data:")
print(f"  Inner surface temperature: {T_inner} C")
print(f"  Outer surface temperature: {T_outer} C")
print(f"  Wall thickness (L): {thickness_mm} mm = {thickness_m} m")
print(f"  Thermal conductivity (k): {k} W/mK")

print("\nCalculation:")
print(f"  Temperature difference: {delta_T} C")
print("  Heat Transfer per m2: Q/A = k × ΔT / L")
print(f"  Q/A = {k} × {delta_T} / {thickness_m}")
print(f"  Q/A = {k * delta_T} / {thickness_m}")

print("\n" + "=" * 60)
print(f"RESULT: Heat transfer rate = {heat_transfer_rate:.2f} W/m2")
print("=" * 60)
