# -----------------------------
# Given data
# -----------------------------
width = 12.0  # width of gate (m)
h1 = 9.0  # deeper side water depth (m)
h2 = 4.5  # shallower side water depth (m)
rho = 1025.0  # density of seawater (kg/m³)
g = 9.81  # acceleration due to gravity (m/s²)

# -----------------------------
# Hydrostatic force on deeper side
# -----------------------------
A1 = h1 * width  # area of gate submerged
h_c1 = h1 / 2  # depth of centroid
F1 = rho * g * h_c1 * A1  # hydrostatic force

# -----------------------------
# Hydrostatic force on shallower side
# -----------------------------
A2 = h2 * width  # area of gate submerged
h_c2 = h2 / 2  # depth of centroid
F2 = rho * g * h_c2 * A2  # hydrostatic force

# -----------------------------
# Net horizontal thrust
# -----------------------------
F_net = F1 - F2

# -----------------------------
# Output results
# -----------------------------
print("=== Dock Gate Hydrostatic Thrust Calculation ===")
print(f"Force from {h1} m side : {F1:,.0f} N  ({F1/1e6:.3f} MN)")
print(f"Force from {h2} m side : {F2:,.0f} N  ({F2/1e6:.3f} MN)")
print(
    f"Resultant horizontal thrust: {F_net:,.0f} N  "
    f"({F_net/1000:.1f} kN or {F_net/1e6:.3f} MN)"
)
