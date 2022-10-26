#Importacion de librerias
from peewee import PostgresqlDatabase

#Datos de conexion
DBNAME = '***REMOVED***'
DBUSER = '***REMOVED***'
DBKEY = '***REMOVED***'
DBHOST = 'localhost'
DBPORT = 5432

DBHOST = '***REMOVED***'
DBPORT = ***REMOVED***




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


<<<<<<< HEAD


=======
>>>>>>> 09989d98b397c3d783c3dc07eb00911f344a51d8
