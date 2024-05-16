import matplotlib.pyplot as plt
from load_csv import load


def main():
    lexye = load("life_expectancy_years.csv")
    gnp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    lexye = lexye['1900']
    gnp = gnp['1900']
    plt.scatter(gnp, lexye)
    plt.title("1900")
    plt.ylabel("Life expectency")
    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()

if __name__ == "__main__":
    main()
