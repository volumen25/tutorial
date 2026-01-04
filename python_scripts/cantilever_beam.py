import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Cantilever Beam Deflection under End Load
# =============================================================================

# -----------------------------
# Beam properties
# -----------------------------
beam_length = 10.0  # Length (m)
young_modulus = 200e9  # Young's modulus (Pa)
second_moment_area = 8.33e-6  # Second moment of area (m^4)
point_load = 1000  # Point load at free end (N)

# -----------------------------
# Position along the beam
# -----------------------------
x_positions = np.linspace(0, beam_length, 100)

# -----------------------------
# Beam deflection equation
# v(x) = (P / (6EI)) * x^2 * (3L - x)
# -----------------------------
deflection = (
    point_load
    / (6 * young_modulus * second_moment_area)
    * x_positions**2
    * (3 * beam_length - x_positions)
)

# -----------------------------
# Plot deflection
# -----------------------------
plt.figure(figsize=(10, 6))
plt.plot(x_positions, deflection * 1000, "b-", linewidth=2)
plt.xlabel("Position along beam (m)")
plt.ylabel("Deflection (mm)")
plt.title("Cantilever Beam Deflection")
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.show()

# -----------------------------
# Maximum deflection at free end
# -----------------------------
max_deflection = deflection[-1]
print(f"Maximum deflection at free end: {max_deflection*1000:.2f} mm")
