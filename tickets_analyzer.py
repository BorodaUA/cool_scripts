from text_file_reader import TextFileReader


class TicketsFileAnalyzer(TextFileReader):
    '''
    A Tickets file analyzer
    '''

    def __init__(self, file, count_type):
        '''
        Initialization of the tickets file
        '''
        self.file = file
        self.count_type = count_type

    @property
    def lucky_tickets(self):
        '''
        Return how many lucky tickets is in a text file
        '''
        LUCKY_TICKETS_COUNT = 0
        try:
            with open(self.file.file_path, 'r') as f:
                #
                for chunk_list in TicketsFileAnalyzer.generate_list_of_strings(
                    f
                ):
                    #
                    for line in chunk_list:
                        #
                        valid_ticket_number = (
                            TicketsFileAnalyzer.
                            ticket_number_validator(
                                ticket_number=line
                            )
                        )
                        if valid_ticket_number is False:
                            continue
                        if self.count_type == "Moskow":
                            is_lucky = TicketsFileAnalyzer.count_moscow_type(
                                ticket_number=valid_ticket_number
                            )
                            if is_lucky is True:
                                LUCKY_TICKETS_COUNT += 1
                        if self.count_type == "Piter":
                            is_lucky = TicketsFileAnalyzer.count_piter_type(
                                ticket_number=valid_ticket_number
                            )
                            if is_lucky is True:
                                LUCKY_TICKETS_COUNT += 1
        #
        except PermissionError as e:
            return str(e)
        except FileNotFoundError as e:
            return str(e)
        return LUCKY_TICKETS_COUNT

    @classmethod
    def ticket_number_validator(cls, ticket_number):
        '''
        Check if ticket number is an integer, and it has
        6 digits length
        '''
        #
        ticket_number = ticket_number.strip()
        #
        if len(ticket_number) != 6:
            return False
        #
        try:
            int(ticket_number)
        except ValueError:
            return False
        #
        return ticket_number

    @staticmethod
    def count_moscow_type(ticket_number):
        '''
        Return True if sum of first 3 digits
        equals sum of last 3 digits of a ticket
        '''
        first_part = sum(int(x) for x in ticket_number[:3])
        second_part = sum(int(x) for x in ticket_number[3:])
        #
        if first_part == second_part:
            return True
        return False

    @staticmethod
    def count_piter_type(ticket_number):
        '''
        Return True if sum of even digits
        equals sum of odd digits of a ticket
        '''
        #
        even = []
        odd = []
        #
        for digit in ticket_number:
            if int(digit) % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)
        #
        even_sum = sum(int(x) for x in even)
        odd_sum = sum(int(x) for x in odd)
        #
        if even_sum == odd_sum:
            return True
        return False
