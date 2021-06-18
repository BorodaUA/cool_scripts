import fileinput


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


class FindAndCount(TextFileReader):
    '''
    Class that helps locate and count a string appearance a in text file
    '''

    def __init__(self, file, query):
        '''
        Initialization of an instance
        '''
        self.file = file
        self.query = query

    @property
    def count_query_apperance_in_file(self):
        '''
        Return count of how many times a word appears in a
        text file
        '''
        WORD_APPEARANCE_COUNT = 0
        #
        try:
            with open(self.file.file_path, 'r') as f:
                #
                for chunk_list in FindAndCount.generate_list_of_strings(f):
                    #
                    for line in chunk_list:
                        #
                        word_count = line.count(self.query)
                        WORD_APPEARANCE_COUNT += word_count

        except PermissionError as e:
            return str(e)
        except FileNotFoundError as e:
            return str(e)
        return WORD_APPEARANCE_COUNT


class FindAndReplace(TextFileReader):
    '''
    Class that helps locate and replace a string a in text file with new
    string
    '''

    def __init__(self, file, find_string, replace_string):
        '''
        Initialization of an instance
        '''
        self.file = file
        self.find_string = find_string
        self.replace_string = replace_string

    def find_and_replace_str_in_file(self):
        '''
        Return count of how many times a find_string was
        replaced in a text file
        '''
        REPLACEMENT_COUNT = 0
        #
        try:
            with fileinput.input(self.file.file_path, inplace=True) as f:
                for line in f:
                    word_count = line.count(self.find_string)
                    REPLACEMENT_COUNT += word_count
                    print(
                        line.replace(
                            self.find_string,
                            self.replace_string,
                        ), end='')
        except PermissionError as e:
            return str(e)
        except FileNotFoundError as e:
            return str(e)
        return REPLACEMENT_COUNT
