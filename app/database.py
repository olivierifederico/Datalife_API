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

#Devuelve una lista con la lista de los paises y un dataframe con los datos historicos
def get_countrystdv():
    try:
        db.connect()
    except:
        pass
    #chequear que los a;os funcionen bien cuando se hacen multiples joins

    #Query
    data = Pais.select(Pais.pais_id,Pais.nombre_EN,Esperanza.year,Esperanza.esperanza).join(Esperanza,on=(Pais.pais_id == Esperanza.pais_id))
    #to Dataframe
    data = pd.DataFrame(data.dicts())
    #stddev calc
    data2 = data.groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()
    #filtro
    bool_lista = data['pais_id'].isin(lista_paises)
    data = data[bool_lista]
    #Preparacion diccionario
    base = data.drop(['esperanza','year'],axis=1).groupby('pais_id')
    base = base.first().reset_index().to_dict(orient='index')
    for i in base:
        datax = base[i]['pais_id']
        filt = data['pais_id'] == datax
        df = data[filt].reset_index(drop=True)
        #Agregado de valores al diccionario
        keylist = df['year'].values
        valuelist = df['esperanza'].values
        if base[i]['pais_id'] == df['pais_id'][0]:
            dictzipped = dict(zip(keylist,valuelist))
            base[i]["esperanza"] = dictzipped
    db.close()
    return base
