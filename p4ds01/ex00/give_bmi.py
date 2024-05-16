import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list:
    """
    Gives a list of BMI from two lists of weight and height

    ARGS:
        height list[int | float]    : list of heights (metters)
        weight list[int | float]    : list of weights (kilograms)
    RETURNS:
        list[int | float]           : list of calculated BMI
    """
    try:
        heights = np.array(height, dtype="f")
        weights = np.array(weight, dtype="f")
        if (len(heights) != len(weights)):
            raise ValueError("Lists must have the same length")
        if (heights < 0).any() or (weights < 0).any():
            raise ValueError("Height or weight cant be negative or null")
        bmi_values = weights / heights ** 2
        return bmi_values.tolist()
    except Exception as error:
        print("Error: ", error)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Take list of BMI and says if its above a given limit or not

    ARGS:
        bmi: list[int | float]: the list of bmi
        limit: int: the limit
    RETURN:
        list[bool]: a list of boolean that says if each bmi
        if its above the limit or not
    """
    try:
        bmi_arr = np.array(bmi, dtype="f")
        if not isinstance(limit, (int, float)):
            raise TypeError("Limit must be an integer or a float")
        is_under_limit = bmi_arr < limit
        return is_under_limit.tolist()
    except Exception as error:
        print("Error: ", error)


def main():
    return


if __name__ == "__main__":
    main()
