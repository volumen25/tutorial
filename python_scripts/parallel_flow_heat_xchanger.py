#!/usr/bin/env python3
"""
Heat Exchanger

Parallel flow heat exchanger with exhaust gas and cooling water
"""

import math

# Given data
m_dot_gas = 0.55  # kg/s
m_dot_water = 0.65  # kg/s
T_gas_in = 420  # °C
T_gas_out = 130  # °C
T_water_in = 15  # °C
cp_gas = 1130  # J/kgK
cp_water = 4190  # J/kgK
U = 150  # W/m²K

# Heat transfer rate
Q = m_dot_gas * cp_gas * (T_gas_in - T_gas_out)

# Water outlet temperature
T_water_out = (Q / (m_dot_water * cp_water)) + T_water_in

# Temperature differences
Delta_T1 = T_gas_in - T_water_in
Delta_T2 = T_gas_out - T_water_out

# LMTD
LMTD = (Delta_T1 - Delta_T2) / math.log(Delta_T1 / Delta_T2)

# Surface area
A = Q / (U * LMTD)

# Results
print(f"Heat Transfer Rate: {Q:,.2f} W")
print(f"Water Outlet Temp: {T_water_out:.2f}°C")
print(f"LMTD: {LMTD:.2f}°C")
print(f"Surface Area: {A:.4f} m²")
