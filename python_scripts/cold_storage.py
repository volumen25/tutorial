"""
Heat Transfer Calculation for Cold Storage Room

Calculate heat transfer per hour through walls, ceiling, and floor
due to conduction in a frozen fish storage room.
"""

# Room dimensions
length = 30  # m
width = 23  # m
height = 3  # m

# Insulation properties
cork_thickness_walls = 0.25  # m (25 cm)
cork_k_walls = 0.049  # W/mK
corkboard_thickness_floor = 0.15  # m (15 cm)
corkboard_k_floor = 0.043  # W/mK

# Temperatures
T_inside = -30  # °C
T_ambient = 21  # °C
T_ground = 10  # °C

# Calculate surface areas
area_floor = length * width
area_ceiling = length * width
area_wall_long = 2 * (length * height)  # Two long walls
area_wall_short = 2 * (width * height)  # Two short walls
area_walls_total = area_wall_long + area_wall_short

# Heat transfer equation: Q = k × A × ΔT / s
# where:
#   Q = heat transfer rate (W)
#   k = thermal conductivity (W/mK)
#   A = area (m²)
#   ΔT = temperature difference (K or °C)
#   s = thickness (m)

# 1. Heat transfer through walls (exposed to ambient air)
delta_T_walls = T_ambient - T_inside
Q_walls = (
    cork_k_walls * area_walls_total * delta_T_walls
) / cork_thickness_walls

# 2. Heat transfer through ceiling (exposed to ambient air)
delta_T_ceiling = T_ambient - T_inside
Q_ceiling = (
    cork_k_walls * area_ceiling * delta_T_ceiling
) / cork_thickness_walls

# 3. Heat transfer through floor (exposed to ground)
delta_T_floor = T_ground - T_inside
Q_floor = (
    corkboard_k_floor * area_floor * delta_T_floor
) / corkboard_thickness_floor

# Total heat transfer
Q_total_watts = Q_walls + Q_ceiling + Q_floor
Q_total_kW = Q_total_watts / 1000
Q_total_per_hour_kWh = Q_total_kW  # kW × 1 hour = kWh
Q_total_per_hour_MJ = Q_total_kW * 3.6  # kW × 3600 s = kJ/s × 3600 = MJ

# Display Results
print("\n" + "=" * 30)
print("HEAT TRANSFER PER HOUR")
print("=" * 30)
print(f"Q per hour: {Q_total_watts * 3600 / 1000:.2f} kJ")

pct_walls = (Q_walls / Q_total_watts) * 100
pct_ceiling = (Q_ceiling / Q_total_watts) * 100
pct_floor = (Q_floor / Q_total_watts) * 100

print(f"Walls:   {pct_walls:>6.2f}%")
print(f"Ceiling: {pct_ceiling:>6.2f}%")
print(f"Floor:   {pct_floor:>6.2f}%")
print("=" * 30)
