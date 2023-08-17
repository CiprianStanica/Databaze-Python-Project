from flask import Flask,request
import mysql.connector

aplicatie = Flask(nume)

connection_mysql = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='database'
        )
cursor_mysql = connection_mysql.cursor()

# @app.route('/trecere',methods=["POST"])
# def insert():
#     data=request.get_json()
#     ID = data['idpersoana']
#     DATA =data['data']
#     SENS = data['sens']
#     POARTA = data['poarta']

#     intrare = f"INSERT INTO USERS.ACCES values ('{ID}','{DATA}','{SENS}','{POARTA}');"
#     print(intrare)
#     cursor_mysql.execute(intrare)
#     connection_mysql.commit()
#     return "Trecere inregistrata cu succes!"