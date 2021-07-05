import random
from task_1_chess_board.task_1 import ChessBoard


def test_chess_board_cli_valid_parameters(cli_client):
    '''
    Test task_1_chess_board/task_1.py valid parameters
    '''
    chess_board_height = random.randint(1, 25)
    chess_board_width = random.randint(1, 25)
    #
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-ht',
        f'{chess_board_height}',
        '-wt',
        f'{chess_board_width}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    #
    a_chess_board = ChessBoard(chess_board_height, chess_board_width)
    a_chess_board = f'{str(a_chess_board)}\n'
    #
    assert 0 == exitcode
    assert b'' == cli_error
    assert a_chess_board == cli_out


def test_chess_board_cli_no_parameters(cli_client):
    '''
    Test task_1_chess_board/task_1.py no parameters
    '''
    command = ('python', 'task_1_chess_board/task_1.py')
    cli_out, cli_error, exitcode = cli_client(command)
    HELP_MSG = (
        b"*** Welcome to the ChessBoard generator ***\n"
        b"You can generate a chess board with custom height "
        b"and width parameters \n"
        b"height and width parameters that must be a positive integers \n"
        b"Example: python task_1.py --height 8 --width 8 \n"
        b"Example: python task_1.py -ht 8 -wt 8 \n\n"
    )
    assert 0 == exitcode
    assert b'' == cli_error
    assert HELP_MSG == cli_out


def test_chess_board_cli_only_height_param(cli_client):
    '''
    Test task_1_chess_board/task_1.py only -ht param
    '''
    chess_board_height = random.randint(1, 25)
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-ht',
        f'{chess_board_height}',
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out
    HELP_MSG = (
        b"*** Welcome to the ChessBoard generator ***\n"
        b"You can generate a chess board with custom height "
        b"and width parameters \n"
        b"height and width parameters that must be a positive integers \n"
        b"Example: python task_1.py --height 8 --width 8 \n"
        b"Example: python task_1.py -ht 8 -wt 8 \n\n"
    )
    assert 0 == exitcode
    assert b'' == cli_error
    assert HELP_MSG == cli_out


def test_chess_board_cli_only_width_param(cli_client):
    '''
    Test task_1_chess_board/task_1.py only -wt param
    '''
    chess_board_width = random.randint(1, 25)
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-wt',
        f'{chess_board_width}',
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out
    HELP_MSG = (
        b"*** Welcome to the ChessBoard generator ***\n"
        b"You can generate a chess board with custom height "
        b"and width parameters \n"
        b"height and width parameters that must be a positive integers \n"
        b"Example: python task_1.py --height 8 --width 8 \n"
        b"Example: python task_1.py -ht 8 -wt 8 \n\n"
    )
    assert 0 == exitcode
    assert b'' == cli_error
    assert HELP_MSG == cli_out


def test_chess_board_cli_height_param_not_int(cli_client):
    '''
    Test task_1_chess_board/task_1.py -ht A -wt INT
    '''
    chess_board_height = random.randint(1, 25)
    chess_board_width = random.randint(1, 25)
    #
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-ht',
        'A',
        '-wt',
        f'{chess_board_width}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    #
    a_chess_board = ChessBoard(chess_board_height, chess_board_width)
    a_chess_board = f'{str(a_chess_board)}\n'
    #
    ERROR_MSG = (
        b'usage: task_1.py [-h] [-ht HEIGHT] [-wt WIDTH]\n'
        b'task_1.py: error: argument -ht/--height: A is not an integer\n'
    )
    #
    assert 2 == exitcode
    assert ERROR_MSG == cli_error
    assert '' == cli_out


def test_chess_board_cli_width_param_not_int(cli_client):
    '''
    Test task_1_chess_board/task_1.py -ht INT -wt A
    '''
    chess_board_height = random.randint(1, 25)
    chess_board_width = random.randint(1, 25)
    #
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-ht',
        f'{chess_board_height}',
        '-wt',
        'B'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    #
    a_chess_board = ChessBoard(chess_board_height, chess_board_width)
    a_chess_board = f'{str(a_chess_board)}\n'
    #
    ERROR_MSG = (
        b'usage: task_1.py [-h] [-ht HEIGHT] [-wt WIDTH]\n'
        b'task_1.py: error: argument -wt/--width: B is not an integer\n'
    )
    #
    assert 2 == exitcode
    assert ERROR_MSG == cli_error
    assert '' == cli_out


def test_chess_board_cli_width_param_negative_int(cli_client):
    '''
    Test task_1_chess_board/task_1.py -ht INT -wt -10
    '''
    chess_board_height = random.randint(1, 25)
    chess_board_width = random.randint(-111, -1)
    #
    command = (
        'python',
        'task_1_chess_board/task_1.py',
        '-ht',
        f'{chess_board_height}',
        '-wt',
        f'{chess_board_width}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    cli_error = cli_error.decode()
    #
    a_chess_board = ChessBoard(chess_board_height, chess_board_width)
    a_chess_board = f'{str(a_chess_board)}\n'
    #
    ERROR_MSG = (
        'usage: task_1.py [-h] [-ht HEIGHT] [-wt WIDTH]\n'
        'task_1.py: error: argument '
        f'-wt/--width: {chess_board_width} is not a positive integer\n'
    )
    #
    assert 2 == exitcode
    assert ERROR_MSG == cli_error
    assert '' == cli_out
