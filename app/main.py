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
    data = get_countrystdv()
    return templates.TemplateResponse('index.html',{
        "request":request,
        'pais0':data[0][0],
        'pais1':data[0][1],
        'pais2':data[0][2],
        'pais3':data[0][3],
        'pais4':data[0][4],
        'pais5':data[0][5],
        'pais6':data[0][6],
        'pais7':data[0][7]})

@app.get("/tablas")
async def tablas():
    return get_tables()

@app.get("/crear_tablas")
async def crear_tablas():
    create_tables()
    return {"Creacion":"Tablas",
            "Tablas":get_tables()}


