#Importacion de librerias
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from connector import get_tables
from database import create_tables,get_coordinates,get_countrystdv

#Instanciar FastApi

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#Decoradores

@app.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse('index.html',{
        "request":request,
        'data':get_countrystdv()})

@app.get("/tablas")
async def tablas():
    return get_tables()

@app.get("/crear_tablas")
async def crear_tablas():
    create_tables()
    return {"Creacion":"Tablas",
            "Tablas":get_tables()}


