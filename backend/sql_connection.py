import mysql.connector
import os

# Set your MySQL credentials here
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'pass12345'
MYSQL_DB = 'pystoredb'
MYSQL_HOST = '127.0.0.1'

__cnx = None

def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB,
                host=MYSQL_HOST
            )
        except mysql.connector.errors.ProgrammingError as e:
            print("First connection attempt failed, trying with no password...")
            __cnx = mysql.connector.connect(
                user=MYSQL_USER,
                database=MYSQL_DB,
                host=MYSQL_HOST
            )
    return __cnx