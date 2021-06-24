import sys
import argparse
from text_file import TxtFile


FILE_NAME = __file__.split('/')[-1]
WELCOME_MSG = (
    '\n*** Welcome to the file parser program ***\n'
    "This program have 2 modes:\n"
    'Mode 1: Find and count how many times '
    'a "query" appears in the text file\n'
    'Mode 1 Usage example: \n'
    f'python {FILE_NAME} -m 1 -f ./big_data.txt -q This \n'
    f'python {FILE_NAME} --mode 1 --file_path ./big_data.txt'
    ' --query This \n'
    '\n'
    'Mode 2: Find and replace "find_string" with "replace_string"'
    'in the text file\n'
    'Mode 2 Usage example: \n'
    f'python {FILE_NAME} -m 2 -f ./big_data.txt -fs Cat -rs Dog \n'
    f'python {FILE_NAME} --mode 2 --file_path ./big_data.txt '
    '--find_string Cat --replace_string Dog\n'
)


def main(**kwargs):
    '''
    Starting point of the program
    '''
    txt_file = TxtFile()
    txt_file.set_file_path(kwargs['file_path'])
    #
    file_name = kwargs['file_path'].split('/')[-1]
    #
    if kwargs['mode'] == 1:
        #
        appearance_count = txt_file.count_query_apperance_in_file(
            query=kwargs['query']
        )
        #
        return (
                f'Query "{kwargs["query"]}" appears in the "{file_name}" file '
                f'{appearance_count} time(s).'
            )
    #
    if kwargs['mode'] == 2:
        #
        replacement_count = txt_file.find_and_replace_str_in_file(
            find_string=kwargs['find_string'],
            replace_string=kwargs['replace_string']
        )
        #
        return (
                f'"Find string" "{kwargs["find_string"]}" was replaced by '
                f'"Replace string" "{kwargs["replace_string"]}" '
                f'{replacement_count} time(s).'
            )


if __name__ == "__main__":
    # sys.argv += [
    #     '-m',
    #     '1',
    #     '-f',
    #     './big_data.txt',
    #     '-q',
    #     'Dog',
    # ]
    # sys.argv += [
    #     '-m',
    #     '2',
    #     '-f',
    #     '/usr/src/app/big_data.txt',
    #     '-fs',
    #     'Cat',
    #     '-rs',
    #     'Dog'
    # ]
    parser = argparse.ArgumentParser()
    #
    parser.add_argument(
        "-m",
        "--mode",
        help='Program work mode',
        type=int,
        choices=[1, 2]
    )
    #
    parser.add_argument(
        "-f",
        "--file_path",
        help='File path to a text file',
        type=str,
    )
    #
    parser.add_argument(
        "-q",
        "--query",
        help='Query to find in a text file',
        type=str
    )
    #
    parser.add_argument(
        "-fs",
        "--find_string",
        help='A string to find in a text file',
        type=str
    )
    #
    parser.add_argument(
        "-rs",
        "--replace_string",
        help='A string that replaces the "find_string" in a text file',
        type=str
    )
    #
    args = parser.parse_args()
    #
    if len(sys.argv) == 1:
        print(WELCOME_MSG)
        sys.exit()
    #
    if args.mode == 1:
        #
        if args.file_path is None or args.query is None:
            print(WELCOME_MSG)
            sys.exit()
        #
        print(
            main(
                mode=args.mode,
                file_path=args.file_path,
                query=args.query
            )
        )
    #
    if args.mode == 2:
        #
        if (
            args.file_path is None or args.find_string is None or
            args.replace_string is None
                ):
            print(WELCOME_MSG)
            sys.exit()
        #
        print(
            main(
                mode=args.mode,
                file_path=args.file_path,
                find_string=args.find_string,
                replace_string=args.replace_string
            )
        )
