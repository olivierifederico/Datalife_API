#Importacion de librerias
from peewee import PostgresqlDatabase
import os

#Datos de conexion
DBNAME = os.environ['DBNAME']
DBUSER = os.environ['DBUSER']
DBKEY = os.environ['DBKEY']
DBHOST = os.environ['DBHOST']
DBPORT = os.environ['DBPORT']


db = PostgresqlDatabase(DBNAME,user = DBUSER, password = DBKEY, host = DBHOST ,port = DBPORT)

db.close()


#Funciones para la api

#Obtener nombre de tablas
def get_tables():
    try:
        db.connect()
    except:
        pass
    data = db.get_tables()
    db.close()
    return data