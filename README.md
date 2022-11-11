<h1>Datalife - API - Mapa Interactivo</h1>

![Mapa Interactivo](/_src/map.png)


[Link al mapa](https://datalifeapipri-prod-datalife-svspeu.mo5.mogenius.io/)
---

---
<p>Cree un mapa interactivo el cual esta conectado a una base de datos en el cual se pueden ver como los paises fueron evolucionando en el tiempo en diferentes aspectos.</p>
<p>Teniendo en cuenta que para tener acceso a los datos se requiere un conocimiento basico de SQL, decidi crear una interfaz que sea amigable con la mayoria de los usuarios con solo conectarse a la API.</p>

<h2>Desarrollo</h2>

---

<h2>Tecnologias utilizadas:</h2>

- Python
- FastApi
- PostgeSQL
- Docker
- HTML
- CSS
- JavaScript

---
<h3>Back</h3>

<p>El servidor en la nube que utilice fue <b>Mogenius</b>.</p>

<p>El despliegue y la conexion entre los contenedores de la <b>API</b> y de <b>postgreSQL</b> los hice de manera individual ya que el servidor <b>no soporta docker-compose</b>.</p>

<p>Conecte este repositorio con el servidor. Esto hace que lea el archivo  <b>Dockerfile</b>, cree la imagen de <b>Docker</b>, y haga el despliegue del contenedor automaticamente cada vez que hago alguna modificacion en el repositorio.</p>

<p>Cree un archivo <b>Dockerfile</b> donde utilizo la imagen <b>tiangolo/uvicorn-gunicorn-fastapi</b>.</p>

<p>La conexion con el contenedor de la base de datos la hice en <b>Python</b> utilizando la libreria <b>Peewee</b>.</p>

<p>Guarde los datos en un <b>DataFrame</b> de <b>Pandas</b>.</p>

<p>De todos los paises tome solo los 8 paises que tengan mayor desviacion estandar(esperanza de vida) y esta sea mayor a 2.5.</p>

<p>Aplique los filtros necesarios y guarde solo las metricas seleccionadas.</p>

<p>Converti el <b>DataFrame</b> en un <b>diccionario</b> para poder procesar los datos posteriormente con <b>Jinja2</b>.</p>

<p>Cree la <b>API</b> con la libreria <b>FastApi</b></p>

---

<h3>Back to Front</h3>
<p>Utilizando <b>StaticFiles</b> programe que al acceder a la <b>API</b> devuelva los archivos <b>HTML</b> y <b>CSS</b></p> 

<p>Junto con los archivos de <b>StaticFiles</b> la <b>API</b> devuelve un archivo <b>JavaScript</b> el cual previamente fue procesado por la libreria <b>Jinja2</b>, utilizando los templates hice la conexion Back-Front y envie el <b>diccionario</b> con todos los datos al front</p>

---

<h3>Front</h3>
<p>Para armar el mapa interactivo utilice la libreria <b>Jsvectormap</b> de <b>JavaScript</b>.</p>

<p>Configure 8 botones que</p>

<p>Configure una escala de colores, la cual se aplica acorde al valor de la metrica en cada pais, pintandolo del color correspondiente.</p>

<p>Cree 2 selectores, uno para los años y otro para las metricas.</p>

<p><b>No tenia una funcion que permitiera actualizar el mapa cuando habia algun cambio en algun selector</b> y en la documentacion <b>tampoco habia informacion</b>.</p>

<p>Lo que me dejo entre 2 opciones:</p>

- Buscar una libreria nueva.

- Crear mi propia funcion.


 <p>Teniendo en cuenta que la fecha de entrega era en 2 dias decidi investigar el funcionamiento del script.</p>

 <p>Cree una funcion que reutiliza algunas partes con las que se inicializa el mapa, lo que me permitio pasarle los valores de las metricas para que los paises cambien de color y en caso de no que haya valores faltantes en algun pais, este se mantenga de color gris.</p>

---

<h2>Proximas actualizaciones:</h2>

- Optimizar el codigo. - 75% listo.
- Mejorar la documentacion.
- Agregar mas metricas.
- Agregar predicciones.
- Agregar datos generales al hover de cada pais.
- Mobile First.
- Mejorar el diseño para facilitar su uso.



