# import os
# import csv
# import mysql.connector
# import shutil
# import datetime


# path = "intrari/"
# fisier_text = (f"{path}Poarta1.txt")
# fisier_csv = (f"{path}Poarta2.txt")


# class Fisiere():
#     def __init__(self):
#         self.connection_mysql = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='password',
#             database='database'
#             )
#         self.cursor_mysql = self.connection_mysql.cursor()




# class FisierTxt(Fisiere):
#     def citeste_text(self):
#         continut = []
#         with open(f"{fisier_text}","r") as fisier:
                
#                 citeste_fisier = fisier.readlines()
            
#                 for linie in citeste_fisier:
#                         strip_randuri = linie.strip("\n ;")
#                         split_cuvinte = linie.split(",")
#                         continut.append(split_cuvinte)
            
#                 for element in continut:
#                         idpersoana = element[0]
#                         data = element[1]
#                         sens = element[2]
#                         poarta = 1
#                         self.cursor_mysql.execute(f"INSERT INTO ACCES VALUES ('{idpersoana}','{data}','{sens}','{poarta});")
#                         self.connection_mysql.commit() 
#                         self.cursor_mysql.close()
#                         self.connection_mysql.close()
#                         print("Fisierul Txt a fost adaugat in baza de date")

# txt_file = FisierTxt()
# txt_file.citeste_text()


import mysql.connector
from datetime import datetime

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

# class FisierTxt(Fisiere):
#     def citeste_text(self, fisier_text):
#         with open(fisier_text, "r") as fisier:
#             citeste_fisier = fisier.readlines()
#             for linie in citeste_fisier:
#                 split_cuvinte = linie.strip().split(",")
#                 idpersoana = split_cuvinte[0]
#                 data_str = split_cuvinte[1]
#                 sens = split_cuvinte[2]
#                 poarta = 1
                
#                 # Convertirea formatului dată și oră
#                 data_format = '%Y-%m-%dT%H:%M:%S.%fZ'
#                 data = datetime.strptime(data_str, data_format).strftime('%Y-%m-%d %H:%M:%S')
                
#                 self.cursor_mysql.execute(f"INSERT INTO ACCES VALUES ('{idpersoana}', '{data}', '{sens}', '{poarta}')")
#                 self.connection_mysql.commit()
#                 print("Fisierul Txt a fost adaugat in baza de date")

# try:
#     fisier_text = "intrari/Poarta1.txt"
#     txt_file = FisierTxt()
#     txt_file.citeste_text(fisier_text)
# except Exception as e:
#     print(f"Erroare: {e}")
# finally:
#     txt_file.close_connection()
class FisierCsv(Fisiere):
    def citeste_csv(self, fisier_csv):
        with open(fisier_csv, "r", encoding='utf-8') as fisier:
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
                
                self.cursor_mysql.execute(f"INSERT INTO ACCES VALUES ('{idpersoana}', '{data}', '{sens}', '{poarta}')")
                self.connection_mysql.commit()
                print("Fisierul Txt a fost adaugat in baza de date")
try:
    fisier_csv = "intrari/Poarta2.csv"
    csv_file = FisierCsv()
    csv_file.citeste_csv(fisier_csv)
except Exception as e:
    print(f"Erroare: {e}")
finally:
    csv_file.close_connection()