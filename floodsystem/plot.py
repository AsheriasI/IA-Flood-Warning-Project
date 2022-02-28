import numpy as np
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """Displays a plot of the water level data against time for a station, including
    plot lines for typical low and high levels"""
    low = station.typical_range[0]
    high = station.typical_range[1]

    plt.plot(dates, levels)

    plt.axhline(low, linestyle="dashed", color="green")
    plt.axhline(high, linestyle="dashed", color="red")

    plt.legend(("Water level", "Typical low", "Typical high"))
    plt.xlabel("Dates")
    plt.ylabel("Water level data (m)")
    plt.title(station.name + " Water Level")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
