from config import secrets
from lib.odbc_conn import Connect
from lib.pandas_db import DbWithPandas

def main():
    print("main function")
    cls_cn = Connect(secrets.ersurb['driver'],
                    secrets.ersurb['server'],
                    secrets.ersurb['database'],
                    secrets.ersurb['username'],
                    secrets.ersurb['password']
    )
    cn = cls_cn.connection()

    s_str = 'SELECT TOP 10 * FROM COMU_MATRICOLE WHERE Annullato = 0;'

    cls_pd = DbWithPandas(cn)
    df = cls_pd.query(s_str)

    print(df.head())

    cn.close()


if __name__ == '__main__':
    main()
