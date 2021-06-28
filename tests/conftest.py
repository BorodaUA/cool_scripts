import pytest
import subprocess
import os
from pathlib import Path


@pytest.fixture(scope='function')
def cli_client():
    '''
    Command line fixture
    '''
    def _cli_client(cli_command):
        proc = subprocess.Popen(
            cli_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        #
        cli_out, cli_error = proc.communicate()
        #
        return cli_out, cli_error, proc.returncode
    #
    yield _cli_client


@pytest.fixture(scope='function')
def create_txt_test_file():
    '''
    A txt file creation fixture
    '''
    #
    def _create_txt_test_file(dir_path, file_path):
        '''
        Return file object
        '''
        global test_dir
        global test_file_path
        #
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        #
        file_obj = open(file_path, 'w')
        #
        test_dir = dir_path
        test_file_path = file_path
        #
        return file_obj
    #
    yield _create_txt_test_file
    #
    try:
        os.remove(test_file_path)
    except (FileNotFoundError, PermissionError) as e:
        return e
    #
    try:
        os.rmdir(test_dir)
    except (FileNotFoundError, PermissionError) as e:
        return e
