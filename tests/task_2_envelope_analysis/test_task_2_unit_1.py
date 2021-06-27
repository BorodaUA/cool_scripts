import random
from task_2_envelope_analysis.task_2 import Envelope


def test_create_envelope_valid_data():
    '''
    Test create an Envelope instance with valid data
    '''
    side_a = random.randint(1, 25)
    side_b = random.randint(1, 25)
    #
    envelope_1 = Envelope(side_a, side_b)
    assert side_a == envelope_1.side_a
    assert side_b == envelope_1.side_b


def test_envelope_1_bigger_valid_data():
    '''
    Test envelope_1 bigger_equal than envelope_2 valid data
    '''
    envelope_1_side_a = float(random.randint(10, 20))
    envelope_1_side_b = float(random.randint(10, 20))
    #
    envelope_2_side_a = float(random.randint(1, 9))
    envelope_2_side_b = float(random.randint(1, 9))
    #
    envelope_1 = Envelope(envelope_1_side_a, envelope_1_side_b)
    envelope_2 = Envelope(envelope_2_side_a, envelope_2_side_b)
    assert envelope_1 >= envelope_2


def test_envelope_2_bigger_valid_data():
    '''
    Test envelope_2 bigger_equal than envelope_1 valid data
    '''
    envelope_1_side_a = float(random.randint(1, 9))
    envelope_1_side_b = float(random.randint(1, 9))
    #
    envelope_2_side_a = float(random.randint(10, 30))
    envelope_2_side_b = float(random.randint(10, 30))
    #
    envelope_1 = Envelope(envelope_1_side_a, envelope_1_side_b)
    envelope_2 = Envelope(envelope_2_side_a, envelope_2_side_b)
    assert envelope_2 >= envelope_1
