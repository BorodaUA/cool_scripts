import argparse
from argparse import RawTextHelpFormatter
import sys
from sequence_number import SequenceNumber


FILE_NAME = sys.argv[0]
WELCOME_MSG = (
    "\n*** Welcome to the Number of squence ***\n"
    "This program will print all the numbers, "
    "whose squares are less than the number specified by the user. \n"
    "Usage example: \n"
    f"python {FILE_NAME} -n 50 \n"
    f"python {FILE_NAME} --number 50 \n"
)


def main(number):
    '''
    Starting point of the program
    '''
    the_number = SequenceNumber(number=number)
    print(the_number.numbers_below)


def is_valid_positive_int(value):
    '''
    A validation func, checks for int as the variable type
    and value to be a positive integer
    '''
    try:
        value = int(value)
        if value < 0:
            raise argparse.ArgumentTypeError(
                f"{value} is not a positive integer"
            )
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"{value} is not an integer"
        )
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=WELCOME_MSG,
        formatter_class=RawTextHelpFormatter,
    )
    #
    parser.add_argument(
        "-n",
        "--number",
        help='The number to check, check squares and print numbers below it',
        type=is_valid_positive_int
    )
    #
    args = parser.parse_args()
    #
    if not args.number:
        print(WELCOME_MSG)
        sys.exit()
    #
    main(number=args.number)
