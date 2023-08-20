import mysql.connector

class MySQL_Connection:

    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def cursor_connect(self):
        try:
            self.connection_mysql = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'password',
                database = 'database'
            )

            self.cursor_mysql = self.connection_mysql.cursor()

        except mysql.connector.Error as err:
            print(f"Eroare la conectarea la baza de date: {err}")

    def close_connection(self):
        if self.cursor_mysql:
            self.cursor_mysql.close()
        
        if self.connection_mysql:
            self.connection_mysql.close()