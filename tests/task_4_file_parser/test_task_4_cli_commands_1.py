import random
import pytest
from .usage_modes_data import MODES_DICT


def task_4_test_file_content(file_obj):
    for i in range(100000):
        file_obj.write(f'This is line {i} Cat and Dog \n')


def test_count_query_appearance_cli_valid_parameters(
    create_txt_test_file, cli_client
        ):
    '''
    Test count query in a txt file via cli
    '''
    my_file_path = 'tests/task_4_file_parser/test_data/test_big_data.txt'
    my_file_dir = 'tests/task_4_file_parser/test_data/'
    #
    query = 'Cat'
    #
    text_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with text_text_file:
        task_4_test_file_content(text_text_file)
    #
    command = (
        'python',
        'task_4_file_parser/task_4.py',
        '-m',
        '1',
        '-f',
        f'{my_file_path}',
        '-q',
        f'{query}'
    )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    expected_result = (
        'Query "Cat" appears in the "test_big_data.txt" file 100000 time(s).\n'
    )
    assert expected_result == cli_out


def test_replace_string_in_file_via_cli_valid_parameters(
    create_txt_test_file, cli_client
        ):
    '''
    Test replace string in a txt file via cli
    '''
    my_file_path = 'tests/task_4_file_parser/test_data/test_big_data.txt'
    my_file_dir = 'tests/task_4_file_parser/test_data/'
    #
    find_string = 'Cat'
    replace_string = 'abc' * random.randint(5, 10)
    #
    text_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with text_text_file:
        task_4_test_file_content(text_text_file)
    #
    command = (
        'python',
        'task_4_file_parser/task_4.py',
        '-m',
        '2',
        '-f',
        f'{my_file_path}',
        '-fs',
        f'{find_string}',
        '-rs',
        f'{replace_string}'
    )
    #
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    #
    expected_result = (
        '"Find string" "Cat" was replaced by "Replace string" '
        f'"{replace_string}" 100000 time(s).\n'
    )
    #
    assert expected_result == cli_out


@pytest.mark.parametrize('usage_modes', MODES_DICT)
def test_count_query_appearance_cli_no_parameters(cli_client, usage_modes):
    '''
    Test count query in a txt file via cli no parameters
    '''
    if usage_modes['mode']:
        command = (
            'python',
            'task_4_file_parser/task_4.py',
            f'{usage_modes["mode"]}',
            f'{usage_modes["value"]}'
        )
    else:
        command = (
                'python',
                'task_4_file_parser/task_4.py',
            )
    cli_out, cli_error, exitcode = cli_client(command)
    cli_out = cli_out.decode()
    expected_result = (
        '\n*** Welcome to the file parser program ***\n'
        "This program have 2 modes:\n"
        'Mode 1: Find and count how many times '
        'a "query" appears in the text file\n'
        'Mode 1 Usage example: \n'
        'python task_4_file_parser/task_4.py -m 1 -f '
        './task_4_file_parser/big_data.txt -q This \n'
        'python task_4_file_parser/task_4.py --mode 1 --file_path '
        './task_4_file_parser/big_data.txt --query This \n'
        '\n'
        'Mode 2: Find and replace "find_string" with "replace_string"'
        'in the text file\n'
        'Mode 2 Usage example: \n'
        'python task_4_file_parser/task_4.py -m 2 -f '
        './task_4_file_parser/big_data.txt '
        '-fs Cat -rs Dog \n'
        'python task_4_file_parser/task_4.py --mode 2 --file_path '
        './task_4_file_parser/big_data.txt '
        '--find_string Cat --replace_string Dog\n\n'
    )
    assert expected_result == cli_out
