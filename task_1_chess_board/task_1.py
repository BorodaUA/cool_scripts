import sys
import argparse
from argparse import RawTextHelpFormatter


class ChessBoard:
    """
    A chess board class
    """

    def __init__(self, height, width):
        """
        An initialization of the ChessBoard class with two parameters:
        height: int
        width: int
        """
        self.height = height
        self.width = width

    def __str__(self):
        """
        Return string of a chess board of given height by
        combining:
        even "* * * * " and
        odd  " * * * *" rows
        """
        result = []
        even_row = ''.join(
            ['\u2B1C' if i % 2 == 0 else '\u2B1B' for i in range(self.width)]
        )
        odd_row = ''.join(
            ['\u2B1B' if i % 2 == 0 else '\u2B1C' for i in range(self.width)]
        )
        for h in range(self.height):
            if h % 2 == 0:
                result.append(''.join(even_row))
            else:
                result.append(''.join(odd_row))
        result = "\n".join(result)
        return result


FILE_NAME = __file__.split('/')[-1]
HELP_MSG = (
    "*** Welcome to the ChessBoard generator ***\n"
    "You can generate a chess board with custom height "
    "and width parameters \n"
    "height and width parameters that must be a positive integers \n"
    f"Example: python {FILE_NAME} --height 8 --width 8 \n"
    f"Example: python {FILE_NAME} -ht 8 -wt 8 \n"
)


def main(height, width):
    '''
    Starting point of the program
    '''
    chess_board = ChessBoard(height, width)
    print(chess_board)


def is_positive_int(value):
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
        description=HELP_MSG,
        formatter_class=RawTextHelpFormatter,
    )
    #
    parser.add_argument(
        "-ht",
        "--height",
        help='The height of the chess board',
        type=is_positive_int
    )
    parser.add_argument(
        "-wt",
        "--width",
        help='The width of the chess board',
        type=is_positive_int
        )
    args = parser.parse_args()
    #
    if not args.height or not args.width:
        print(HELP_MSG)
        sys.exit()
    #
    main(height=args.height, width=args.width)
