# This code produces the bar graph for the measurements lab

import matplotlib.pyplot as plt

trials = [1, 2, 3, 4, 5]
densities = [
    0.914141414,
    0.969696970,
    0.953525641,
    0.995500000,
    0.991816367
]

average_density = 0.964936078
true_density = 0.9978  # Water density at 22°C

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

# True density line
plt.axhline(
    true_density,
    linestyle="-",
    linewidth=2.5,
    color="red",
    label=f"True Density at 22°C = {true_density:.4f} g/mL"
)

# Add density values above bars
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.006,
        f"{density:.4f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)
plt.title("Density Measurements of Water — 100 mL Beaker at 22°C")

plt.xticks(trials)
plt.ylim(0.85, 1.03)

plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()