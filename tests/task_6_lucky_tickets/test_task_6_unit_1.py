import pytest
from task_6_lucky_tickets.tickets_analyzer import TicketsFileAnalyzer
from task_6_lucky_tickets.txt_file import TxtFile


def lucky_tickets_file_content(file_obj):
    '''
    Write content of the test tickets file
    '''
    for i in range(1, 1000000):
        i = i / 100000
        i = f"{i:.5f}".replace('.', '')
        file_obj.write(f'{i}\n')


def test_create_instance_with_count_type_moscow(create_txt_test_file):
    '''
    Test create instances of a TxtFile and TicketsFileAnalyzer
    with count_type "Moscow" valid data
    '''
    my_file_path = 'tests/task_6_lucky_tickets/test_data/tickets.txt'
    my_file_dir = 'tests/task_6_lucky_tickets/test_data/'
    #
    count_type = 'Moscow'
    lucky_tickets = 55251
    #
    test_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with test_text_file:
        lucky_tickets_file_content(test_text_file)
    #
    test_txt_file_instance = TxtFile()
    test_txt_file_instance.set_file_path(my_file_path)
    tickets_file_instace = TicketsFileAnalyzer(
        test_txt_file_instance,
        count_type
    )
    assert my_file_path == test_txt_file_instance.file_path
    assert lucky_tickets == tickets_file_instace.lucky_tickets


def test_create_instance_with_count_type_piter(create_txt_test_file):
    '''
    Test create instances of a TxtFile and TicketsFileAnalyzer
    with count_type "Piter" valid data
    '''
    my_file_path = 'tests/task_6_lucky_tickets/test_data/tickets.txt'
    my_file_dir = 'tests/task_6_lucky_tickets/test_data/'
    #
    count_type = 'Piter'
    lucky_tickets = 25080
    #
    test_text_file = create_txt_test_file(my_file_dir, my_file_path)
    with test_text_file:
        lucky_tickets_file_content(test_text_file)
    #
    test_txt_file_instance = TxtFile()
    test_txt_file_instance.set_file_path(my_file_path)
    tickets_file_instace = TicketsFileAnalyzer(
        test_txt_file_instance,
        count_type
    )
    assert my_file_path == test_txt_file_instance.file_path
    assert lucky_tickets == tickets_file_instace.lucky_tickets


def test_create_instance_file_not_exists(create_txt_test_file):
    '''
    Test create instances of a TxtFile and TicketsFileAnalyzer
    with file not exist
    '''
    my_file_path = 'tests/task_6_lucky_tickets/test_data/tickets.txt'
    # my_file_dir = 'tests/task_6_lucky_tickets/test_data/'
    # #
    # count_type = 'Piter'
    # lucky_tickets = 25080
    #
    error_msg = 'No such file or directory'
    error_code = 2
    #
    with pytest.raises(SystemExit) as err:
        test_txt_file_instance = TxtFile()
        test_txt_file_instance.set_file_path(my_file_path)
    #
    assert error_code == err.value.code.errno
    assert error_msg == err.value.code.strerror
