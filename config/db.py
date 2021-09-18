import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='parcial',
    port=3306
)