import sys


class TxtFile:
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
        #
        self.file_path = file_path
