from config import secrets

class Configuration:
    config_dict = dict()

    def __init__(self):
        self.config_dict = secrets.odbc_dict

    def keys_verify(self, dict_to_verify: dict()):
        result = True
        
        knows_keys = ['driver',
                    'server', 
                    'database', 
                    'username', 
                    'password']

        for key in knows_keys:
            result and key in dict_to_verify

        return result

    def get_odbc(self, odbc_name: str) -> dict():
        result_dict = self.config_dict[odbc_name]

        if self.keys_verify(result_dict):
            return result_dict
        else:
            return dict()
