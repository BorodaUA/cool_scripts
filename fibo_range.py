import sys


class FiboRange:
    '''
    A FiboRange class
    '''
    def __init__(self, start_range=None, end_range=None):
        '''
        Initialization of the FiboRance instance
        '''
        self.start_range = start_range
        self.end_range = end_range

    def set_range(self, start_range, end_range):
        '''
        A set method for the FiboRange
        '''
        if end_range <= start_range:
            sys.exit('"end_range" must be greater then "start_range"')
        #
        self.start_range = start_range
        self.end_range = end_range

    def __repr__(self):
        '''
        Representation of the fibonacci sequence in given range
        '''
        return self.fibo_range

    @property
    def fibo_range(self):
        '''
        Return string of fibonacci sequence in given range
        '''
        a = 0
        b = 1
        #
        result = []
        #
        while a <= self.end_range:
            result.append(a)
            a, b = b, a+b
        #
        start_index = FiboRange.find_index_of_closest_int(
            result,
            self.start_range
        )
        #
        result = [str(i) for i in result[start_index:]]
        #
        return ','.join(result)

    @staticmethod
    def find_index_of_closest_int(numbers_lst, value):
        '''
        Return index of item closest to the value
        '''
        min_difference = value
        min_difference_index = 0
        #
        for num in enumerate(numbers_lst):
            difference = abs(value - num[1])
            #
            if min_difference >= difference:
                min_difference = difference
                min_difference_index = num[0]
        #
        return min_difference_index
