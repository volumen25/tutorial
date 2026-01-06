import math

# -----------------------------
# Given data
# -----------------------------
diameter_small = 0.025  # m (effort plunger)
diameter_large = 0.070  # m (load piston)
load = 5880.0  # N (equivalent to 5.88 kN)

# -----------------------------
# Calculate radii and cross-sectional areas
# -----------------------------
radius_small = diameter_small / 2
radius_large = diameter_large / 2

area_small = math.pi * (radius_small**2)  # m²
area_large = math.pi * (radius_large**2)  # m²

# -----------------------------
# System pressure and ideal force on small plunger
# -----------------------------
pressure = load / area_large  # Pa
force_small = pressure * area_small  # N

# -----------------------------
# Output results
# -----------------------------
print(f"System pressure: {pressure:.2f} Pa " f"(or {pressure / 1e6:.3f} MPa)")
print(f"Ideal force on small plunger: {force_small:.1f} N")
