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


class EnvelopesAnalyzer:
    """
    An EnvelopesAnalyzer class
    """
    QUIT_MSG = "Quitting..."
    WELCOME_MSG = (
        '*** Welcome to the Envelope Analyzer *** \n'
        'Follow the program instruction to find out '
        'which Envelope can fit inside the other \n'
        'You can quit at any moment by typing command: q'
    )
    CANNOT_FIT_MSG = 'Envelopes can not fit inside each other'
    START_OVER_MSG = (
        "Would you like to start over? \n"
        "Type: y/yes or n/no "
    )

    @classmethod
    def input_start_over_handler(cls, message, error_msg):
        """
        A helper method, that return valid user's input or
        an error message
        """
        while True:
            user_input = input(message)
            if isinstance(user_input, str):
                if user_input.lower() == "q":
                    return False
                if user_input.lower() == 'y' or user_input.lower() == 'yes':
                    return True
                elif user_input.lower() == 'n' or user_input.lower() == 'no':
                    return False
                else:
                    print(error_msg)
                    continue

    @classmethod
    def input_envelope_handler(cls, message, error_msg):
        """
        A helper method, that return valid user's input or
        an error message
        """
        while True:
            user_input = input(message)
            if isinstance(user_input, str):
                if user_input.lower() == "q":
                    return False
            #
            try:
                user_input = float(user_input)
                if user_input <= 0:
                    print(error_msg)
                    continue
                return user_input
            except ValueError:
                print(error_msg)

    def play(self):
        """
        A play method, responsible for a while loop that continuously asking
        user input and showing the result comparison of two envelopes areas.
        """
        while True:
            print(EnvelopesAnalyzer.WELCOME_MSG)
            #
            envelope_1_side_a = EnvelopesAnalyzer.input_envelope_handler(
                message="Please enter Envelope 1 side A: ",
                error_msg='Envelope 1 side A must be a positive integer'
            )
            if envelope_1_side_a is False:
                print(EnvelopesAnalyzer.QUIT_MSG)
                break
            #
            envelope_1_side_b = EnvelopesAnalyzer.input_envelope_handler(
                message="Please enter Envelope 1 side B: ",
                error_msg='Envelope 1 side B must be a positive integer'
            )
            if envelope_1_side_b is False:
                print(EnvelopesAnalyzer.QUIT_MSG)
                break
            #
            envelope_2_side_c = EnvelopesAnalyzer.input_envelope_handler(
                message="Please enter Envelope 2 side C: ",
                error_msg='Envelope 2 side C must be a positive integer'
            )
            if envelope_2_side_c is False:
                print(EnvelopesAnalyzer.QUIT_MSG)
                break
            #
            envelope_2_side_d = EnvelopesAnalyzer.input_envelope_handler(
                message="Please enter Envelope 2 side D: ",
                error_msg='Envelope 2 side D must be a positive integer'
            )
            if envelope_2_side_d is False:
                print(EnvelopesAnalyzer.QUIT_MSG)
                break
            #
            envelope_1 = Envelope(
                side_a=envelope_1_side_a,
                side_b=envelope_1_side_b
            )
            envelope_2 = Envelope(
                side_a=envelope_2_side_c,
                side_b=envelope_2_side_d
            )
            #
            envelope_1_area = envelope_1.envelope_area()
            envelope_2_area = envelope_2.envelope_area()
            #
            if envelope_1.side_a >= envelope_2.side_a:
                if (
                    envelope_1.side_b >= envelope_2.side_b or
                    envelope_1.side_b <= envelope_2.side_a and
                    envelope_1.side_a <= envelope_2.side_b
                        ):
                    print(
                        f'\nEnvelope 1 area is {envelope_1_area}\n'
                        f'Envelope 2 area is {envelope_2_area}\n'
                        'Envelope 2 can fit inside Envelope 1'
                    )
                else:
                    print(EnvelopesAnalyzer.CANNOT_FIT_MSG)
            #
            if envelope_2.side_a >= envelope_1.side_a:
                if (
                    envelope_2.side_b >= envelope_1.side_b or
                    envelope_2.side_b <= envelope_1.side_a and
                    envelope_2.side_a <= envelope_1.side_b
                        ):
                    print(
                        f'\nEnvelope 1 area is {envelope_1_area}\n'
                        f'Envelope 2 area is {envelope_2_area}\n'
                        'Envelope 1 can fit inside Envelope 2'
                    )
                else:
                    print(EnvelopesAnalyzer.CANNOT_FIT_MSG)
            #
            start_over = EnvelopesAnalyzer.input_start_over_handler(
                message=EnvelopesAnalyzer.START_OVER_MSG,
                error_msg='Could not recognize that command, please repeat.'
            )
            if start_over is False:
                print(EnvelopesAnalyzer.QUIT_MSG)
                break


if __name__ == "__main__":
    game = EnvelopesAnalyzer()
    game.play()
