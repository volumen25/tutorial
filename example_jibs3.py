"""
Crane Geometry Optimization - Finding Minimum Force Configuration

Analyzes how changing the geometry affects forces in the jib and tie,
helping identify the optimal angles for minimum effort.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# INPUT PARAMETERS - FIXED CONSTRAINTS
# =============================================================================

# Fixed parameters
post_length_m = 8  # meters (vertical post - fixed)
load_force_kn = 20  # kilonewtons (applied load - fixed)

# Variable parameters to explore
jib_length_m = 13  # meters (can be varied)
tie_length_m = 9  # meters (can be varied)

# =============================================================================
# FORCE CALCULATION FUNCTION
# =============================================================================


def calculate_forces(post, jib, tie, load):
    """
    Calculate forces in jib and tie given triangle geometry.

    Args:
        post: Length of vertical post (m)
        jib: Length of jib beam (m)
        tie: Length of tie cable (m)
        load: Applied load force (kN)

    Returns:
        Tuple of (force_in_jib, force_in_tie, angle_at_post_deg,
                  angle_at_tie_deg, angle_at_jib_deg)
        Returns None if triangle is invalid
    """
    # Check triangle inequality (valid triangle must exist)
    if post + jib <= tie or post + tie <= jib or jib + tie <= post:
        return None

    # Calculate angles using law of cosines
    try:
        angle_at_post_rad = math.acos(
            (jib**2 + tie**2 - post**2) / (2 * jib * tie)
        )
        angle_at_tie_rad = math.acos(
            (jib**2 + post**2 - tie**2) / (2 * jib * post)
        )
        angle_at_jib_rad = math.pi - angle_at_post_rad - angle_at_tie_rad

        # Calculate forces using law of sines
        force_in_jib = (
            load * math.sin(angle_at_jib_rad) / math.sin(angle_at_post_rad)
        )
        force_in_tie = (
            load * math.sin(angle_at_tie_rad) / math.sin(angle_at_post_rad)
        )

        # Convert angles to degrees
        angle_at_post_deg = math.degrees(angle_at_post_rad)
        angle_at_tie_deg = math.degrees(angle_at_tie_rad)
        angle_at_jib_deg = math.degrees(angle_at_jib_rad)

        return (
            force_in_jib,
            force_in_tie,
            angle_at_post_deg,
            angle_at_tie_deg,
            angle_at_jib_deg,
        )
    except ValueError:
        # Invalid geometry (e.g., arccos of value > 1)
        return None


# =============================================================================
# ANALYZE VARYING JIB ANGLE (BY CHANGING TIE LENGTH)
# =============================================================================

# Range of tie lengths to test (keeping jib and post fixed)
tie_lengths = np.linspace(5, 20, 100)

jib_forces = []
tie_forces = []
jib_angles = []
valid_tie_lengths = []

print("Analyzing effect of varying tie length (jib angle)...\n")

for tie_len in tie_lengths:
    result = calculate_forces(
        post_length_m, jib_length_m, tie_len, load_force_kn
    )
    if result:
        f_jib, f_tie, _, _, angle_jib = result
        jib_forces.append(f_jib)
        tie_forces.append(f_tie)
        jib_angles.append(angle_jib)
        valid_tie_lengths.append(tie_len)

# Find optimal configuration
min_jib_idx = np.argmin(jib_forces)
min_tie_idx = np.argmin(tie_forces)
min_total_idx = np.argmin(np.array(jib_forces) + np.array(tie_forces))

print("=" * 79)
print("OPTIMIZATION RESULTS - VARYING TIE LENGTH")
print("=" * 79)
print(f"Fixed: Post = {post_length_m} m, Jib = {jib_length_m} m\n")

print("Minimum jib force configuration:")
print(f"  Tie length: {valid_tie_lengths[min_jib_idx]:.2f} m")
print(f"  Jib force:  {jib_forces[min_jib_idx]:.2f} kN")
print(f"  Tie force:  {tie_forces[min_jib_idx]:.2f} kN")
print(f"  Jib angle:  {jib_angles[min_jib_idx]:.2f}°\n")

print("Minimum tie force configuration:")
print(f"  Tie length: {valid_tie_lengths[min_tie_idx]:.2f} m")
print(f"  Jib force:  {jib_forces[min_tie_idx]:.2f} kN")
print(f"  Tie force:  {tie_forces[min_tie_idx]:.2f} kN")
print(f"  Jib angle:  {jib_angles[min_tie_idx]:.2f}°\n")

print("Minimum total force configuration:")
print(f"  Tie length: {valid_tie_lengths[min_total_idx]:.2f} m")
print(f"  Jib force:  {jib_forces[min_total_idx]:.2f} kN")
print(f"  Tie force:  {tie_forces[min_total_idx]:.2f} kN")
print(
    f"  Total:      {jib_forces[min_total_idx] + tie_forces[min_total_idx]:.2f} kN"
)
print(f"  Jib angle:  {jib_angles[min_total_idx]:.2f}°\n")

print(f"Current configuration (tie = {tie_length_m} m):")
current_result = calculate_forces(
    post_length_m, jib_length_m, tie_length_m, load_force_kn
)
if current_result:
    f_jib_curr, f_tie_curr, _, _, angle_jib_curr = current_result
    print(f"  Jib force:  {f_jib_curr:.2f} kN")
    print(f"  Tie force:  {f_tie_curr:.2f} kN")
    print(f"  Total:      {f_jib_curr + f_tie_curr:.2f} kN")
    print(f"  Jib angle:  {angle_jib_curr:.2f}°")

# =============================================================================
# VISUALIZATION
# =============================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot 1: Forces vs Tie Length
ax1.plot(valid_tie_lengths, jib_forces, "b-", linewidth=2, label="Jib Force")
ax1.plot(valid_tie_lengths, tie_forces, "r-", linewidth=2, label="Tie Force")
ax1.plot(
    valid_tie_lengths,
    np.array(jib_forces) + np.array(tie_forces),
    "g--",
    linewidth=2,
    label="Total Force",
)

# Mark optimal points
ax1.plot(
    valid_tie_lengths[min_total_idx],
    jib_forces[min_total_idx] + tie_forces[min_total_idx],
    "go",
    markersize=10,
    label="Minimum Total",
)

# Mark current configuration
if current_result:
    ax1.plot(
        tie_length_m,
        f_jib_curr + f_tie_curr,
        "ko",
        markersize=8,
        label="Current Config",
    )

ax1.set_xlabel("Tie Length (m)", fontsize=12)
ax1.set_ylabel("Force (kN)", fontsize=12)
ax1.set_title(
    f"Force Analysis: Post={post_length_m}m, Jib={jib_length_m}m, "
    f"Load={load_force_kn}kN",
    fontsize=14,
)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: Jib Angle vs Tie Length
ax2.plot(valid_tie_lengths, jib_angles, "m-", linewidth=2, label="Jib Angle")
ax2.axhline(
    y=45, color="gray", linestyle="--", alpha=0.5, label="45° Reference"
)
ax2.plot(
    valid_tie_lengths[min_total_idx],
    jib_angles[min_total_idx],
    "go",
    markersize=10,
    label="Optimal Angle",
)
if current_result:
    ax2.plot(
        tie_length_m,
        angle_jib_curr,
        "ko",
        markersize=8,
        label="Current Angle",
    )

ax2.set_xlabel("Tie Length (m)", fontsize=12)
ax2.set_ylabel("Jib Angle (degrees)", fontsize=12)
ax2.set_title("Jib Angle vs Tie Length", fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(
    "/home/claude/crane_optimization.png", dpi=150, bbox_inches="tight"
)
print("\n" + "=" * 79)
print("Graph saved as: crane_optimization.png")
print("=" * 79)

# =============================================================================
# KEY INSIGHTS
# =============================================================================

print("\n" + "=" * 79)
print("KEY INSIGHTS FOR OPTIMAL CRANE DESIGN")
print("=" * 79)
print("""
1. TOTAL FORCE MINIMIZATION:
   - The minimum total force occurs when the geometry creates a balanced
     load distribution between the jib and tie.
   - Optimal jib angle is typically in the range of 30-60°.

2. ANGLE CONSIDERATIONS:
   - Very shallow angles (<30°) create high compression in the jib.
   - Very steep angles (>70°) create high tension in the tie.
   - The sweet spot balances both forces.

3. PRACTICAL RECOMMENDATIONS:
   - For your fixed post (8m) and jib (13m), the optimal tie length
     minimizes the total structural load.
   - Consider the trade-off between reach (horizontal distance) and
     force requirements.

4. DESIGN MODIFICATIONS:
   - Increasing jib length provides more reach but may increase forces.
   - Adjusting tie length is often the easiest way to optimize.
   - Consider variable-length ties (winches) for different load positions.
""")
