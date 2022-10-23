
from peewee import Model,TextField,CharField,IntegerField,ForeignKeyField,FloatField
from connector import db
import pandas as pd

from data import dict_paises

#Creacion del modelo de base de datos

class DataLife(Model):
    class Meta:
        database = db

class Pais(DataLife):
    pais_id=TextField(primary_key=True) 
    nombre_ESP = CharField()
    nombre_EN = CharField()
    codigo_pais = CharField()
    latitud = FloatField()
    longitud= FloatField()

class Esperanza(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    esperanza = FloatField()

class Salud(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    gasto_salud = FloatField()

class Esperanza_gen(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    esperanza_fem = FloatField()
    esperanza_mas = FloatField()

class Educacion(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    gasto_educacion = FloatField()

class Economia(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    inflacion= FloatField()
    credito_al_sector_privado = FloatField()
    crecimiento_per_capita_Bruto = FloatField()
    riesgo_empobrecimiento_salud = FloatField()
    cremiento_pob = FloatField()

class Ambiente(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    exposcion_contaminacion = FloatField()

class Locacion(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    pais = CharField()
    longitude = FloatField()
    latitude = FloatField()

class Terciario(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    terciario_completo = FloatField()

class Esperanza_saludable(DataLife):
    id = IntegerField(primary_key=True)
    pais_id = ForeignKeyField(Pais)
    year = IntegerField()
    esp_vida_salud_60 = FloatField()

#Funcion para crear las tablas
def create_tables():
    db.connect()
    Pais.create_table()
    Esperanza.create_table()
    Salud.create_table()
    Esperanza_gen.create_table()
    Educacion.create_table()
    Economia.create_table()
    Ambiente.create_table()
    
    db.close()


#Api Front

"""def get_coordinates():
    try:
        db.connect()
    except:
        pass
    data = Locacion.select(Locacion.pais,Locacion.longitude,Locacion.latitude).limit(5)
    db.close()
    return data"""

#Devuelve una lista con la lista de los paises y un dataframe con los dataframes historicos
"""def get_countrystdv():
    try:
        db.connect()
    except:
        pass
    #chequear que los a;os funcionen bien cuando se hacen multiples joins
    data = Pais.select(Pais.pais_id,Pais.nombre,Esperanza.esperanza,Esperanza.year).join(Esperanza,on=(Paises.pais_id == Esperanza.pais_id))
    data = pd.DataFrame(data.dicts())
    data2 = data.groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()
    bool_lista = data['pais_id'].isin(lista_paises)
    data = data[bool_lista]
    lista_paises = data['nombre'].unique()
    return [lista_paises,data]"""

