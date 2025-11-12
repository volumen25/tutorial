# Thermal Expansion {#thermal_expansion}

Thermal expansion is the tendency of materials to change their shape, area, and volume in response to a change in temperature. When most substances are heated, their particles move more vigorously and tend to occupy more space, leading to an increase in dimensions. Conversely, when substances are cooled, they generally contract. This phenomenon occurs in solids, liquids, and gases, although the degree and nature of expansion vary depending on the material’s state and properties.

## Linear Expansion

This occurs along a specific dimension or direction, primarily in long, narrow objects (like rods or beams). When the temperature of a solid object increases, its length expands by an amount proportional to its original length and the temperature change. The equation for linear expansion is:

$$
\Delta L = \alpha L_0 \Delta T
$$ {#eq-linearexp} where:

-   $\Delta L$ is the change in length,

-   $\alpha$ is the coefficient of linear expansion (unique to each material),

-   $L_0$ is the original length, and

-   $\Delta T$ is the temperature change.

## Superficial Expansion

Applicable to two-dimensional surfaces, such as sheets or plates. Here, both length and width expand, leading to an increase in surface area. The formula for area expansion is: $$
\Delta A = 2 \alpha A_0 \Delta T
$$ {#eq-superficial-exp} where:

-   $\Delta A$ is the change in area,
-   $A_0$ is the initial area, and
-   $\Delta T$ is the temperature change.

## Volumetric Expansion

Relevant for three-dimensional objects (like solids, liquids, and gases). The volume of an object expands with temperature, especially in fluids where this effect is more pronounced. The formula is: $$
\Delta V = \beta V_0 \Delta T
$$ {#eq-volumetric-exp}

where:

-   $\Delta V$ is the change in volume,
-   $\beta$ is the coefficient of volumetric expansion, which is approximately three times the linear expansion coefficient for isotropic solids,
-   $V_0$ is the initial volume, and
-   $\Delta T$ is the temperature change.

## Thermal Expansion of a Steel Pipeline

A steel section of pipeline is $75\ \mathrm{m}$ long when out of service at an ambient temperature of $20^\circ\mathrm{C}$. In service, it transports steam at $203^\circ\mathrm{C}$. Assuming the pipe is free to expand, find its length at the operating temperature.\
(The coefficient of linear expansion for steel is $\alpha = 12\times10^{-6}\ /\!^\circ\mathrm{C}$.)

Given:

$$
\begin{aligned}
L_0 &= 75\ \mathrm{m}, \\
T_1 &= 20^\circ\mathrm{C}, \\
T_2 &= 203^\circ\mathrm{C}, \\
\alpha &= 12\times10^{-6}\ /\!^\circ\mathrm{C}.
\end{aligned}
$$

The temperature rise is:

$$
\Delta T = T_2 - T_1 = 203 - 20 = 183^\circ\mathrm{C}.
$$

For linear expansion:

$$
L = L_0 (1 + \alpha \Delta T).
$$

Substitute the values:

$$
\begin{aligned}
L &= 75 \left(1 + 12\times10^{-6} \times 183\right) \\
  &= 75 \left(1 + 0.002196\right) \\
  &= 75.1647\ \mathrm{m}.
\end{aligned}
$$

**Final Answer**

$$
\boxed{L = 75.165\ \mathrm{m}}
$$

**Note:** The pipe expands by:

$$
\Delta L = L - L_0 = 0.165\ \mathrm{m} = 165\ \mathrm{mm}.
$$

### Code

``` python
# Linear Expansion of a Steel Pipeline
# ------------------------------------
# Given:
#   L0 = 75 m   (initial length)
#   T1 = 20 °C  (ambient temperature)
#   T2 = 203 °C (operating temperature)
#   α  = 12 × 10⁻⁶ /°C (coefficient of linear expansion for steel)
#
# Find:
#   Final length L at 203 °C.

# Given values
L0 = 75.0                 # m
T1 = 20.0                 # °C
T2 = 203.0                # °C
alpha = 12e-6             # /°C

# Temperature change
delta_T = T2 - T1

# Final length using linear expansion formula
L = L0 * (1 + alpha * delta_T)

# Expansion amount
expansion = L - L0

# Display results
print(f"Initial Length (m): {L0:.2f}")
print(f"Final Length (m):   {L:.3f}")
print(f"Expansion (m):      {expansion:.3f}")
```

## Thermal Expansion of a Brass Cube

If a solid brass cube measures **50 mm × 50 mm × 50 mm** at **10°C**, what volume will it occupy when heated to **78°C**?

Coefficient of linear expansion for brass, $\alpha = 18.4 \times 10^{-6}\,/^\circ \mathrm{C}$.

**Step 1: Given Data**

$$
\begin{aligned}
L_0 &= 50\ \mathrm{mm} = 0.05\ \mathrm{m}, \\
T_1 &= 10^\circ \mathrm{C}, \\
T_2 &= 78^\circ \mathrm{C}, \\
\Delta T &= T_2 - T_1 = 68^\circ \mathrm{C}, \\
\alpha &= 18.4 \times 10^{-6}\,/^\circ \mathrm{C}.
\end{aligned}
$$

**Step 2: Coefficient of Volumetric Expansion**

$$
\beta = 3\alpha = 3(18.4 \times 10^{-6}) = 55.2 \times 10^{-6}\,/^\circ \mathrm{C}.
$$

**Step 3: Initial and Final Volumes**

Initial volume:

$$
V_0 = L_0^3 = (0.05)^3 = 0.000125\ \mathrm{m^3}.
$$

Expanded volume:

$$
V = V_0(1 + \beta \Delta T)
$$

$$
V = 0.000125[1 + (55.2 \times 10^{-6})(68)].
$$

$$
V = 0.000125(1 + 0.0037536) = 0.00012547\ \mathrm{m^3}.
$$

**Step 4: Final Answer**

$$
\boxed{V = 0.00012547\ \mathrm{m^3}}
$$

**Note:** The multiplier from m³ to mm³ is 1 × 10⁹. The brass cube expands from **125000 mm³** to **125469.20 mm³** when heated from **10°C** to **78°C**.

### Code

``` python
# Thermal Expansion of a Brass Cube
# --------------------------------
# Given:
#   L0 = 50 mm  (initial side length)
#   T1 = 10 °C  (initial temperature)
#   T2 = 78 °C  (final temperature)
#   α  = 18.4 × 10⁻⁶ /°C  (linear expansion coefficient for brass)
#
# Find:
#   Final volume V at 78 °C (in mm³).

# Given values
L0 = 50e-3                # convert mm to m
T1 = 10
T2 = 78
alpha = 18.4e-6           # /°C

# Temperature change
delta_T = T2 - T1

# Volumetric expansion coefficient
beta = 3 * alpha

# Initial and final volumes (in m³)
V0 = L0 ** 3
V = V0 * (1 + beta * delta_T)

# Convert to mm³ for output (1 m³ = 1e9 mm³)
V0_mm3 = V0 * 1e9
V_mm3 = V * 1e9
delta_V = V_mm3 - V0_mm3

# Display results
print(f"Initial Volume (mm³): {V0_mm3:.2f}")
print(f"Final Volume (mm³):   {V_mm3:.2f}")
print(f"Increase in Volume (mm³): {delta_V:.2f}")
```