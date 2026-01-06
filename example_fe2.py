# -----------------------------
# Given data
# -----------------------------
width = 2.0  # m (width of bulkhead)
h_oil = 4.0  # m (oil depth)
h_water = 6.0  # m (water depth)
rho_oil = 850.0  # kg/m³
rho_water = 1000.0  # kg/m³
g = 9.81  # m/s²

# -----------------------------
# Display input parameters
# -----------------------------
print("Bulkhead Separating Oil and Water")
print(f"Bulkhead width          : {width} m")
print(f"Oil side    : {h_oil} m deep,   ρ = {rho_oil} kg/m³")
print(f"Water side  : {h_water} m deep,   ρ = {rho_water} kg/m³")
print()

# -----------------------------
# Hydrostatic force on oil side
# -----------------------------
A_oil = width * h_oil
h_c_oil = h_oil / 2
F_oil = rho_oil * g * h_c_oil * A_oil

# -----------------------------
# Hydrostatic force on water side
# -----------------------------
A_water = width * h_water
h_c_water = h_water / 2
F_water = rho_water * g * h_c_water * A_water

# -----------------------------
# Net horizontal thrust
# -----------------------------
F_net_N = F_water - F_oil  # positive towards oil side
F_net_kN = F_net_N / 1000

# -----------------------------
# Output results
# -----------------------------
print(f"Force from oil side     : {F_oil:8.0f} N  = {F_oil/1000:6.1f} kN")
print(f"Force from water side   : {F_water:8.0f} N  = {F_water/1000:6.1f} kN")
print()
print(f"NET THRUST              : {F_net_N:8.0f} N  = {F_net_kN:6.1f} kN")
print("Direction               : Towards the oil side")
