from ft_filter import ft_filter
import sys


def main():
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
