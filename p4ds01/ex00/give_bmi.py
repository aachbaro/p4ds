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
        if (len(height) != len(weight)):
            raise ValueError("Lists must have the same length")
        if not isinstance(height, (int, float)):
            raise TypeError("Elements of lists must be integer or float")
        if not isinstance(weight, (int, float)):
            raise TypeError("Elements of lists must be integer or float")
        bmi_values = []
        for h, w in zip(height, weight):
            if h <= 0 or w <= 0:
                raise ValueError("Height or weight cant be negative or null")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
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
        if not isinstance(limit, (int, float)):
            raise TypeError("Limit must be an integer or a float")
        is_under_limit = []
        for item in bmi:
            is_under_limit.append(item > limit)
        return is_under_limit
    except Exception as error:
        print("Error: ", error)
