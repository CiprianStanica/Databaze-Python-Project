import os
from muta_intrari_txt_si_csv import fisier_text, fisier_csv, FisierTxt, FisierCsv, time

def main():
    while True:
        if os.path.exists(fisier_text):
            try:
                txt_file = FisierTxt()
                txt_file.citeste_text(fisier_text)
            except FileNotFoundError as e:
                print("Nu a fost adaugat niciun fisier text")
            finally:
                txt_file.close_connection()

        if os.path.exists(fisier_csv):
            try:
                csv_file = FisierCsv()
                csv_file.citeste_csv(fisier_csv)
            except FileNotFoundError as e:
                print("Nu a fost adaugat niciun fisier CSV")
            finally:
                csv_file.close_connection()

        time.sleep(5)

if __name__ == "__main__":
    main()