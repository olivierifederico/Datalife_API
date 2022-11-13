/* Input desde Python.
 
Diccionario que contiene un diccionario por cada pais,
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

*/
const nan = "--" // Correcion de valores faltantes.
const pais = {{data|safe}}




// Carga de valores default.
var markers = [];
var dataViz_default = {}
for (i in pais) {
  markers.push({ name: pais[i]['nombre_ESP'], coords: [pais[i]['latitud'], pais[i]['longitud']] })
  dataViz_default[pais[i]['pais_id']] = pais[i]['esperanza'][1990]
}


/*
Mapa
- Creacion de mapa inicial.
- Funcion necesaria para el reload del mapa.
- Funcion reload mapa.
*/

// Mapa Inicial.
var map = new jsVectorMap({
  selector: "#map",
  map: "world",
  backgroundColor : 'whitesmoke',
  regionStyle: {
      initial: {
          fill: '#9FB5B5'
      }
  },
  
  /*
  Escala de colores
  - Valores Default cargados previamente en "dataViz_default".
  */

  visualizeData: {
      scale: ['#F48C01', '#21D900'],
      values: dataViz_default
  },

  /*
    Marcadores
    - Nombre del pais.
    - Coordenadas cargadas previamente en "markers".
    - No son seleccionables.
    - Estilo del marcador.
  */

  // Nombre
  labels: {
      markers: {
          render: (marker) => marker.name
      }
  },
  // Coordenadas
  markers: markers,
  // No seleccionable
  markersSelectable: false,
  // Estilo
  markerLabelStyle: {
      initial: {
          fontFamily: "Roboto",
          fontWeight: 700,
          fontSize: 22,
          backgroundColor: 'red'
      }
  },
});

// Pre Reload Mapa.
H = (function () {
      function t(t, e) {
          var i = t.scale,
              s = t.values;
          (this._scale = i), (this._values = s), (this._fromColor = this.hexToRgb(i[0])), (this._toColor = this.hexToRgb(i[1])), (this._map = e), this.setMinMaxValues(s), this.visualize();
      }
      var e = t.prototype;
      return (
          (e.setMinMaxValues = function (t) {
              for (var e in ((this.min = Number.MAX_VALUE), (this.max = 0), t)) (e = parseFloat(t[e])) > this.max && (this.max = e), e < this.min && (this.min = e);
          }),
          (e.visualize = function () {
              var t,
                  e = {};
              for (var i in this._values) (t = parseFloat(this._values[i])), isNaN(t) || (e[i] = this.getValue(t));
              this.setAttributes(e);
          }),
          (e.setAttributes = function (t) {
              for (var e in t) this._map.regions[e] && this._map.regions[e].element.setStyle("fill", t[e]);
          }),
          (e.getValue = function (t) {
              for (var e, i = "#", s = 0; s < 3; s++) i += (1 === (e = Math.round(this._fromColor[s] + (this._toColor[s] - this._fromColor[s]) * ((t - this.min) / (this.max - this.min))).toString(16)).length ? "0" : "") + e;
              return i;
          }),
          (e.hexToRgb = function (t) {
              var e = 0,
                  i = 0,
                  s = 0;
              return (
                  4 == t.length ? ((e = "0x" + t[1] + t[1]), (i = "0x" + t[2] + t[2]), (s = "0x" + t[3] + t[3])) : 7 == t.length && ((e = "0x" + t[1] + t[2]), (i = "0x" + t[3] + t[4]), (s = "0x" + t[5] + t[6])),
                  [parseInt(e), parseInt(i), parseInt(s)]
              );
          }),
          t
      );
  })(),

