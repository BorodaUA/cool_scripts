import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from num_to_str_storage import ( # noqa
    SINGLE_DIGITS,
    SINGLE_DIGITS_FEMININE,
    DOUBLE_DIGITS,
    DOUBLE_DIGITS_DECS,
    TRIPLE_DIGITS,
    THOUSAND_ENDINGS,
    MILLION_ENDINGS
)


class NumbersToWords:
    '''
    Number2Words class
    '''

    def __init__(self, number):
        self.number = number

    @property
    def ranks(self):
        '''
        Return list of ranks of the number
        123456789
        >>>['123', '456', '789']
        '''
        return f'{self.number:,}'.split(',')

    def flatten(self, incoming_tuple):
        '''
        Unpacking tuples helper
        '''
        if not isinstance(incoming_tuple, tuple):
            return incoming_tuple
        #
        if incoming_tuple == ():
            return incoming_tuple
        #
        if isinstance(incoming_tuple[0], tuple):
            return (
                self.flatten(incoming_tuple[0]) +
                self.flatten(incoming_tuple[1:])
                )
        return incoming_tuple[:1] + self.flatten(incoming_tuple[1:])

    def __repr__(self):
        '''
        Representation of numbers in text
        '''
        ranks = self.ranks
        #
        tuple_of_lists = self.get_words_of_numbers(ranks)
        tuple_of_lists = self.flatten(tuple_of_lists)
        #
        result_list = []
        for i in tuple_of_lists:
            temp_str = ''.join(i)
            result_list.append(temp_str)
        #
        return ' '.join(result_list)

    def get_words_of_numbers(self, ranks):
        '''
        Return tuple of words
        '''
        list_of_ranks = ranks
        result_words_list = []
        #
        if len(list_of_ranks) == 1:
            first_rank = self.create_list_of_numbers(int(list_of_ranks[0]))
            first_rank = self.flatten(first_rank)
            #
            first_rank_words = self.first_rank_convertor(first_rank)
            #
            result_words_list.append(first_rank_words)
            #
            return result_words_list
        #
        if len(list_of_ranks) == 2:
            second_rank = self.create_list_of_numbers(int(list_of_ranks[0]))
            second_rank = self.flatten(second_rank)
            #
            second_rank_words = self.second_rank_convertor(second_rank)
            result_words_list.append(second_rank_words)
            #
            if list_of_ranks[1] != '000':
                return result_words_list, self.get_words_of_numbers(
                    list_of_ranks[-1:]
                )
            #
            return result_words_list
        if len(list_of_ranks) == 3:
            third_rank = self.create_list_of_numbers(int(list_of_ranks[0]))
            third_rank = self.flatten(third_rank)
            #
            third_rank_words = self.third_rank_convertor(third_rank)
            result_words_list.append(third_rank_words)
            #
            if list_of_ranks[1] != '000':
                return result_words_list, self.get_words_of_numbers(
                    list_of_ranks[1:]
                )
            #
            if list_of_ranks[2] != '000':
                return result_words_list, self.get_words_of_numbers(
                    list_of_ranks[-1:]
                )
            #
            return result_words_list

    def create_list_of_numbers(self, numbers):
        '''
        Return tuple of numbers
        '''
        number_lenght = int(len(str(numbers)))
        divider = int('1' + '0' * (number_lenght - 1))
        #
        last_digits = numbers % divider
        first_digits = numbers - last_digits
        #
        try:
            DOUBLE_DIGITS[numbers]
            return numbers,
        except KeyError:
            pass
        #
        if last_digits != 0:
            return first_digits, self.create_list_of_numbers(last_digits)
        return first_digits,

    def first_rank_convertor(self, numbers):
        '''
        A helper method that converts numbers
        from 1 to 999 to russian words
        '''
        words = []
        for num in numbers:
            #
            if len(str(num)) == 1:
                words.append(SINGLE_DIGITS[num])
            #
            if len(str(num)) == 2:
                try:
                    words.append(DOUBLE_DIGITS[num])
                except KeyError:
                    words.append(DOUBLE_DIGITS_DECS[num])
            #
            if len(str(num)) == 3:
                words.append(TRIPLE_DIGITS[num])
        #
        return ' '.join(words)

    def second_rank_convertor(self, numbers):
        '''
        A helper method that converts numbers
        from 1000 to 999 999 to russian words
        '''
        words = []
        try:
            ending = THOUSAND_ENDINGS[numbers[-1]]
        except KeyError:
            ending = "тысячь"
        #
        for num in numbers:
            #
            if len(str(num)) == 1:
                #
                if num in [1]:
                    words.append(
                        f'{SINGLE_DIGITS_FEMININE[num]}'
                    )
                    continue
                elif num in [2, 3, 4]:
                    words.append(
                        f'{SINGLE_DIGITS_FEMININE[num]}'
                    )
                    continue
                else:
                    words.append(f'{SINGLE_DIGITS[num]}')
            #
            if len(str(num)) == 2:
                #
                try:
                    words.append(
                        f'{DOUBLE_DIGITS[num]}'

                    )
                except KeyError:
                    words.append(
                        f'{DOUBLE_DIGITS_DECS[num]}'
                    )
            #
            if len(str(num)) == 3:
                #
                words.append(
                    f'{TRIPLE_DIGITS[num]}'
                )
        #
        words.append(ending)
        #
        return ' '.join(words)

    def third_rank_convertor(self, numbers):
        '''
        A helper method that converts numbers
        from 1 000 000 to 999 999 999 to russian words
        '''
        words = []
        #
        try:
            ending = MILLION_ENDINGS[numbers[-1]]
        except KeyError:
            ending = "миллионов"
        #
        for num in numbers:
            #
            if len(str(num)) == 1:
                words.append(
                    f'{SINGLE_DIGITS[num]}'
                )
            #
            if len(str(num)) == 2:
                try:
                    words.append(
                        f'{DOUBLE_DIGITS[num]}'
                    )
                except KeyError:
                    words.append(
                        f'{DOUBLE_DIGITS_DECS[num]}'
                    )
            #
            if len(str(num)) == 3:
                words.append(
                    f'{TRIPLE_DIGITS[num]}'
                )
        #
        words.append(ending)
        #
        return ' '.join(words)
