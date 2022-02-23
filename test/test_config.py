import pytest
import config
import os.path
from lib.configuration import Configuration

class TestConfigSecretsFile:
    def test_secrets_exist_is_true(self):
        path_to_secrets = 'config/secrets.py'

        assert os.path.exists(path_to_secrets) == True, "Il File " + path_to_secrets + " non e' presente"


class TestConfigurationLib:
    def test_get_odbc_dict_has_knows_keys(self):
        knows_keys = ['driver',
                    'server', 
                    'database', 
                    'username', 
                    'password']
        conf = Configuration()
        
        assert list(conf.get_odbc('ersurb').keys()) == knows_keys
        assert list(conf.get_odbc('erdis_read').keys()) == knows_keys
