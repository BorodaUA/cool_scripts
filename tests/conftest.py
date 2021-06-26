import pytest
import subprocess


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
