def test_fibo_range_cli_valid_parameters(cli_client):
    '''
    Test task_8_fibo_range/task_8.py valid parameters
    '''
    start_range = 50
    end_range = 200
    #
    command = (
        'python',
        'task_8_fibo_range/task_8.py',
        '-sr',
        f'{start_range}',
        '-er',
        f'{end_range}'
    )
    #
    cli_out, cli_error, exitcode = cli_client(command)
    cli_error = cli_error.decode()
    cli_out = cli_out.decode().strip()
    #
    expected_result = '55,89,144'
    #
    assert 0 == exitcode
    assert '' == cli_error
    assert expected_result == cli_out


def test_fibo_range_cli_no_parameters(cli_client):
    '''
    Test task_8_fibo_range/task_8.py no parameters
    '''
    command = ('python', 'task_8_fibo_range/task_8.py')
    cli_out, cli_error, exitcode = cli_client(command)
    cli_error = cli_error.decode()
    #
    HELP_MSG = (
        "\n*** Welcome to the Fibonacci numbers for the range ***\n"
        "This program will print all fibonacci numbers, in the range of "
        "numbers specified by the user. \nUsage example: \n"
        "python task_8_fibo_range/task_8.py -sr 50 -er 200 \n"
        "python task_8_fibo_range/task_8.py "
        "--start_range 50 --end_range 200 \n\n"
    )
    assert 1 == exitcode
    assert HELP_MSG == cli_error
    assert b'' == cli_out


def test_fibo_range_cli_start_range_bigger_end_range(cli_client):
    '''
    Test task_8_fibo_range/task_8.py start_range bigger than
    end_range

    '''
    start_range = 300
    end_range = 200
    command = (
        'python',
        'task_8_fibo_range/task_8.py',
        '-sr',
        f'{start_range}',
        '-er',
        f'{end_range}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_error = cli_error.decode()
    #
    error_msg = (
        '"end_range" must be greater then "start_range"\n'
    )
    assert 1 == exitcode
    assert error_msg == cli_error
    assert b'' == cli_out
