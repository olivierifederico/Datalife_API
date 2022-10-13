#Importacion de librerias
from peewee import PostgresqlDatabase

#Datos de conexion
DBNAME = '***REMOVED***'
DBUSER = '***REMOVED***'
DBKEY = '***REMOVED***'
DBHOST = '***REMOVED***'
DBPORT = ***REMOVED***

db = PostgresqlDatabase(DBNAME,user = DBUSER, password = DBKEY, host = DBHOST ,port = DBPORT)

#Funciones para la api

#Obtener nombre de tablas
def get_tables():
    db.connect()
    data = db.get_tables()
    db.close()
    return data
