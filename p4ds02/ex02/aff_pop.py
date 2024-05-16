import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Plot total population for France and Belgium."""
    try:
        data = load("population_total.csv")
        data_france = data.loc[data['country'] == 'France']
        data_belgium = data.loc[data['country'] == 'Belgium']
        pop_france_str = data_france.values[0][1:250]
        pop_belgium_str = data_belgium.values[0][1:250]
        pop_france = [float(pop.replace('M', '')) * 1e6 for pop in pop_france_str]
        pop_belgium = [float(pop.replace('M', '')) * 1e6 for pop in pop_belgium_str]
        years = data.columns[1:250]
        plt.plot(years, pop_france, label="France")
        plt.plot(years, pop_belgium, label="Belgium")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(years[::40])
        plt.yticks()
        plt.yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
        plt.legend()
        plt.show()
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    main()
