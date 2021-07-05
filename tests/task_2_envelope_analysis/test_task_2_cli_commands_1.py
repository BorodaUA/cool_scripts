import sys
import io
import random
import pytest
from task_2_envelope_analysis.task_2 import EnvelopesAnalyzer


def test_envelope_1_bigger_cli_valid_parameters(monkeypatch, capsys):
    '''
    Test envelope_1 >= envelope_2 valid parameters
    '''
    envelope_1_side_a = str(float(random.randint(20, 30)))
    envelope_1_side_b = str(float(random.randint(20, 30)))
    #
    envelope_2_side_a = str(float(random.randint(1, 19)))
    envelope_2_side_b = str(float(random.randint(1, 19)))
    start_over = 'n'
    #
    input_values = '\n'.join(
        [
            envelope_1_side_a,
            envelope_1_side_b,
            envelope_2_side_a,
            envelope_2_side_b,
            start_over
        ]
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    with pytest.raises(SystemExit):
        env_analyzer = EnvelopesAnalyzer()
        env_analyzer.main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Envelope Analyzer *** \n'
            'Follow the program instruction to find out which '
            'Envelope can fit inside the other \n'
            'You can quit at any moment by typing command: q\n'
            '\nPlease enter Envelope 1 side A: '
            'Please enter Envelope 1 side B: '
            'Please enter Envelope 2 side C: '
            'Please enter Envelope 2 side D: \n'
            'Envelope 1 with sides: '
            f'{envelope_1_side_a} and {envelope_1_side_b}\n'
            'Envelope 2 with sides:  '
            f'{envelope_2_side_a} and {envelope_2_side_b}\n'
            'Envelope 2 can fit inside Envelope 1\n'
            '\nWould you like to start over? \nType: y/yes or n/no '
        )
    assert '' == cli_error
    assert expected_result == cli_out


def test_envelope_2_bigger_cli_valid_parameters(monkeypatch, capsys):
    '''
    Test envelope_2 >= envelope_1 valid parameters
    '''
    envelope_1_side_a = str(float(random.randint(1, 19)))
    envelope_1_side_b = str(float(random.randint(1, 19)))
    #
    envelope_2_side_a = str(float(random.randint(20, 30)))
    envelope_2_side_b = str(float(random.randint(20, 30)))
    start_over = 'n'
    #
    input_values = '\n'.join(
        [
            envelope_1_side_a,
            envelope_1_side_b,
            envelope_2_side_a,
            envelope_2_side_b,
            start_over
        ]
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    with pytest.raises(SystemExit):
        env_analyzer = EnvelopesAnalyzer()
        env_analyzer.main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Envelope Analyzer *** \n'
            'Follow the program instruction to find out which '
            'Envelope can fit inside the other \n'
            'You can quit at any moment by typing command: q\n'
            '\nPlease enter Envelope 1 side A: '
            'Please enter Envelope 1 side B: '
            'Please enter Envelope 2 side C: '
            'Please enter Envelope 2 side D: \n'
            'Envelope 1 with sides: '
            f'{envelope_1_side_a} and {envelope_1_side_b}\n'
            'Envelope 2 with sides:  '
            f'{envelope_2_side_a} and {envelope_2_side_b}\n'
            'Envelope 1 can fit inside Envelope 2\n'
            '\nWould you like to start over? \nType: y/yes or n/no '
        )
    assert '' == cli_error
    assert expected_result == cli_out


def test_envelopes_cannot_fit_cli_valid_parameters(monkeypatch, capsys):
    '''
    Test envelopes cannot fit inside each other, valid parameters
    '''
    envelope_1_side_a = str(float(random.randint(10, 20)))
    envelope_1_side_b = str(float(random.randint(21, 30)))
    #
    envelope_2_side_a = str(float(random.randint(1, 10)))
    envelope_2_side_b = str(float(random.randint(40, 50)))
    start_over = 'n'
    #
    input_values = '\n'.join(
        [
            envelope_1_side_a,
            envelope_1_side_b,
            envelope_2_side_a,
            envelope_2_side_b,
            start_over
        ]
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    with pytest.raises(SystemExit):
        env_analyzer = EnvelopesAnalyzer()
        env_analyzer.main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Envelope Analyzer *** \n'
            'Follow the program instruction to find out which '
            'Envelope can fit inside the other \n'
            'You can quit at any moment by typing command: q\n'
            '\nPlease enter Envelope 1 side A: '
            'Please enter Envelope 1 side B: '
            'Please enter Envelope 2 side C: '
            'Please enter Envelope 2 side D: '
            'Envelopes can not fit inside each other'
            '\nWould you like to start over? \nType: y/yes or n/no '
        )
    assert '' == cli_error
    assert expected_result == cli_out


def test_quit_in_start_over_handler_cli(monkeypatch, capsys):
    '''
    Test "q" quit in start_over handler
    envelopes with valid parameters
    '''
    envelope_1_side_a = str(float(random.randint(20, 30)))
    envelope_1_side_b = str(float(random.randint(20, 30)))
    #
    envelope_2_side_a = str(float(random.randint(1, 19)))
    envelope_2_side_b = str(float(random.randint(1, 19)))
    start_over = 'q'
    #
    input_values = '\n'.join(
        [
            envelope_1_side_a,
            envelope_1_side_b,
            envelope_2_side_a,
            envelope_2_side_b,
            start_over
        ]
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    with pytest.raises(SystemExit):
        env_analyzer = EnvelopesAnalyzer()
        env_analyzer.main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Envelope Analyzer *** \n'
            'Follow the program instruction to find out which '
            'Envelope can fit inside the other \n'
            'You can quit at any moment by typing command: q\n'
            '\nPlease enter Envelope 1 side A: '
            'Please enter Envelope 1 side B: '
            'Please enter Envelope 2 side C: '
            'Please enter Envelope 2 side D: \n'
            'Envelope 1 with sides: '
            f'{envelope_1_side_a} and {envelope_1_side_b}\n'
            'Envelope 2 with sides:  '
            f'{envelope_2_side_a} and {envelope_2_side_b}\n'
            'Envelope 2 can fit inside Envelope 1\n'
            '\nWould you like to start over? \nType: y/yes or n/no '
        )
    assert '' == cli_error
    assert expected_result == cli_out


def test_quit_in_input_envelope_handler_cli(monkeypatch, capsys):
    '''
    Test "q" quit in input envelope handler
    envelopes with valid parameters
    '''
    envelope_1_side_a = str(float(random.randint(20, 30)))
    envelope_1_side_b = str(float(random.randint(20, 30)))
    #
    envelope_2_side_a = str(float(random.randint(1, 19)))
    envelope_2_side_b = str(float(random.randint(1, 19)))
    start_over = 'n'
    quit_command = 'q'
    #
    input_values = '\n'.join(
        [
            envelope_1_side_a,
            quit_command,
            envelope_1_side_b,
            envelope_2_side_a,
            envelope_2_side_b,
            start_over
        ]
    )
    #
    monkeypatch.setattr(sys, 'stdin', io.StringIO(input_values))
    #
    with pytest.raises(SystemExit):
        env_analyzer = EnvelopesAnalyzer()
        env_analyzer.main()
    #
    cli_out, cli_error = capsys.readouterr()
    #
    expected_result = (
            '\n*** Welcome to the Envelope Analyzer *** \n'
            'Follow the program instruction to find out which '
            'Envelope can fit inside the other \n'
            'You can quit at any moment by typing command: q\n'
            '\nPlease enter Envelope 1 side A: '
            'Please enter Envelope 1 side B: '
        )
    assert '' == cli_error
    assert expected_result == cli_out
