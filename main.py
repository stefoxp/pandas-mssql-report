from config import secrets
from lib.odbc_conn import Connect
from lib.pandas_db import DbWithPandas
from lib.configuration import Configuration

def main():
    # print("main function")

    conf = Configuration()

    cls_cn = Connect(conf.get_odbc('ersurb'))
    cn = cls_cn.connection()

    # s_str = 'SELECT TOP 10 * FROM COMU_MATRICOLE WHERE Annullato = 0;'
    s_str = '''SELECT TOP 100 
    ct.Codice as TipoUtenteCodice, ct.Descrizione As TipoUtente, ct.Presidio As PresidioPerTipoUtente
    , cm.Matricola As CodiceEnte, cm.CodiceFiscale, cm.Cognome, cm.Nome, cm.Sesso, cm.Email, cm.Cellulare 
    FROM COMU_MATRICOLE cm
        INNER JOIN COMU_TIPOLOGIE ct
            ON ct.Codice = cm.Tipologia 
    WHERE Annullato = 0'''

    cls_pd = DbWithPandas(cn)
    df = cls_pd.query(s_str)

    print(df.head())

    cn.close()


if __name__ == '__main__':
    main()
