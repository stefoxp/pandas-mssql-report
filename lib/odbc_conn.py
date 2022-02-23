import pyodbc

class Connect():
    def __init__(self, odbc_dict: dict()):
        self.driver = odbc_dict['driver']
        self.server = odbc_dict['server']
        self.database = odbc_dict['database']
        self.username = odbc_dict['username']
        self.password = odbc_dict['password']

    def connection(self):
        return pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
