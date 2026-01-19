# I-SECTION GIRDER Problem 7.9 on p.178

# Input Dimensions (mm)

tf_w = 120  # top flange width
tf_t = 20  # top flange thickness
h_web = 180  # height of web (between flanges)
tw = 15  # web thickness
bf_w = 160  # bottom flange width
bf_t = 30  # bottom thickness

total_h = 230  # total depth of the I-section girder

# Areas

A_top = tf_w * tf_t
A_web = h_web * tw
A_bot = bf_w * bf_t
total_A = A_top + A_web + A_bot

# y-coordinates from the bottom face

y_bot = bf_t / 2
y_web = bf_t + h_web / 2
y_top = bf_t + h_web + tf_t / 2

# Own moments of inertia of each part

Iown_top = tf_w * tf_t**3 / 12
Iown_web = tw * h_web**3 / 12
Iown_bot = bf_w * bf_t**3 / 12


# Table data
parts = [
    ("Top flange   ", A_top, y_top, Iown_top),
    ("Web          ", A_web, y_web, Iown_web),
    ("Bottom flange", A_bot, y_bot, Iown_bot),
]

# Print Table + Results

sum_Ay = 0
sum_Ay2 = 0
sum_Iown = 0

print("=" * 88)
print(
    "Part             Area(mm²)   y(mm)         A·y(mm³)        A·y²(mm⁴)         Iown(mm⁴)"
)
print("-" * 88)

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
# k        = (I_na / total_A)**0.5

print("-" * 85)
print(
    f"{'TOTAL':<14}  {total_A:7.0f}   {'':>8}   {sum_Ay:12.0f}   {sum_Ay2:16.0f}   {sum_Iown:12.0f}"
)
print("=" * 85)
print()
print("Final Results")
print("═" * 60)
# print(f"Beam total depth          : {total_h} mm")
print(f"Total area                : {total_A:5.0f} mm²")
print(f"Neutral axis from bottom  : {y_bar:6.2f} mm")
print(f"I about bottom face       : {I_bottom/1e6:5.1f} × 10⁶ mm⁴ (reference)")
print(
    f"I about neutral axis      : {I_na/1e6:4.1f} × 10⁶ mm⁴ (used for design)"
)
# print(f"Radius of gyration k     : {k:5.1f} mm")
print("═" * 60)
