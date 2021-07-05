import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from number_2_words import NumbersToWords # noqa

HELP_MSG = (
    '***Welcome to the Numbers 2 Words converter *** \n'
    'Please type in number(s), that will be converted to word(s): '
)
NUMBER_TO_LARGE = (
    'Handling numbers above 999 999 999 not implemented yet.'
)
NEGATIVE_NUM_MSG = 'Please enter a number greater then zero'
ZERO = 'ноль'
NOT_INTEGER_MSG = 'Please enter a valid number'


def main():
    '''
    Starting point of the program
    '''
    try:
        user_input = int(input(HELP_MSG))
        if user_input == 0:
            print(ZERO)
            sys.exit()
        if user_input < 0:
            print(NEGATIVE_NUM_MSG)
            sys.exit()
        if user_input > 999999999:
            print(NUMBER_TO_LARGE)
            sys.exit()
        number_inst = NumbersToWords(user_input)
        print(number_inst)
    except ValueError:
        print(NOT_INTEGER_MSG)


if __name__ == "__main__":
    main()
