from peewee import Model,TextField,CharField,IntegerField,ForeignKeyField,FloatField
from connector import db
import pandas as pd
# Creacion del modelo de base de datos

class DataLife(Model):
    class Meta:
        database = db

"""
Ej:

class Nombre_tabla(Database):
    nombre de columna = Tipo de valor
    ej:

    columna0 = TextField(primary_key=True)
    columna1 = CharField()
    columna2 = FloatField()
    columna3 = TextField()
    columna4 = IntegerField()

"""

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

# Api Front


def data_front():
    """
Devuelve un diccionario que contiene un diccionario por cada pais,
y dentro de este tiene valores y diccionarios, donde en
estos ultimos se encuentran valores historicos.

Ej:
    {
        0:{
            nombre:paisx, 
            latitud:valor, 
            etc:etc, 
            metrica1:{
                year1:valor,
                year2:valor,
                year3:valor
            },
            metrica2:{
                year1:valor,
                year2:valor,
                year3:valor
            }
        }
    }
"""
    try:
        db.connect() #conexion a la base de datos
    except:
        pass
    data= []

    """queries utilizando peewee, se guardan en una lista.
    - 0 Esperanza, nombre, id, latitud y logitud
    - 1 Terciario completo
    - 2 Esperanza saludable
    - 3 Acceso de la poblacion al credito privado
    """
    data.append(Pais.select(Pais.pais_id,Pais.nombre_EN,Pais.nombre_ESP,Pais.latitud,Pais.longitud,Esperanza.esperanza,Esperanza.year).join(Esperanza,on=(Pais.pais_id == Esperanza.pais_id)))
    data.append(Terciario.select(Terciario.pais_id, Terciario.year, Terciario.terciario_completo.alias('terciario')))
    data.append(Esperanza_saludable.select(Esperanza_saludable.pais_id,Esperanza_saludable.year, Esperanza_saludable.esp_vida_salud_60.alias('esperanza_saludable')))
    data.append(Economia.select(Economia.pais_id, Economia.year, Economia.credito_al_sector_privado.alias('credito_privado')))
    
    # Conversion de los diccionarios a dataframe
    data_df = []
    for i in range(len(data)):
        data_df.append(pd.DataFrame(data[i].dicts()))
    # Calculo de la desviacion STD
    """
    - Se agrupan los paises por 'pais_id'
    - Se calcula la desviacion STD de la columna 'esperanza'
    - Se ordenan de manera descendente
    - Se resetea el index
    - Se guardan solo los paises que tengan desv std mayor a 2.5,
    y en caso de que haya mas de 8, los que tengan la mayor desv std.
    - Se guardan los paises en una lista para utilizarla posteriormente en un filtro 
    """
    data2 = data_df[0].groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()

    # Se aplica el filtro de la lista de paises al DataFrame
    for i in range(len(data_df)):
        bool_x = data_df[i]['pais_id'].isin(lista_paises)
        data_df[i] = data_df[i][bool_x]

    # Preparacion del diccionario base, donde solo quedan los datos generales
    # de los paises seleccionados y la estructura para ingestar los datos posteriormente.
    base = data_df[0].drop(['esperanza','year'],axis=1).groupby('pais_id')
    base = base.first().reset_index().to_dict(orient='index')

    """
    Por cada pais en el diccionario base se aplica un filtro
    en los dataframes previamente creados
    para poder extraer los los annos y los valores de cada metrica,
    y posteriormente ser agregados al diccionario base

    """
    for a in base:
        data_x = base[a]['pais_id']
        data_df_filt = []
        data_key = []
        data_value = []
        # Filtro aplicado a cada dataframe dependiendo de que metrica sea.
        # Se extraen los valores en 2 listas, data_key y data_value
        for i in range(len(data_df)):
            filt_x = data_df[i]['pais_id'] == data_x
            data_df_filt.append(data_df[i][filt_x].reset_index(drop=True))
            data_key.append(data_df_filt[i]['year'].values)
            if i == 0:
                metrica_x = 'esperanza'
            elif i == 1:
                metrica_x = 'terciario'
            elif i == 2:
                metrica_x = 'esperanza_saludable'
            elif i == 3:
                metrica_x = 'credito_privado'
            data_value.append(data_df_filt[i][metrica_x].values)

        # Se crea un diccionario con el nombre "dict_x" por cada metrica 
        # el cual contiene el anno(key) y valor(value)
        # y se agrega al diccionario base: metrica(key):dict_x(key)
        if base[a]['pais_id'] == data_df_filt[0]['pais_id'][0]:
            for i in range(len(data_df)):
                dict_x = dict(zip(data_key[i],data_value[i]))
                if i == 0:
                    metrica_x = 'esperanza'
                elif i == 1:
                    metrica_x = 'terciario'
                elif i == 2:
                    metrica_x = 'esperanza_saludable'
                elif i == 3:
                    metrica_x = 'credito_privado'
                base[a][metrica_x] = dict_x
    db.close() # Cierre de conexion a la base de datos
    return base