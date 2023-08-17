from flask import Flask, render_template,request
import mysql.connector
app = Flask(__name__)

connection_mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='database'
    )
cursor_mysql = connection_mysql.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formular')
def meniu():
    return render_template('formular.html')

@app.route("/register", methods = ["POST","GET"])
def inregistrare():
    if request.method == "POST":
        nume = request.form["nume"]
        prenume = request.form["prenume"]
        nume_companie =request.form["nume_companie"]
        id_manager = request.form["id_manager"]
        inregistrare = f"INSERT INTO UTILIZATORI values (null,'{nume}','{prenume}','{nume_companie}','{id_manager}');"
        cursor_mysql.execute(inregistrare)
        connection_mysql.commit()

  
if __name__ == '__main__':
    app.run(debug=True)

cursor_mysql.close()
connection_mysql.close()
    