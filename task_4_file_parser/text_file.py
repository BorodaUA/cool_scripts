import fileinput
import sys


class TextFileReader:
    '''
    A TextFileReader class
    '''
    @staticmethod
    def generate_list_of_strings(text_file, chunk_size=1024):
        """
        Helper generator that reads a file and yidld a list
        of strings one by one till the end of the file
        """
        while True:
            data = text_file.readlines(chunk_size)
            if not data:
                break
            yield data


class TxtFile(TextFileReader):
    '''
    A .txt file class
    '''

    def __init__(self, file_path=None):
        '''
        Initialization of an instance
        '''
        self.file_path = file_path

    def set_file_path(self, file_path):
        '''
        Setter method for file object
        '''
        try:
            with open(file_path, 'r'):
                pass
        except (FileNotFoundError, PermissionError) as e:
            sys.exit(e)
        self.file_path = file_path

    def count_query_apperance_in_file(self, query):
        '''
        Return count of how many times a word appears in a
        text file
        '''
        WORD_APPEARANCE_COUNT = 0
        #
        with open(self.file_path, 'r') as f:
            #
            for chunk_list in TxtFile.generate_list_of_strings(f):
                #
                for line in chunk_list:
                    #
                    word_count = line.count(query)
                    WORD_APPEARANCE_COUNT += word_count
        #
        return WORD_APPEARANCE_COUNT

    def find_and_replace_str_in_file(self, find_string, replace_string):
        '''
        Return count of how many times a find_string was
        replaced in a text file
        '''
        REPLACEMENT_COUNT = 0
        #
        with fileinput.input(self.file_path, inplace=True) as f:
            for line in f:
                word_count = line.count(find_string)
                REPLACEMENT_COUNT += word_count
                print(
                    line.replace(
                        find_string,
                        replace_string,
                    ), end='')
        #
        return REPLACEMENT_COUNT
