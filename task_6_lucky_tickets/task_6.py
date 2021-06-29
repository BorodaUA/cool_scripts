import argparse
from argparse import RawTextHelpFormatter
import sys
from txt_file import TxtFile
from tickets_analyzer import TicketsFileAnalyzer

FILE_NAME = __file__.split('/')[-1]

WELCOME_MSG = (
    '\n***Welcome to the Lucky Tickets counter*** \n'
    'This program will help you count how many "lucky tickets" '
    'is in a text file\n'
    '\nUsage Examples: \n'
    'Count type "Moskow": \n'
    f'python task_6_lucky_tickets/{FILE_NAME} '
    '-f ./task_6_lucky_tickets/tickets.txt -ct Moscow \n'
    f'python task_6_lucky_tickets/{FILE_NAME} --file_path '
    './task_6_lucky_tickets/tickets.txt --count_type Moscow\n'
    '\nCount type "Piter": \n'
    f'python task_6_lucky_tickets/{FILE_NAME} '
    '-f ./task_6_lucky_tickets/tickets.txt -ct Piter\n'
    f'python task_6_lucky_tickets/{FILE_NAME} '
    '--file_path ./task_6_lucky_tickets/tickets.txt --count_type Piter\n'
)


def main(file_path, count_type):
    '''
    Starting point of the program
    '''
    #
    txt_file = TxtFile()
    txt_file.set_file_path(file_path)
    #
    tickets_file = TicketsFileAnalyzer(
        file=txt_file,
        count_type=count_type
    )
    #
    TICKETS_FILE_NAME = file_path.split('/')[-1]
    RESULT_MSG = (
        f'File "{TICKETS_FILE_NAME}" was counted by "{count_type}" method '
        f'and it has {tickets_file.lucky_tickets} lucky tickets'
    )
    #
    print(RESULT_MSG)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=WELCOME_MSG,
        formatter_class=RawTextHelpFormatter,
    )
    #
    parser.add_argument(
        "-f",
        "--file_path",
        help='File path to the file with tickets numbers',
        type=str
    )
    #
    parser.add_argument(
        "-ct",
        "--count_type",
        help='"Lucky ticket" count type',
        choices=['Moscow', 'Piter'],
        type=lambda s: s.capitalize()
    )
    #
    args = parser.parse_args()
    #
    if not args.file_path or not args.count_type:
        print(WELCOME_MSG)
        sys.exit()
    #
    main(
        file_path=args.file_path,
        count_type=args.count_type
    )
