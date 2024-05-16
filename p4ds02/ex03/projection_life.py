import matplotlib.pyplot as plt
from load_csv import load


def main():
    """displays the projection of life expectancy in relation
    to the gross national product of he year 1900 for each country"""
    try:
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
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    main()
