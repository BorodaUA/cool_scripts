from task_4_file_parser.text_file import TxtFile
import random


def task_4_test_file_content(file_obj):
    for i in range(100000):
        file_obj.write(f'This is line {i} Cat and Dog \n')


def test_count_query_appearance_in_the_file(create_txt_test_file):
    '''
    Test query appearance in the test txt file
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
    test_file_instance = TxtFile()
    test_file_instance.set_file_path(my_file_path)
    #
    appearance_count = test_file_instance.count_query_apperance_in_file(query)
    #
    assert 100000 == appearance_count


def test_replacement_string_in_the_file(create_txt_test_file):
    '''
    Test replacement "find_string" with "replace_string"
    in the test txt file
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
    test_file_instance = TxtFile()
    test_file_instance.set_file_path(my_file_path)
    #
    replacement_count = test_file_instance.find_and_replace_str_in_file(
        find_string,
        replace_string
    )
    #
    assert 100000 == replacement_count
