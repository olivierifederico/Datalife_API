#Importacion de librerias
from fastapi import FastAPI
from connector import get_tables
#Instanciar FastApi
app = FastAPI()

#Decoradores
@app.get("/")
async def defecto():
    return "Datalife API"

@app.get("/tablas")
async def tablas():
    return get_tables()

