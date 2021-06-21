class SequenceNumber:
    '''
    The SequenceNumber class
    '''

    def __init__(self, number):
        '''
        Initialization of the instance
        '''
        self.number = number

    @property
    def numbers_below(self):
        '''
        Return string of numbers whose squares below the self.number
        '''
        start_number = 1
        result_list = []
        #
        while True:
            square_number = start_number * start_number
            #
            if square_number <= self.number:
                result_list.append(str(start_number))
                start_number += 1
            else:
                break
        #
        return ','.join(result_list)
