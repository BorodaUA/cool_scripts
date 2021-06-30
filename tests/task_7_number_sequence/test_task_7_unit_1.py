import random
from task_7_number_sequence.sequence_number import SequenceNumber


def test_create_number_sequence_valid_data():
    '''
    Test create the SequenceNumber instance with
    valid data
    '''
    test_number = random.randint(1, 100000)
    number_with_sequence = SequenceNumber(test_number)
    #
    assert test_number == number_with_sequence.number


def test_square_last_number_sequence_le_then_number():
    '''
    Test square of last number of number the sequence
    <= then the number
    '''
    test_number = random.randint(1, 100000)
    number_with_sequence = SequenceNumber(test_number)
    #
    last_number_square = int(
        number_with_sequence.numbers_below.split(',')[-1].strip()
    ) ** 2
    assert test_number >= last_number_square
