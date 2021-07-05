import random
from task_1_chess_board.task_1 import ChessBoard


def test_create_chess_board_valid_data():
    '''
    Test create the ChessBoard instance with
    valid data
    '''
    chess_board_height = random.randint(1, 25)
    chess_board_width = random.randint(1, 25)
    #
    chess_board = ChessBoard(chess_board_height, chess_board_width)
    #
    assert chess_board_height == chess_board.height
    assert chess_board_width == chess_board.width


def test_str_chess_board_valid_data():
    '''
    Test str representation the ChessBoard instance with
    valid data
    '''
    #
    expected_chess_board = (
        '⬜⬛⬜⬛⬜⬛⬜⬛\n'
        '⬛⬜⬛⬜⬛⬜⬛⬜\n'
        '⬜⬛⬜⬛⬜⬛⬜⬛\n'
        '⬛⬜⬛⬜⬛⬜⬛⬜'
    )
    chess_board = ChessBoard(4, 8)
    str_chess_board = str(chess_board)
    #
    assert expected_chess_board == str_chess_board
