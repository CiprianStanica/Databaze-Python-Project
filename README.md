# Databaze-Python-Project
 This is a database made in Python, in which the hours worked by the employees of a company are monitored with the help of two gates through which they enter or leave:

 -First, the hours they entered or leaved on one of the two gates can be found in two documents: 'Poarta1.csv' and 'Poarta1.txt', which can be found in 'intrari' folder;

    In 'main.py', can be found a couple of functions, that make the whole process complete:
        1. 'muta_intrari_txt_si_csv.py' checks the 'intrari' folder every 5 seconds, and if it founds the two files of the two gates, it reads  and insert them in the MySQL databse, in the 'ACCES' tabel. After that, it moves the thwo files in the 'backup_intrari' folder. If it doesn`t find any files in 'intrari', the function will display the next messaje: "Nu a fost gasit niciun fisier nou"
        2. 'calcul_ore.py' calculates the hours based on the introduced data
        3. 'send_email.py' sends an gmail in wich is attached a file that contains the workers that didn`t fulfilled the minim hours of work they had to do

-Second, a server is created, that takes the data entered ('nume','prenume','companie','idmanager'), and stores them into a MySQL databse, in 'utilizatori' tabel;

        1. 'server.py' creates the server and stores the data
        2. the folder 'templates' contains the 'html'files, 'index.html' and 'formular.html', in which can be found the design for the web pages
        