# -----------------------------
# Given parameters
# -----------------------------
area_small_mm2 = 25.0  # mm² (small piston)
area_large_mm2 = 100.0  # mm² (large piston)
force_small = 150.0  # N (force applied to small piston)

# -----------------------------
# Convert areas to SI units (m²)
# -----------------------------
area_small = area_small_mm2 * 1e-6  # 1 mm² = 10^-6 m²
area_large = area_large_mm2 * 1e-6

# -----------------------------
# System pressure and load on large piston
# -----------------------------
pressure = force_small / area_small  # Pa
load_large = pressure * area_large  # N

# -----------------------------
# Output results
# -----------------------------
print(f"System pressure: {pressure:.2f} Pa " f"(or {pressure / 1e6:.1f} MPa)")
print(f"Load carried by larger piston: {load_large:.1f} N")
