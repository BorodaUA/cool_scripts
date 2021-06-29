def lucky_tickets_file_content(file_obj):
    '''
    Write content of the test tickets file
    '''
    for i in range(1, 1000000):
        i = i / 100000
        i = f"{i:.5f}".replace('.', '')
        file_obj.write(f'{i}\n')


def test_count_tickets_moscow_method_cli_valid_parameters(
    create_txt_test_file, cli_client
        ):
    '''
    Test count lucky tickets by moscow method in a txt file via cli
    '''
    my_file_path = 'tests/task_6_lucky_tickets/test_data/tickets.txt'
    my_file_name = my_file_path.split('/')[-1]
    my_file_dir = 'tests/task_6_lucky_tickets/test_data/'
    count_type = 'Moscow'
    #
    test_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with test_text_file:
        lucky_tickets_file_content(test_text_file)
    #
    command = (
        'python',
        'task_6_lucky_tickets/task_6.py',
        '-f',
        f'{my_file_path}',
        '-ct',
        f'{count_type}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    expected_result = (
        f'File "{my_file_name}" was counted by "{count_type}" '
        'method and it has 55251 lucky tickets\n'
    )
    assert expected_result == cli_out


def test_count_tickets_piter_method_cli_valid_parameters(
    create_txt_test_file, cli_client
        ):
    '''
    Test count lucky tickets by piter method in a txt file via cli
    '''
    my_file_path = 'tests/task_6_lucky_tickets/test_data/tickets.txt'
    my_file_name = my_file_path.split('/')[-1]
    my_file_dir = 'tests/task_6_lucky_tickets/test_data/'
    count_type = 'Piter'
    #
    test_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with test_text_file:
        lucky_tickets_file_content(test_text_file)
    #
    command = (
        'python',
        'task_6_lucky_tickets/task_6.py',
        '-f',
        f'{my_file_path}',
        '-ct',
        f'{count_type}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    expected_result = (
        f'File "{my_file_name}" was counted by "{count_type}" '
        'method and it has 25080 lucky tickets\n'
    )
    assert expected_result == cli_out
