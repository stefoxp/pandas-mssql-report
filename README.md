# Report from Ms SQL server with pandas

Report pandas da database

Procedura di attivazione:

- python -m venv env (oppure python3 -m venv env)
- source env/bin/activate
- pip3 install pandas
- sudo apt-get install unixodbc-dev
- sudo -H pip3 install pyodbc -> [Documentazione](https://github.com/mkleehammer/pyodbc/wiki)
- [Driver ODBC per SQL server](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)
- pip install Flask
- pip install pytest
- pip freeze > requirements.txt
- $ odbcinst -j
- pip install -r requirements.txt
- python -m flask run

> N.B. è necessario installare apt-get install unixodbc-dev -> non basta su Ubuntu 20 (il 12/02/2022): non riesco a installare pip install pyodbc
Devo provare ad installare il wheel come indicato su [https://github.com/mkleehammer/pyodbc/wiki/Install](https://github.com/mkleehammer/pyodbc/wiki/Install)

- Tratto da [https://github.com/microsoft/msphpsql/issues/1112](https://github.com/microsoft/msphpsql/issues/1112) per la connessione al server SQL 2008 R2 è necessario impostare su /etc/ssl/openssl.cnf TLSv1.0 invece di TLSv1.2

[default_conf]
ssl_conf = ssl_sect

[ssl_sect]
system_default = system_default_sect

[system_default_sect]
MinProtocol = TLSv1.0
CipherString = DEFAULT@SECLEVEL=2