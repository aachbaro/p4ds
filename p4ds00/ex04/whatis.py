import sys

if (len(sys.argv) < 2):
     exit()

try:
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
    assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"

    number = int(sys.argv[1])

    if (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)
