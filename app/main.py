#Importacion de librerias
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import data_front

#Instanciar FastApi

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#Decoradores

@app.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse('index.html',{
        "request":request,
        'data':data_front()})