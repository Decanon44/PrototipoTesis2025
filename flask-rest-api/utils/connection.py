import mysql.connector

def conectar():
  cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="12345",
    database="tienda")
  return cnx

