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
