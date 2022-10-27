
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
    Terciario.create_table()
    Esperanza_saludable.create_table()
    
    db.close()

"""def load_tables():
    db.connect()
    Pais.insert_many(dict_pais).execute()
    Esperanza.insert_many(dict_esperanza).execute()
    Salud.insert_many(dict_salud).execute()
    Esperanza_gen.insert_many(dict_esperanza_gen).execute()
    Educacion.insert_many(dict_educacion).execute()
    Economia.insert_many(dict_economia).execute()
    Ambiente.insert_many(dict_ambiente).execute()
    Terciario.insert_many(dict_terciario).execute()
    Esperanza_saludable.insert_many(dict_esp_salu).execute()
    
    db.close()"""




#Api Front

#Devuelve una lista con la lista de los paises y un dataframe con los datos historicos
def data_front():
    try:
        db.connect()
    except:
        pass
    #chequear que los a;os funcionen bien cuando se hacen multiples joins
    data_esperanza = Pais.select(Pais.pais_id,Pais.nombre_EN,Pais.nombre_ESP,Pais.latitud,Pais.longitud,Esperanza.esperanza,Esperanza.year).join(Esperanza,on=(Pais.pais_id == Esperanza.pais_id))
    data_esperanza = pd.DataFrame(data_esperanza.dicts())
    #stddev calc
    data2 = data_esperanza.groupby('pais_id')[['esperanza']].std().sort_values(by='esperanza',ascending=False).reset_index()
    data2 = data2[data2['esperanza']>2.5].head(8)
    lista_paises = data2['pais_id'].values.tolist()
    #querys to df
    data_terciario = Terciario.select(Terciario.pais_id, Terciario.year, Terciario.terciario_completo)
    data_terciario = pd.DataFrame(data_terciario.dicts())
    data_esperanza_saludable = Esperanza_saludable.select(Esperanza_saludable.pais_id,Esperanza_saludable.year, Esperanza_saludable.esp_vida_salud_60)
    data_esperanza_saludable = pd.DataFrame(data_esperanza_saludable.dicts())
    data_credito_privado = Economia.select(Economia.pais_id, Economia.year, Economia.credito_al_sector_privado)
    data_credito_privado = pd.DataFrame(data_credito_privado.dicts())
    data_riesgo_pobreza = Economia.select(Economia.pais_id,Economia.year,Economia.riesgo_empobrecimiento_salud)
    data_riesgo_pobreza = pd.DataFrame(data_riesgo_pobreza.dicts())
    #filtro
    bool_esp = data_esperanza['pais_id'].isin(lista_paises)
    bool_terc = data_terciario['pais_id'].isin(lista_paises)
    bool_esp_sal = data_esperanza_saludable['pais_id'].isin(lista_paises)
    bool_cred_priv = data_credito_privado['pais_id'].isin(lista_paises)
    bool_riesgo_pob = data_riesgo_pobreza['pais_id'].isin(lista_paises)
    data_esperanza = data_esperanza[bool_esp]
    data_terciario = data_terciario[bool_terc]
    data_esperanza_saludable = data_esperanza_saludable[bool_esp_sal]
    data_credito_privado = data_credito_privado[bool_cred_priv]
    data_riesgo_pobreza = data_riesgo_pobreza[bool_riesgo_pob]
    #Preparacion diccionario
    base = data_esperanza.drop(['esperanza','year'],axis=1).groupby('pais_id')
    base = base.first().reset_index().to_dict(orient='index')
    for i in base:
        datax = base[i]['pais_id']
        #Filtro
        filt_esp = data_esperanza['pais_id'] == datax
        filt_terc = data_terciario['pais_id'] == datax
        filt_esp_sal = data_esperanza_saludable['pais_id'] == datax
        filt_cred_priv = data_credito_privado['pais_id'] == datax
        ######filt_risk = data_riesgo_pobreza['pais_id'] = datax
        df_esp = data_esperanza[filt_esp].reset_index(drop=True)
        df_terc = data_terciario[filt_terc].reset_index(drop=True)
        df_esp_sal = data_esperanza_saludable[filt_esp_sal].reset_index(drop=True)
        df_cred_priv = data_credito_privado[filt_cred_priv].reset_index(drop=True)
        #####df_risk = data_credito_privado[filt_risk].reset_index(drop=True)
        #Agregado de valores al diccionario
        keys_esp = df_esp['year'].values
        keys_terc = df_terc['year'].values
        keys_esp_sal = df_esp_sal['year'].values
        keys_cred_priv = df_cred_priv['year'].values
        vals_esp = df_esp['esperanza'].values
        vals_terc = df_terc['terciario_completo'].values
        vals_esp_sal = df_esp_sal['esp_vida_salud_60'].values
        vals_cred_priv = df_cred_priv['credito_al_sector_privado'].values

        if base[i]['pais_id'] == df_esp['pais_id'][0]:
            dict_esp = dict(zip(keys_esp,vals_esp))
            base[i]["esperanza"] = dict_esp
            dict_terc = dict(zip(keys_terc,vals_terc))
            base[i]["terciario"] = dict_terc
            dict_esp_sal = dict(zip(keys_esp_sal,vals_esp_sal))
            base[i]["esperanza_saludable"] = dict_esp_sal
            dict_cred_priv = dict(zip(keys_cred_priv,vals_cred_priv))
            base[i]["credito_privado"] = dict_cred_priv
    db.close()
    return base
