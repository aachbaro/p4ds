import sys


def analyse_string(str):
    """
        This functions parse the given string and print the numbers:
         - uppercases
         - lowercases
         - punctuation marks
         - spaces
         - digits

         Args:
            str (str): The string to analyse

        Returns:
            nothing.
    """
    uppers = 0
    lowers = 0
    puncts = 0
    spaces = 0
    digits = 0
    for char in str:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char in ",.?!;:-'\"":
            puncts += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
    str_len = len(str)
    print(f"The text contains {str_len} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{puncts} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Anayse a given string and gives the amount of letters 
    (uper and lower), punctuation marks, spaces and digits"""
    try:
        if len(sys.argv) == 1:
            input_string = input("What is the text to count?\n")
        elif len(sys.argv) == 2:
            input_string = sys.argv[1]
        else:
            raise AssertionError("More than one argument is provided")
        analyse_string(input_string)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
