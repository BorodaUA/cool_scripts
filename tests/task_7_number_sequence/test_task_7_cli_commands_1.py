import random


def test_number_sequence_cli_no_parameters(cli_client):
    '''
    Test task_7_number_sequence/task_7.py no parameters
    '''
    command = ('python', 'task_7_number_sequence/task_7.py')
    cli_out, cli_error, exitcode = cli_client(command)
    #
    HELP_MSG = (
        b"\n*** Welcome to the Number of squence ***\n"
        b"This program will print all the numbers, whose squares are less than"
        b" the number specified by the user. \nUsage example: \n"
        b"python task_7_number_sequence/task_7.py -n 50 \n"
        b"python task_7_number_sequence/task_7.py --number 50 \n\n"
    )
    assert 0 == exitcode
    assert b'' == cli_error
    assert HELP_MSG == cli_out


def test_number_sequence_cli_n_valid_int(cli_client):
    '''
    Test task_7_number_sequence/task_7.py -n valid int
    check for square of last number in the sequence
    <= then test_number
    '''
    test_number = random.randint(1, 100000)
    #
    command = (
        'python',
        'task_7_number_sequence/task_7.py',
        '-n',
        f'{test_number}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    #
    last_number_square = int(cli_out.split(',')[-1].strip()) ** 2
    #
    assert 0 == exitcode
    assert b'' == cli_error
    assert test_number >= last_number_square


def test_number_sequence_cli_n_not_int(cli_client):
    '''
    Test task_7_number_sequence/task_7.py -n not int
    '''
    not_int_list = [{}, [], (), 'abc', None, True, b'def']
    test_number = str(random.choice(not_int_list))
    #
    command = (
        'python',
        'task_7_number_sequence/task_7.py',
        '-n',
        f'{test_number}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_error = cli_error.decode()
    #
    error_msg = (
        'usage: task_7.py [-h] [-n NUMBER]\ntask_7.py: error: '
        f'argument -n/--number: {test_number} is not an integer\n'
    )
    #
    assert 2 == exitcode
    assert b'' == cli_out
    assert error_msg == cli_error


def test_number_sequence_cli_n_negative_int(cli_client):
    '''
    Test task_7_number_sequence/task_7.py -n negative int
    '''
    test_number = random.randint(-123456, -1)
    #
    command = (
        'python',
        'task_7_number_sequence/task_7.py',
        '-n',
        f'{test_number}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_error = cli_error.decode()
    #
    error_msg = (
        'usage: task_7.py [-h] [-n NUMBER]\ntask_7.py: error: '
        f'argument -n/--number: {test_number} is not a positive integer\n'
    )
    #
    assert 2 == exitcode
    assert b'' == cli_out
    assert error_msg == cli_error
