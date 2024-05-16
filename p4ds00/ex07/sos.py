import sys


def create_morse_dict():
    """
    Create and return a morse dictionnary

    Returns:
        dict: morse dictionnary
    """
    return {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
        "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
        "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
        "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ",
        "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
    }


def encode_to_morse(s, morse_dict):
    """
    return s in morse code

    Args:
        s (str): the string to translate in morse
        morse_dict (dict): the morse dictionnary

    Returns:
        str: the encoded string
    """
    assert isinstance(s, str), "the arguments are bad"

    morse_code = ""
    for char in s.upper():
        morse_code += morse_dict.get(char, "")
        if not morse_dict.get(char, ""):
            raise AssertionError("the arguments are bad")
    return morse_code


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        morse_dict = create_morse_dict()
        morse_code = encode_to_morse(s, morse_dict)
        print(morse_code)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
