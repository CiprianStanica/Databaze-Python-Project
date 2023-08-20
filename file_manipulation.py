import os
import shutil
import datetime
from mysql_connection import MySQL_Connection

fisier_text = "intrari/Poarta1.txt"

class FileManipulation:
    def __init__(self):
        self.db_connection = MySQL_Connection(host = 'localhost',
             user = 'root',
             password = 'password',
             database = 'database')
        self.db_connection.cursor_connect()

    def citeste_text(self):
        with open(fisier_text, "r") as fisier:
            citeste_fisier = fisier.readlines()
            for linie in citeste_fisier:
                split_cuvinte = linie.strip().split(",")
                idpersoana = split_cuvinte[0]
                data_str = split_cuvinte[1]
                sens = split_cuvinte[2]
                poarta = 1

                data_format = '%Y-%m-%dT%H:%M:%S.%fZ'
                data = self.formatare_data(data_str, data_format)

                self.inserare_in_baza(idpersoana, data, sens, poarta)

    def formatare_data(self, data_str, format_date):
        data = datetime.datetime.strptime(data_str, format_date).strftime('%Y-%m-%d %H:%M:%S')
        return data

    def inserare_in_baza(self, idpersoana, data, sens, poarta):
        query = "INSERT INTO ACCES (idpersoana, data, sens, poarta) VALUES (%s, %s, %s, %s)"
        valori = (idpersoana, data, sens, poarta)

        cursor = self.close_connection()
        cursor.execute(query, valori)
        self.db_connection.connection_mysql.commit()

    def muta_fisier_backup(self, fisier_text):
        nume_fisier = os.path.basename(fisier_text)
        folder_backup = "backup_intrari/"
        cale_destinatie = os.path.join(folder_backup, nume_fisier)
        shutil.move(fisier_text, cale_destinatie)
        print(f"Fisierul a fost mutat in {cale_destinatie}")
        return

    def close_connection(self):
        self.db_connection.close_connection()

if __name__ == "__main__":
    file_manipulator = FileManipulation()
    file_manipulator.citeste_text()
    file_manipulator.muta_fisier_backup()
    file_manipulator.close_connection()
    
