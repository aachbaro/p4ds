import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and
    end arguments.
    ARGS:
        family (list): a 2d array
        start (int): the start of the new list
        end (int): the end of the new list
    RETURNS:
        (list): the new array
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        # if not family:
        #     raise ValueError("family cant be empty")
        sublist_length = len(family[0])
        if not all(len(sublist) == sublist_length for sublist in family):
            raise ValueError("all list in family must have the same length")
        arr = np.array(family)
        if any(dim == 2 for dim in arr.shape):
            new_arr = arr[start:end]
            print(f"My shape is : {arr.shape}")
            print(f"My new shape is : {new_arr.shape}")
            return new_arr.tolist()
        else:
            raise ValueError("family must be a 2d array")
    except Exception as error:
        print("Error: ", error)
