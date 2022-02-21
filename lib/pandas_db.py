import pandas

class DbWithPandas():
    def __init__(self, connection):
        self.connection = connection

    def query(self, sql_str):
        df = pandas.read_sql_query(sql_str, self.connection)
        return df
