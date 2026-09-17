# This code produces the bar graph for the measurements lab

import matplotlib.pyplot as plt

trials = [1, 2, 3, 4]
densities = [7.13, 7.45, 6.84, 7.77]

average_density = 7.2975
true_density = 7.18  # Approximate density of a modern U.S. penny

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
    label=f"Average Density = {average_density:.4f} g/cm³"
)

# True/theoretical density line
plt.axhline(
    true_density,
    linestyle="-",
    linewidth=2.5,
    color="red",
    label=f"True Density = {true_density:.2f} g/cm³"
)

# Add density values above each bar
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.08,
        f"{density:.2f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/cm³)", fontsize=12)
plt.title("Density Measurements of a Penny", fontsize=14)

plt.xticks(trials)
plt.ylim(6.5, 8.1)

plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()