import sys
import argparse
from text_file_parser import FindAndCount, FindAndReplace
from text_file import TxtFile


class FileParser:
    '''
    A File parser class
    '''
    FILE_NAME = __file__.split('/')[-1]
    WELCOME_MSG = (
        '*** Welcome to the file parser program ***\n'
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
        '--find_string Cat --replace_string Dog'
    )


if __name__ == "__main__":
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
        print(FileParser.WELCOME_MSG)
        sys.exit()
    #
    if args.file_path:
        file_name = args.file_path.split('/')[-1]
    #
    file_obj = TxtFile(file_path=args.file_path)
    if args.mode == 1:
        #
        if args.file_path is None or args.query is None:
            print(FileParser.WELCOME_MSG)
            sys.exit()
        #
        find_and_count = FindAndCount(
            file=file_obj,
            query=args.query
        )
        appearance_count = find_and_count.count_query_apperance_in_file
        #
        if isinstance(appearance_count, str):
            print(appearance_count)
            sys.exit()
        #
        if isinstance(appearance_count, int):
            print(
                f'Query "{args.query}" appears in the "{file_name}" file '
                f'{appearance_count} time(s).'
            )
            sys.exit()
    if args.mode == 2:
        #
        if (
            args.file_path is None or args.find_string is None or
            args.replace_string is None
                ):
            print(FileParser.WELCOME_MSG)
            sys.exit()
        #
        find_and_replace = FindAndReplace(
            file=file_obj,
            find_string=args.find_string,
            replace_string=args.replace_string
        )
        replacement_count = find_and_replace.find_and_replace_str_in_file()
        #
        if isinstance(replacement_count, str):
            print(replacement_count)
            sys.exit()
        #
        if isinstance(replacement_count, int):
            print(
                f'"Find string" "{args.find_string}" was replaced by '
                f'"Replace string" "{args.replace_string}" '
                f'{replacement_count} time(s).'
            )
            sys.exit()
