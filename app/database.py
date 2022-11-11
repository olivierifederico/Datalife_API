from peewee import Model,TextField,CharField,IntegerField,ForeignKeyField,FloatField
from connector import db
import pandas as pd
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

#Api Front

#Devuelve una lista con la lista de los paises y un dataframe con los datos historicos
def data_front():
    try:
        db.connect()
    except:
        pass
    data= []
    #queries
    data.append(Pais.select(Pais.pais_id,Pais.nombre_EN,Pais.nombre_ESP,Pais.latitud,Pais.longitud,Esperanza.esperanza,Esperanza.year).join(Esperanza,on=(Pais.pais_id == Esperanza.pais_id)))
    data.append(Terciario.select(Terciario.pais_id, Terciario.year, Terciario.terciario_completo.alias('terciario')))
    data.append(Esperanza_saludable.select(Esperanza_saludable.pais_id,Esperanza_saludable.year, Esperanza_saludable.esp_vida_salud_60.alias('esperanza_saludable')))
    data.append(Economia.select(Economia.pais_id, Economia.year, Economia.credito_al_sector_privado.alias('credito_privado')))
    #queries a df
    #Lista de dicts [0]Esperanza de vida, [1]Terciario, [2]Esp. Saludable, [3]Cred. Priv, [4]Riesgo Pobreza
    data_df = []
    for i in range(len(data)):
        data_df.append(pd.DataFrame(data[i].dicts()))
    #stddev calc
    data2 = data_df[0].groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()
    #filtro
    for i in range(len(data_df)):
        bool_x = data_df[i]['pais_id'].isin(lista_paises)
        data_df[i] = data_df[i][bool_x]
    #Preparacion diccionario
    base = data_df[0].drop(['esperanza','year'],axis=1).groupby('pais_id')
    base = base.first().reset_index().to_dict(orient='index')
    for a in base:
        data_x = base[a]['pais_id']
        data_df_filt = []
        data_key = []
        data_value = []
        #Filtro
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
        #seguir por aca
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
    db.close()
    return base