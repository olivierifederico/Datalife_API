# Eleccion del contenedor de FastApi

FROM tiangolo/uvicorn-gunicorn-fastapi

# Ejecucion de comandos para instalar los modulos necesarios.
RUN pip install peewee
RUN pip install psycopg2-binary
RUN pip install fastapi-login
RUN pip install python-multipart
RUN pip install wbgapi
RUN pip install pandas

# Exposicion del puerto 80
EXPOSE 80

# Copiado de archivos al contenedor
COPY ./app /app