import operator
import sys


class Envelope:
    """
    An Envelope class
    """
    def __init__(self, side_a, side_b):
        """
        Initialization of the Envelope class with 2 parameters
        side_a: int
        side_b: int
        """
        self.side_a = side_a
        self.side_b = side_b

    def envelope_area(self):
        """
        Return area of an envelope by multiplying sides
        of an envelope
        """
        return self.side_a * self.side_b

    @staticmethod
    def _comparison(self, other, sign):
        '''
        Equality check for envelope instances
        for > >= and <= < operators
        '''
        #
        if operator.gt.__name__ == sign:
            the_operator = operator.gt
        #
        if operator.ge.__name__ == sign:
            the_operator = operator.ge
        #
        if (
            the_operator(self.side_a, other.side_a) and
            the_operator(self.side_b, other.side_b) or
            the_operator(self.side_b, other.side_a) and
            the_operator(self.side_a, other.side_b)
                ):
            return True
        return False

    @staticmethod
    def _equality(self, other, sign):
        '''
        Equality check for envelope instances
        for == and != operators
        '''
        if operator.eq.__name__ == sign:
            the_operator = operator.eq
        #
        if operator.ne.__name__ == sign:
            the_operator = operator.ne
        if (
            the_operator(self.side_a, other.side_a) and
            the_operator(self.side_b, other.side_b)
                ):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Custom ">" "greater then" implimentation for envelope instances
        """
        if Envelope._comparison(self, other, 'gt'):
            return True
        return False

    def __ge__(self, other):
        """
        Custom ">=" "greater or equal then"
        implimentation for envelope instances
        """
        if Envelope._comparison(self, other, 'ge'):
            return True
        return False

    def __eq__(self, other):
        '''
        Custom "==" equal implementation for envelope
        instances
        '''
        if Envelope._equality(self, other, 'eq'):
            return True
        return False

    def __ne__(self, other):
        '''
        Custom "!=" not equal implementation for envelope
        instances
        '''
        if Envelope._equality(self, other, 'ne'):
            return True
        return False


class EnvelopesAnalyzer:
    """
    An EnvelopesAnalyzer class
    """
    QUIT_MSG = "Quitting..."
    WELCOME_MSG = (
        '\n*** Welcome to the Envelope Analyzer *** \n'
        'Follow the program instruction to find out '
        'which Envelope can fit inside the other \n'
        'You can quit at any moment by typing command: q\n'
    )
    CANNOT_FIT_MSG = 'Envelopes can not fit inside each other'
    START_OVER_MSG = (
        "Would you like to start over? \n"
        "Type: y/yes or n/no "
    )
    START_OVER_ERR_MSG = 'Could not recognize that command, please repeat.'
    ENVELOPES_SIDES_DICT = [
        {
            'env_msg': 'Please enter Envelope 1 side A: ',
            'env_err_msg': (
                'Envelope 1 side A '
                'must be a positive integer'
            ),
        },
        {
            'env_msg': 'Please enter Envelope 1 side B: ',
            'env_err_msg': (
                'Envelope 1 side B '
                'must be a positive integer'
            ),
        },
        {
            'env_msg': 'Please enter Envelope 2 side C: ',
            'env_err_msg': (
                'Envelope 2 side C '
                'must be a positive integer'
            ),
        },
        {
            'env_msg': 'Please enter Envelope 2 side D: ',
            'env_err_msg': (
                'Envelope 2 side D '
                'must be a positive integer'
            ),
        },
    ]

    @staticmethod
    def input_start_over_handler(message, error_msg):
        """
        A helper method, that return valid user's input
        """
        while True:
            user_input = input(message)
            if isinstance(user_input, str):
                if user_input.lower() == "q":
                    sys.exit(EnvelopesAnalyzer.QUIT_MSG)
                if user_input.lower() == 'y' or user_input.lower() == 'yes':
                    return True
                elif user_input.lower() == 'n' or user_input.lower() == 'no':
                    sys.exit(EnvelopesAnalyzer.QUIT_MSG)
                else:
                    print(error_msg)
                    continue

    @staticmethod
    def input_envelope_handler(envelopes_dict):
        """
        A helper method, that return valid user's input
        """
        result_list = []
        for env in envelopes_dict:
            #
            while len(result_list) != 4:
                user_input = input(env['env_msg'])
                if isinstance(user_input, str):
                    if user_input.lower() == "q":
                        sys.exit(EnvelopesAnalyzer.QUIT_MSG)
                #
                try:
                    user_input = float(user_input)
                    if user_input <= 0:
                        print(env['env_err_msg'])
                        continue
                    result_list.append(user_input)
                    break
                except ValueError:
                    print(env['env_err_msg'])
        #
        return result_list

    def main(self):
        """
        A main method, responsible for a while loop that continuously asking
        user input and showing the result comparison of two envelopes.
        """
        while True:
            print(EnvelopesAnalyzer.WELCOME_MSG)
            #
            envelopes_sides = EnvelopesAnalyzer.input_envelope_handler(
                EnvelopesAnalyzer.ENVELOPES_SIDES_DICT
            )
            #
            envelope_1 = Envelope(
                side_a=envelopes_sides[0],
                side_b=envelopes_sides[1]
            )
            #
            envelope_2 = Envelope(
                side_a=envelopes_sides[2],
                side_b=envelopes_sides[3]
            )
            # #
            if envelope_1 >= envelope_2:
                print(
                        f'\nEnvelope 1 with sides: {envelope_1.side_a} and '
                        f'{envelope_1.side_b}\n'
                        f'Envelope 2 with sides:  {envelope_2.side_a} and '
                        f'{envelope_2.side_b}\n'
                        'Envelope 2 can fit inside Envelope 1\n'
                    )
            elif envelope_2 >= envelope_1:
                print(
                        f'\nEnvelope 1 with sides: {envelope_1.side_a} and '
                        f'{envelope_1.side_b}\n'
                        f'Envelope 2 with sides:  {envelope_2.side_a} and '
                        f'{envelope_2.side_b}\n'
                        'Envelope 1 can fit inside Envelope 2\n'
                    )
            else:
                print(EnvelopesAnalyzer.CANNOT_FIT_MSG)
            #
            EnvelopesAnalyzer.input_start_over_handler(
                message=EnvelopesAnalyzer.START_OVER_MSG,
                error_msg=EnvelopesAnalyzer.START_OVER_ERR_MSG
            )


if __name__ == "__main__":
    game = EnvelopesAnalyzer()
    game.main()
