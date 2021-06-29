from task_5_numbers_convertor.number_2_words import NumbersToWords


def test_create_instance_with_valid_data():
    '''
    Test create an instance of NumbersToWords
    with valid data
    '''
    input_number = 123456789
    num_instance = NumbersToWords(input_number)
    assert input_number == num_instance.number


def test_instance_repr_with_valid_data():
    '''
    Test create an instance of NumbersToWords
    with valid data, and check its __repr__
    '''
    input_number = 123456789
    num_instance = NumbersToWords(input_number)
    #
    expected_result = (
        'сто двадцать три миллиона четыреста пятьдесят шесть тысячь '
        'семьсот восемьдесят девять'
    )
    #
    assert expected_result == num_instance.__repr__()


def test_instance_ranks_with_valid_data():
    '''
    Test create an instance of NumbersToWords
    with valid data, and check its ranks property
    '''
    input_number = 123456789
    num_instance = NumbersToWords(input_number)
    #
    expected_result = ['123', '456', '789']
    #
    assert expected_result == num_instance.ranks
