import math

# -----------------------------
# Given data
# -----------------------------
D1 = 0.3  # Inlet diameter in meters
D2 = 0.1  # Throat diameter in meters
Cd = 0.95  # Coefficient of discharge
h_mercury = 0.250  # Manometer reading in meters of mercury
SG = 13.6  # Specific gravity of mercury relative to water
g = 9.81  # Acceleration due to gravity in m/s²

# -----------------------------
# Cross-sectional areas
# -----------------------------
A1 = math.pi * (D1**2) / 4  # Area at the inlet
A2 = math.pi * (D2**2) / 4  # Area at the throat

# -----------------------------
# Equivalent water head
# -----------------------------
# The difference in water levels (equivalent head) generates
# a hydrostatic pressure in the connecting legs that counteracts
# the mercury column. Multiplying by (SG - 1) accounts for the
# specific gravity of mercury relative to water.
h_eq = h_mercury * (SG - 1)

# -----------------------------
# Diameter ratio
# -----------------------------
beta = D2 / D1

# -----------------------------
# Discharge calculations
# -----------------------------
# Theoretical discharge based on the ideal flow equation
Q_theoretical = A2 * math.sqrt((2 * g * h_eq) / (1 - beta**4))

# Actual discharge accounting for the coefficient of discharge
Q_actual = Cd * Q_theoretical

# -----------------------------
# Output results
# -----------------------------
print(f"Cross-sectional area at inlet (A1): {A1:.4f} m²")
print(f"Cross-sectional area at throat (A2): {A2:.4f} m²")
print(f"Equivalent water head (h_eq): {h_eq:.4f} m")
print(f"Theoretical discharge: {Q_theoretical:.4f} m³/s")
print(f"Actual discharge: {Q_actual:.4f} m³/s")
