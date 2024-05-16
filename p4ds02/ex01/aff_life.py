import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Plot life expectancy projections for France."""
    try:
        data = load("life_expectancy_years.csv")
        data = data.loc[data['country'] == 'France']
        years = data.columns[1:]
        life_expency = data.values[0][1:]
        plt.plot(years, life_expency, label="France")
        plt.title("France life expectency Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectency")
        plt.xticks(years[::40])
        plt.show()
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    main()
