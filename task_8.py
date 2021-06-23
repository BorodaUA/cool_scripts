import argparse
from argparse import RawTextHelpFormatter
import sys


FILE_NAME = __file__.split('/')[-1]
WELCOME_MSG = (
    "\n*** Welcome to the Fibonacci numbers for the range ***\n"
    "This program will print all fibonacci numbers, "
    "in the range of numbers specified by the user. \n"
    "Usage example: \n"
    f"python {FILE_NAME} -sr 50 -er 200 \n"
    f"python {FILE_NAME} --start_range 50 --end_range 200 \n"
)


def fibo_range(start_range, end_range):
    '''
    Return string of fibonacci sequence in given range
    '''
    a = 0
    b = 1
    #
    result = []
    #
    while a <= end_range:
        result.append(a)
        a, b = b, a+b
    #
    start_index = find_index_of_closest_int(result, start_range)
    #
    result = [str(i) for i in result[start_index:]]
    #
    return ','.join(result)


def main(start_range, end_range):
    '''
    Starting point of the program
    '''
    if end_range <= start_range:
        print('"end_range" must be greater then "start_range"')
        sys.exit()
    print(
        fibo_range(
            start_range=start_range,
            end_range=end_range
        )
    )


def find_index_of_closest_int(numbers_lst, value):
    '''
    Return index of item closest to the value
    '''
    min_difference = value
    min_difference_index = 0
    #
    for num in enumerate(numbers_lst):
        difference = abs(value - num[1])
        #
        if min_difference >= difference:
            min_difference = difference
            min_difference_index = num[0]
    #
    return min_difference_index


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
    #
    parser = argparse.ArgumentParser(
        description=WELCOME_MSG,
        formatter_class=RawTextHelpFormatter,
    )
    #
    parser.add_argument(
        "-sr",
        "--start_range",
        help='The start number of the range',
        type=is_valid_positive_int
    )
    #
    parser.add_argument(
        "-er",
        "--end_range",
        help='The end number of the range',
        type=is_valid_positive_int
    )
    args = parser.parse_args()
    #
    if args.start_range is None or args.end_range is None:
        print(WELCOME_MSG)
        sys.exit()
    #
    main(
        start_range=args.start_range,
        end_range=args.end_range
    )
