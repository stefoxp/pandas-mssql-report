import pytest
import config
import os.path

class TestConfigSecrets:
    def test_secrets_exist_is_true(self):
        path_to_secrets = 'config/secrets.py'

        assert os.path.exists(path_to_secrets) == True
