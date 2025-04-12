import pandas as pd
import matplotlib.pyplot as plt


def make_chart(fname, year):
    df = pd.read_csv(fname)
    output_name = fname.split('.')[0]

    x = df["Model"]
    y = df["Power Consumption (MWh)"]

    plt.figure(figsize=(10,6))

    plt.bar(x,y)

    plt.title(f"AI Models and Their Energy Energy Consumption During Training ({output_name.strip('-')}, {year})")
    plt.xlabel("Model")
    plt.ylabel("Power Consumption (MWh)")

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(fname=output_name)

make_chart('luccioni-et-al.csv', 2022)
make_chart('castro.csv', 2024)