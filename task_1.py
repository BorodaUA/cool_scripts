import sys


class ChessBoard:
    """
    A chess board class
    """
    HELP_MSG = (
        "ChessBoard class creates a custom chess board with given \n"
        "height and width parameters that must be a positive integers \n"
        "Example: ChessBoard(8,8) \n"
        "Example: ChessBoard(height=10, width=10) \n"
        "Example: ChessBoard(12, width=12) \n"
    )
    ERROR_MSG = (
        "Please provide valid integers "
        "as height and width parameters \n"
        "Example: ChessBoard(8,8) \n"
        "Example: ChessBoard(height=10, width=10) \n"
        "Example: ChessBoard(12, width=12) \n"
    )

    def __new__(cls, *args, **kwargs):
        """
        The new method with validation of the *args, **kwargs
        """
        if len(args) == 0 and len(kwargs) == 0:
            print(cls.HELP_MSG)
            sys.exit()
        if len(args) + len(kwargs) > 2:
            print(cls.ERROR_MSG)
            sys.exit()
        if len(args) + len(kwargs) < 2:
            print(cls.ERROR_MSG)
            sys.exit()
        if len(args) != 0 or len(kwargs) != 0:
            return super().__new__(cls)

    def __init__(self, height, width):
        """
        An initialization of the ChessBoard class with two parameters:
        height: int
        width: int
        """
        self.height = self.is_valid_height(height)
        self.width = self.is_valid_width(width)
        print(self.create_chess_board())

    def is_valid_height(self, height):
        '''
        A validation method, checks for int as the variable type
        and height to be a positive integer
        '''
        if type(height) != int:
            print("Please provide valid integer as height parameter")
            sys.exit()
        if height < 0:
            print("Parameter height must be a positive integer")
            sys.exit()
        return height

    def is_valid_width(self, width):
        '''
        A validation method, checks for int as the variable type
        and width to be a positive integer
        '''
        if type(width) != int:
            print("Please provide valid integer as width parameter")
            sys.exit()
        if width < 0:
            print("Parameter width must be a positive integer")
            sys.exit()
        return width

    def create_chess_board(self):
        """
        Return a chess board of given height by
        combining:
        even "* * * * " and
        odd  " * * * *" rows
        """
        result = []
        even_row = ''.join(
            ['*' if i % 2 == 0 else ' ' for i in range(self.width)]
        )
        odd_row = ''.join(
            [' ' if i % 2 == 0 else '*' for i in range(self.width)]
        )
        for h in range(self.height):
            if h % 2 == 0:
                result.append(''.join(even_row))
            else:
                result.append(''.join(odd_row))
        result = "\n".join(result)
        return result


print('ABCDEFGH')
ChessBoard(8, width=8)
