from peewee import Model,TextField,CharField,IntegerField,ForeignKeyField,FloatField
from connector import db
import pandas as pd


#Creacion del modelo de base de datos

class DataLife(Model):
    class Meta:
        database = db

class Paises(DataLife):
    pais_id=TextField(primary_key=True) 
    nombre = CharField()

class Esperanza(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    esperanza = FloatField()

class Salud(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    gasto_salud = FloatField()

class Esperanza_gen(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    esperanza_fem = FloatField()
    esperanza_mas = FloatField()

class Educacion(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    gasto_educacion = FloatField()

class Economia(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    inflacion= FloatField()
    Credito_al_sector_privado = FloatField()
    Crecimiento_per_capita_Bruto = FloatField()
    Riesgo_empobrecimiento_salud = FloatField()
    Cremiento_pob = FloatField()

class Ambiente(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    exposcion_contaminacion = FloatField()

class Locacion(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    pais = CharField()
    longitude = FloatField()
    latitude = FloatField()

class Terciario(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    Year = IntegerField()
    terciario_completo = FloatField()

class Esperanza_saludable(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Paises)
    year = IntegerField()
    esp_vida_salud_60 = FloatField()

#Funcion para crear las tablas
def create_tables():
    db.connect()
    Paises.create_table()
    Esperanza.create_table()
    Salud.create_table()
    Esperanza_gen.create_table()
    Educacion.create_table()
    Economia.create_table()
    Ambiente.create_table()
    Locacion.create_table()
    db.close()


#Api Front

def get_coordinates():
    try:
        db.connect()
    except:
        pass
    data = Locacion.select().limit(5)
    db.close()
    return data

    
#Devuelve una lista con la lista de los paises y un dataframe con los dataframes historicos
def get_countrystdv():
    try:
        db.connect()
    except:
        pass
    #chequear que los a;os funcionen bien cuando se hacen multiples joins
    data = Paises.select(Paises.pais_id,Paises.nombre,Esperanza.esperanza,Esperanza.year).join(Esperanza,on=(Paises.pais_id == Esperanza.pais_id))
    data = pd.DataFrame(data.dicts())
    data2 = data.groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()
    bool_lista = data['pais_id'].isin(lista_paises)
    data = data[bool_lista]
    lista_paises = data['nombre'].unique()
    return [lista_paises,data]