//Funcion Reload utilizando .extend
map.extend("reloadWith", function (newParams) {
  this.reset();

  Object.keys(this.regions).forEach((key) => {
      const el = this.regions[key].element.shape.node;
      el.parentElement.removeChild(el);
  });
  this.regions = {};

  Object.keys(newParams).forEach((key) => {
      this.params[key] = newParams[key];
  });

  // Lamado a funciones que se utilizan para inicializar el mapa
  this._createRegions();
  this.updateSize();
  this._createMarkers(this.params.markers);
  this._repositionLabels();
  this._setupElementEvents()

  //Visualizacion escala de colores
  this.params.visualizeData && (this.dataVisualization = new H(this.params.visualizeData, this))

  const legendHorizontal = document.createElement("div");
  const legendVertical = document.createElement("div");

  legendHorizontal.setAttribute("class", "jvm-series-h");
  legendVertical.setAttribute("class", "jvm-series-v");

  this.legendHorizontal = legendHorizontal;
  this.legendVertical = legendVertical;

  if (this.params.series) {
      this.container.appendChild(this.legendHorizontal);
      this.container.appendChild(this.legendVertical);
      this._createSeries();
  }
});


numero = 0

// Bucle de jinja 
{% for i in data %}
document.querySelector('#{{data[i]["pais_id"]}}').addEventListener('click', () => {
map.setFocus({ region: '{{data[i]["pais_id"]}}', animate: true })
})
{% endfor %}


const $mapTitle = document.getElementById('mapTitle');
const $select = document.querySelector("#metrica");
const $dataTitle = document.getElementById('dataTitle');
const $dataYear = document.getElementById('dataYear')
const $year = document.querySelector('#year')



// Se guardan los elementos en 2 listas, una de los paises y otro del valor de la metrica.

var numero = 0
var $li = []
var $i = []
for (i in pais) {
    $li[numero] = document.getElementById('pais'+numero)
    $i[numero] = document.getElementById('s'+numero)
    numero++
}




/*
Funcion que se ejecuta para mostrar los datos de las metricas.
- Se obtiene la metrica y el anno
- Carga de datos en las listas del html
- Visualizacion de colores post init del mapa.

*/

// 
var onLoaderino = 1;

const yearMetric = () => {
// metrica
  const indexMetrica = $select.selectedIndex;
  var metrica;
  if(indexMetrica == 0){
    metrica = 'esperanza'
  }else if(indexMetrica == 1){
    metrica = 'credito_privado'
  }else if(indexMetrica == 2){
    metrica = 'terciario'
  }else if(indexMetrica == 3){
    metrica = 'esperanza_saludable'
  }
// anno
  var valorYear = $year.value;
// conversion para el titulo de la metrica
  valorYear = valorYear.toString()
  const seleccionFinal = "Metrica:" + metrica[0].toUpperCase()+metrica.substring(1)
  $dataTitle.innerText = seleccionFinal
  $dataYear.innerText = valorYear

// carga de datos en las listas 
  numero = 0
  for (i in $i){
    $i[i].innerText = pais[numero]['nombre_ESP']
    $li[i].innerText = pais[numero][metrica][valorYear]
    numero++
  }

/* 
Despues de la inicializacion del mapa
esta parte permite la visualizacion de colores
cada vez que hay algun cambio en un selector.

*/
  if(onLoaderino == 0){
    dataViz = {}
    for (i in pais){
        dataViz[pais[i]['pais_id']] = pais[i][metrica][valorYear]
    }


    map.reloadWith({
      markers: markers,
      markersSelectable: false,
      backgroundColor : 'whitesmoke',
      regionStyle: {
          initial: { fill: "#9FB5B5" }
      },
      series: {
        markers: [
            {
                attribute: "fill",
                legend: {
                    title: "Something (marker)"
                },
                scale: {
                    mScale1: "#2D2D2D",
                    mScale2: "#2D2D2D"
                },
                values: {
                    0: "mScale1",
                    1: "mScale2",
                    2: "mScale2"
                }
            }
        ]
    },
      visualizeData: { 
        scale: ['#F48C01', '#21D900'],
          values :dataViz
      }  
  },);
    dataMap = dataViz_default
  }
  
  onLoaderino = 0


  // Seteo del mapa
 
}

yearMetric()


// Listeners de los selectores que ejecutan la funcion "yearMetric()"
$select.addEventListener("change", yearMetric);
$year.addEventListener("change", yearMetric)
