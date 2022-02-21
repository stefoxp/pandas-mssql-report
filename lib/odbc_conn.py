import pyodbc

class Connect():
    def __init__(self, driver, server, database, username, password):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def connection(self):
        return pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
