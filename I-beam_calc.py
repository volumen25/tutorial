# I-BEAM SECTION PROPERTIES

# INPUT DIMENSIONS (mm)

bf = 300  # flange width (top and bottom the same)
tf = 20  # flange thickness (top and bottom the same)
h_web = 560  # clear height of web (between flanges)
tw = 12  # web thickness

total_h = h_web + 2 * tf  # total depth of the I-beam

# CALCULATIONS
# Areas

A_top = bf * tf
A_bot = bf * tf
A_web = tw * h_web
total_A = A_top + A_bot + A_web

# y-coordinates from the very bottom face

y_bot = tf / 2
y_web = tf + h_web / 2
y_top = tf + h_web + tf / 2

# Own moments of inertia of each part

Iown_top = bf * tf**3 / 12
Iown_bot = bf * tf**3 / 12
Iown_web = tw * h_web**3 / 12

# Table data
parts = [
    ("Bottom flange", A_bot, y_bot, Iown_bot),
    ("Web          ", A_web, y_web, Iown_web),
    ("Top flange   ", A_top, y_top, Iown_top),
]

# PRINT TABLE + FINAL RESULTS

sum_Ay = 0
sum_Ay2 = 0
sum_Iown = 0

print("=" * 85)
print(
    "Part             Area (mm²)     y (mm)       A·y               A·y²        Iown"
)
print("-" * 85)

for name, A, y, Iown in parts:
    Ay = A * y
    Ay2 = A * y * y
    sum_Ay += Ay
    sum_Ay2 += Ay2
    sum_Iown += Iown

    print(
        f"{name}  {A:8.0f}   {y:8.1f}   {Ay:12.0f}   {Ay2:16.0f}   {Iown:12.0f}"
    )

y_bar = sum_Ay / total_A
I_bottom = sum_Iown + sum_Ay2
I_na = I_bottom - total_A * y_bar**2
k = (I_na / total_A) ** 0.5

print("-" * 85)
print(
    f"{'TOTAL':<14}  {total_A:8.0f}   {'':>8}   {sum_Ay:10.0f}   {sum_Ay2:18.0f}   {sum_Iown:10.0f}"
)
print("=" * 85)
print()
print("FINAL RESULTS")
print("═" * 60)
print(f"Beam total depth          : {total_h} mm")
print(f"Total area                : {total_A:5.0f} mm²")
print(f"Neutral axis from bottom  : {y_bar:6.2f} mm")
print(
    f"I about bottom face       : {I_bottom/1e6:5.1f} × 10⁶ mm⁴ (reference only)"
)
print(
    f"I about neutral axis      : {I_na/1e6:4.1f} × 10⁶ mm⁴ (used for design)"
)
print(f"Radius of gyration k      : {k:5.1f} mm")
print("═" * 60)
