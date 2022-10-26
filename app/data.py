import wbgapi as wb
import pandas as pd
# Lista de paises

paises = ['USA','GBR','ITA','FRA','DEU','JPN','CAN','RUS','ARG','AUS','BRA','CHN','IND','MEX','IDN','KOR','SAU','ZAF','TUR','ESP','NOR',
'URY','ARE','SWE','PRT','NZL','GRC','CHL','NLD','ISL']

# Import
pais_data = pd.read_csv('../csv/paisesalfa2.csv')

#Renombro columnas
pais_data.rename(columns={'alfa2':'pais_id','nombre_espanol': 'nombre_ESP', 'nombre_ingles':'nombre_EN', 'alfa3': 'codigo_pais'}, inplace=True)
# Capitalizar columa nombre_ESP
pais_data.nombre_ESP = pais_data.nombre_ESP.str.title()
dict_pais = pais_data.to_dict('records')
dict_pais
# Esperanza de vida 
esperanza_de_vida = wb.data.DataFrame(["SP.DYN.LE00.IN"],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')

esperanza_de_vida.columns = ["Esperanza de Vida"]

esperanza_de_vida.reset_index(inplace=True)

esperanza_de_vida["id"] = esperanza_de_vida.index
esperanza_de_vida

esperanza_de_vida.rename(columns={'economy':'pais_id', 'time':'year','Esperanza de Vida':'esperanza'}, inplace=True)
esperanza_de_vida = esperanza_de_vida[['id', 'pais_id', 'year', 'esperanza']]
esperanza_de_vida


esperanza_de_vida.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)


dict_esperanza = esperanza_de_vida.to_dict('records')


# Salud

salud = wb.data.DataFrame(['SH.XPD.GHED.GD.ZS'],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')

salud.columns = ["Gasto Publico En Salud % PBI"]

salud.reset_index(inplace=True)
salud["id"] = salud.index


salud.rename(columns={'economy':'pais_id', 'time':'year','Gasto Publico En Salud % PBI'
:'gasto_salud'}, inplace=True)
salud = salud[['id', 'pais_id', 'year', 'gasto_salud']]

salud.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)


dict_salud = salud.to_dict('records')
dict_salud


# Esperanza por genero

esperanza_de_vida_gen = wb.data.DataFrame(["SP.DYN.LE00.FE.IN","SP.DYN.LE00.MA.IN" ],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')

esperanza_de_vida_gen.columns = ["esperanza_fem", 'esperanza_mas']

esperanza_de_vida_gen.reset_index(inplace=True)
esperanza_de_vida_gen["id"] = esperanza_de_vida_gen.index
esperanza_de_vida_gen.rename(columns={'economy':'pais_id', 'time':'year'}, inplace=True)
esperanza_de_vida_gen = esperanza_de_vida_gen[['id', 'pais_id', 'year', 'esperanza_fem', 'esperanza_mas']]

esperanza_de_vida_gen.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)

dict_esperanza_gen = esperanza_de_vida_gen.to_dict('records')
dict_esperanza_gen


# Educacion

educacion = wb.data.DataFrame(['SE.XPD.TOTL.GD.ZS'],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')

educacion.columns = ["gasto_educacion"]

educacion.reset_index(inplace=True)

educacion["id"] = educacion.index
educacion.rename(columns={'economy':'pais_id', 'time':'year'}, inplace=True)
educacion = educacion[['id', 'pais_id', 'year', 'gasto_educacion']]


educacion.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)



dict_educacion = educacion.to_dict('records')
dict_educacion

# Economia 
economia = wb.data.DataFrame(["FP.CPI.TOTL.ZG","NY.GDP.PCAP.KD.ZG", 'FS.AST.PRVT.GD.ZS', 'SP.POP.GROW','SH.SGR.IRSK.ZS'],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')

economia.columns = ["inflacion",'credito_al_sector_privado',"crecimiento_per_capita_Bruto",'riesgo_empobrecimiento_salud', 'cremiento_pob']

economia.reset_index(inplace=True)


economia["id"] = economia.index


economia.rename(columns={'economy':'pais_id', 'time':'year'}, inplace=True)
economia = economia[['id', 'pais_id', 'year', "inflacion",'credito_al_sector_privado',"crecimiento_per_capita_Bruto",'riesgo_empobrecimiento_salud', 'cremiento_pob']
]

economia.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)



dict_economia = economia.to_dict('records')
dict_economia

# Ambiente

ambiente = wb.data.DataFrame(['EN.ATM.PM25.MC.ZS'],
paises,numericTimeKeys=True,time=range(1990,2020),columns='series')


ambiente.columns = ["exposcion_contaminacion"]

ambiente.reset_index(inplace=True)

ambiente["id"] = ambiente.index

ambiente.rename(columns={'economy':'pais_id', 'time':'year'}, inplace=True)
ambiente = ambiente[['id', 'pais_id', 'year', 'exposcion_contaminacion']]


ambiente.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)


dict_ambiente = ambiente.to_dict('records')
dict_ambiente


# Terciario

terciario = pd.read_csv('../csv/Terciario.csv')
terciario.rename(columns={'Code':'pais_id','Year':'year'}, inplace=True)

terciario.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)

dict_terciario = terciario.to_dict('records')

dict_terciario


# Esperanza de vida saludable
esp_salud = pd.read_csv('../csv/esp_salud.csv')
esp_salud
esp_salud.replace({
    'pais_id': {'USA': 'US',
        'GBR':'GB',
        'ITA':'IT',
        'FRA': 'FR',
        'DEU':'DE',
        'JPN':'JP',
        'CAN': 'CA',
        'RUS': 'RU',
        'ARG':'AR',
        'AUS':'AU',
        'BRA': 'BR',
        'CHN': 'CN',
        'IND': 'IN',
        'MEX':'MX',
        'IDN':'ID',
        'KOR':'KR',
        'SAU':'SA',
        'ZAF': 'ZA',
        'TUR': 'TR',
        'ESP': 'ES',
        'NOR':'NO',
        'URY':'UY',
        'ARE':'AE',
        'SWE':'SE',
        'PRT':'PT',
        'NZL':'NZ',
        'GRC': 'GR',
        'CHL': 'CL',
        'NLD': 'NL',
        'ISL': 'IS'

        
    }
}, inplace= True)
dict_esp_salu = esp_salud.to_dict('records')

dict_esp_salu

