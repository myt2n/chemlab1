# This code produces the bar graph for the measurements lab


import matplotlib.pyplot as plt

trials = [1, 2, 3, 4, 5]
densities = [0.988, 0.970, 0.977333333, 0.98075, 0.9834]

average_density = 0.979896667
true_density = 0.99802  # Water density at 21°C, g/mL

plt.figure(figsize=(9, 6))

bars = plt.bar(
    trials,
    densities,
    width=0.6,
    edgecolor="black",
    label="Individual Trial Density"
)

# Average density line
plt.axhline(
    average_density,
    linestyle="--",
    linewidth=2.5,
    color="blue",
    label=f"Average Density = {average_density:.4f} g/mL"
)

# True/theoretical density line
plt.axhline(
    true_density,
    linestyle="-",
    linewidth=2.5,
    color="red",
    label=f"True Density at 21°C = {true_density:.4f} g/mL"
)

# Add density values above each bar
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.0015,
        f"{density:.4f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)
plt.title("Density Measurements of Water — Volumetric Pipette at 21°C", fontsize=14)

plt.xticks(trials)
plt.ylim(0.94, 1.01)

plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()