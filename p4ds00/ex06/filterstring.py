from ft_filter import ft_filter
import sys


def main():
    """
    This function processes command line arguments and filters
    words based on a specified length.
    The function first checks if the correct number of command line
    arguments are provided and if the second argument is a valid
    integer. If so, it splits the first argument into words
    and filters them based on the length specified by the second argument.

    Parameters:
    None

    Returns:
    None
    """
    try:
        print("step 1")
        if len(sys.argv) == 3 and sys.argv[2].isdigit():
            words = sys.argv[1].split()
            n = int(sys.argv[2])
            print(ft_filter(lambda word: len(word) > n, words))
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
