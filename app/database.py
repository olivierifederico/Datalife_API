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

class Alfa2(DataLife):
    alfa2 = TextField(primary_key=True)
    nombre_espanol = CharField()
    nombre_ingles = CharField()
    alfa3 = ForeignKeyField(Paises)
    latitud = FloatField()
    longitud = FloatField()

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
    data = Alfa2.select(Alfa2.alfa2.alias('a2'),Alfa2.nombre_ingles).limit(8)
    db.close()
    #BORRAR
    data = pd.DataFrame(data.dicts())
    data = data.to_dict(orient='index')
    print(data)
    #BORRAR
    return data


#Devuelve una lista con la lista de los paises y un dataframe con los datos historicos
def get_countrystdv():
    try:
        db.connect()
    except:
        pass
    #chequear que los a;os funcionen bien cuando se hacen multiples joins

    #Query
    data = Alfa2.select(Alfa2.alfa2,Alfa2.alfa3,Alfa2.nombre_ingles,Esperanza.year,Esperanza.esperanza).join(Esperanza,on=(Alfa2.alfa3 == Esperanza.pais_id))
    #to Dataframe
    data = pd.DataFrame(data.dicts())
    #stddev calc
    data2 = data.groupby('alfa3')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['alfa3'].values.tolist()
    #filtro
    bool_lista = data['alfa3'].isin(lista_paises)
    data = data[bool_lista]
    #Preparacion diccionario
    base = data.drop(['esperanza','year'],axis=1).groupby('alfa2')
    base = base.first().reset_index().to_dict(orient='index')
    for i in base:
        datax = base[i]['alfa3']
        filt = data['alfa3'] == datax
        df = data[filt].reset_index(drop=True)
        keylist = df['year'].values
        valuelist = df['esperanza'].values
        #print(base)
        if base[i]['alfa3'] == df['alfa3'][0]:
            dictzipped = dict(zip(keylist,valuelist))
            base[i]["esperanza"] = dictzipped
    db.close()
    return base

print(get_countrystdv())