import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880–latest)
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_extended = pd.Series(range(1880, 2051))
    line1 = result.slope * years_extended + result.intercept
    ax.plot(years_extended, line1, color="red")

    # Second line of best fit (2000–latest)
    df_recent = df[df["Year"] >= 2000]
    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent_extended = pd.Series(range(2000, 2051))
    line2 = result_recent.slope * years_recent_extended + result_recent.intercept
    ax.plot(years_recent_extended, line2, color="green")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return figure
    fig.savefig("sea_level_plot.png")
    return fig
