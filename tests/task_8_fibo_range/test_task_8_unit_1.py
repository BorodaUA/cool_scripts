import pytest
from task_8_fibo_range.fibo_range import FiboRange


def test_create_fibo_range_with_valid_data():
    '''
    Test create FiboRange instance with valid start_range
    and end_range parameters
    '''
    start_range = 50
    end_range = 200
    #
    fibo_range_instance = FiboRange()
    fibo_range_instance.set_range(start_range, end_range)
    #
    assert start_range == fibo_range_instance.start_range
    assert end_range == fibo_range_instance.end_range


def test_fibo_range_repr_with_valid_data():
    '''
    Test FiboRange instance __repr__ with valid start_range
    and end_range parameters
    '''
    start_range = 50
    end_range = 200
    #
    fibo_range_instance = FiboRange()
    fibo_range_instance.set_range(start_range, end_range)
    #
    expected_result = '55,89,144'
    assert expected_result == fibo_range_instance.__repr__()


def test_create_fibo_range_with_start_range_bigger_end_range():
    '''
    Test create FiboRange instance with valid start_range
    and end_range parameters
    '''
    start_range = 500
    end_range = 200
    #
    with pytest.raises(SystemExit) as err:
        fibo_range_instance = FiboRange()
        fibo_range_instance.set_range(start_range, end_range)
    #
    error_code = '"end_range" must be greater then "start_range"'
    #
    assert error_code == err.value.code
