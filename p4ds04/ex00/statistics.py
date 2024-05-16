
def mean(vector):
    """Gives the mean of the array"""
    return (sum(vector) / len(vector))

def median(vector) -> float:
    """Gives the median of the array"""
    vector.sort()
    if not len(vector) % 2:
        median = (vector[len(vector) // 2 - 1] + vector[len(vector) // 2]) / 2
    else:
        median = vector[len(vector) // 2]
    return median


def quartile(vector) -> float:
    """Return the quartile of a given sequence"""
    sort = sorted(vector)
    n = len(sort)
    q1_index = n // 4
    q3_index = 3 * n // 4
    q1 = float(sort[q1_index])
    q3 = float(sort[q3_index])
    return [q1, q3]

def std(vector):
    """Gives the standard variation of a given vector"""
    return (sum([(x - mean(vector)) ** 2 for x in vector]) / len(vector)) ** 0.5

def var(vector):
    """Gives the variance of a given vector"""
    return (std(vector) ** 2)



def ft_statistics(*args: any, **kwargs: any) -> None:
    """Gives statistics about the numbers given in parametters"""
    vector = [x for x in args]
    for key, value in kwargs.items():
        if not vector:
            print("ERROR")
        elif value == "mean":
            print(f"mean : {mean(vector)}")
        elif value == "median":
            print(f"median : {median(vector)}")
        elif value == "quartile":
            print(f"quartile: {quartile(vector)}")
        elif value == "std":
            print(f"std : {std(vector)}")
        elif value == "var":
            print(f"var : {var(vector)}")
        