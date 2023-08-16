import mysql.connector
import os
from datetime import datetime
import shutil
import time

class Fisiere:
    def __init__(self):
        self.connection_mysql = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='database'
        )
        self.cursor_mysql = self.connection_mysql.cursor()

    def close_connection(self):
        self.cursor_mysql.close()
        self.connection_mysql.close()

class FisierTxt(Fisiere):
    def citeste_text(self, fisier_text):
        with open(fisier_text, "r") as fisier:
            citeste_fisier = fisier.readlines()
            for linie in citeste_fisier:
                split_cuvinte = linie.strip().split(",")
                idpersoana = split_cuvinte[0]
                data_str = split_cuvinte[1]
                sens = split_cuvinte[2]
                poarta = 1
                
                # Convertirea formatului dată și oră
                data_format = '%Y-%m-%dT%H:%M:%S.%fZ'
                data = datetime.strptime(data_str, data_format).strftime('%Y-%m-%d %H:%M:%S')
                
                # Inserare în baza de date
                query = "INSERT INTO ACCES (idpersoana, data, sens, poarta) VALUES (%s, %s, %s, %s)"
                valori = (idpersoana, data, sens, poarta)
                self.cursor_mysql.execute(query, valori)
                self.connection_mysql.commit()
                print("Fisierul Txt a fost adaugat in baza de date")
                fisier.close()
                
                # Mutare în folderul backup_intrari
                self.muta_fisier_backup(fisier_text)
                return
   
    def muta_fisier_backup(self, fisier_text):
        nume_fisier = os.path.basename(fisier_text)
        folder_backup = "backup_intrari/"
        cale_destinatie = os.path.join(folder_backup, nume_fisier)
        shutil.move(fisier_text, cale_destinatie)
        print(f"Fisierul a fost mutat in {cale_destinatie}")
        return

fisier_text = "intrari/Poarta1.txt"
while True:
    if not os.path.exists(fisier_text):
        print("Nu a fost adaugat niciun fisier")
        time.sleep(5)
    else:
        try:
            txt_file = FisierTxt()
            while True:
                txt_file.citeste_text(fisier_text)
                time.sleep(5)
        except FileNotFoundError as e:
            print("Nu a fost adaugat niciun fisier")
        finally:
            txt_file.close_connection()