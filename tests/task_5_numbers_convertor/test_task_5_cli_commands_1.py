import sys
import io
import pytest
import random
from task_5_numbers_convertor.task_5 import main
from .numbers_2_words_data import NUMBERS_WITH_WORDS


@pytest.mark.parametrize(
    'input_number',
    NUMBERS_WITH_WORDS
)
def test_input_number_is_valid_int(capsys, monkeypatch, input_number):
    '''
    Test numbers convertor with valid int
    '''
    #
    monkeypatch.setattr(
        sys,
        'stdin',
        io.StringIO(input_number['number'])
    )
    #
    main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
        '***Welcome to the Numbers 2 Words converter *** \n'
        'Please type in number(s), that will be converted to word(s): '
        f'{input_number["words"]}\n'

    )
    #
    assert '' == cli_error
    assert expected_result == cli_out


def test_input_number_is_zero(capsys, monkeypatch):
    '''
    Test numbers convertor with valid int
    '''
    input_number = '0'
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_number))
    #
    with pytest.raises(SystemExit):
        main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
        '***Welcome to the Numbers 2 Words converter *** \n'
        'Please type in number(s), that will be converted to word(s): '
        'ноль\n'
    )
    #
    assert '' == cli_error
    assert expected_result == cli_out


def test_input_number_above_999_999_999(capsys, monkeypatch):
    '''
    Test numbers convertor with valid int
    '''
    input_number = str(random.randint(1234567890, 9876543211))
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_number))
    #
    with pytest.raises(SystemExit):
        main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
        '***Welcome to the Numbers 2 Words converter *** \n'
        'Please type in number(s), that will be converted to word(s): '
        'Handling numbers above 999 999 999 not implemented yet.\n'
    )
    #
    assert '' == cli_error
    assert expected_result == cli_out


def test_input_number_not_int(capsys, monkeypatch):
    '''
    Test numbers convertor with valid int
    '''
    not_int_list = [{}, [], (), 'abc', None, True, b'def']
    input_number = str(random.choice(not_int_list))
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_number))
    #
    main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
        '***Welcome to the Numbers 2 Words converter *** \n'
        'Please type in number(s), that will be converted to word(s): '
        'Please enter a valid number\n'
    )
    #
    assert '' == cli_error
    assert expected_result == cli_out


def test_input_number_negative_int(capsys, monkeypatch):
    '''
    Test numbers convertor with negative int
    '''
    input_number = str(random.randint(-12345, -1))
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_number))
    #
    with pytest.raises(SystemExit):
        main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
        '***Welcome to the Numbers 2 Words converter *** \n'
        'Please type in number(s), that will be converted to word(s): '
        'Please enter a number greater then zero\n'
    )
    #
    assert '' == cli_error
    assert expected_result == cli_out
