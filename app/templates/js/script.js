//primer parte

const nan = "---"
const paises = {{ data | safe }}


var markers = [];

for (i in paises) {
  markers.push({ name: paises[i]['nombre_EN'], coords: [paises[i]['latitud'], paises[i]['longitud']] })
}

var mierda = {
  {{data[0]['pais_id']}}:{{data[0]['esperanza'][1990]}},
  {{data[1]['pais_id']}}:{{data[1]['esperanza'][1990]}},
  {{data[2]['pais_id']}}:{{data[2]['esperanza'][1990]}},
  {{data[3]['pais_id']}}:{{data[3]['esperanza'][1990]}},
  {{data[4]['pais_id']}}:{{data[4]['esperanza'][1990]}},
  {{data[5]['pais_id']}}:{{data[5]['esperanza'][1990]}},
  {{data[6]['pais_id']}}:{{data[6]['esperanza'][1990]}},
  {{data[7]['pais_id']}}:{{data[7]['esperanza'][1990]}},
  }

var map = new jsVectorMap({
  selector: "#map",
  map: "world",
  regionStyle: {
      initial: {
          fill: '#d1d4db'
      }
  },

  visualizeData: {
      scale: ['#DEE007', '#3EBB01'],
      values: mierda
  },
  labels: {
      markers: {
          render: (marker) => marker.name
      }
  },
  markers: markers,
  markersSelectable: true,
  selectedMarkers: markers.map((marker, index) => {
      var name = marker.name;
      if (name === "Russia" || name === "Brazil") {
          return index;
      }
  }),
  markerLabelStyle: {
      initial: {
          fontFamily: "Roboto",
          fontWeight: 700,
          fontSize: 22,
          backgroundColor: 'red'
      }
  },

});




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

map.extend("reloadWith", function (newParams) {
  this.reset();

  // Remove old regions from DOM then empty the object
  Object.keys(this.regions).forEach((key) => {
      const el = this.regions[key].element.shape.node;
      el.parentElement.removeChild(el);
  });
  this.regions = {};

  // Overwrite the old params with the new params
  Object.keys(newParams).forEach((key) => {
      this.params[key] = newParams[key];
  });

  this._createRegions();
  this.updateSize();
  this._createMarkers(this.params.markers);
  this._repositionLabels();
  this._setupElementEvents()
  // "jvm-series-container jvm-series-h"
  // "jvm-series-container jvm-series-v"
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


document.querySelector("#focus2").addEventListener("click", () => {
  map.reloadWith({
      markers: markers,
      regionStyle: {
          initial: { fill: "#d1d5db" }
      },
      series: {
          markers: [
              {
                  attribute: "fill",
                  legend: {
                      title: "Something (marker)"
                  },
                  scale: {
                      mScale1: "#ffc371",
                      mScale2: "#c79efd"
                  },
                  values: {
                      // Notice: the key must be a number of the marker.
                      0: "mScale1",
                      1: "mScale2",
                      2: "mScale2"
                  }
              }
          ]
      },
      visualizeData: { 
          scale: ['#DEE007', '#3EBB01'],
          values :mierda
      }
  });
});

document.querySelector("#focus").addEventListener("click", () => {
  map.reloadWith({
      markers: [
          { name: "Brazil", coords: [-14.235, -51.9253] },
          { name: "Norway", coords: [60.472, 8.4689] },
          { name: "China", coords: [35.8617, 104.1954] },
          { name: "United States", coords: [37.0902, -95.7129] },
          { name: "Egypt", coords: [26.8206, 30.8025] }
      ],
      regionStyle: {
          initial: { fill: "#d1d5db" }
      },
      series: {
          markers: [
              {
                  attribute: "fill",
                  legend: {
                      title: "Something (marker)"
                  },
                  scale: {
                      mScale1: "#ffc371",
                      mScale2: "#c79efd"
                  },
                  values: {
                      // Notice: the key must be a number of the marker.
                      0: "mScale1",
                      1: "mScale2",
                      2: "mScale2"
                  }
              }
          ]
      },
      visualizeData: { 
          scale: ['#DEE007', '#3EBB01'],
          values :{
              BR: 42.08279,
              ID: 0,
              IN: 24.916456,
              KR: 50.774,
              PT: 0,
              RU: 0,
              TR: 0,
              ZA: 71.9382,
          }
      }
  });
});


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
const $li0 = document.getElementById('pais0')
const $li1 = document.getElementById('pais1')
const $li2 = document.getElementById('pais2')
const $li3 = document.getElementById('pais3')
const $li4 = document.getElementById('pais4')
const $li5 = document.getElementById('pais5')
const $li6 = document.getElementById('pais6')
const $li7 = document.getElementById('pais7')

const $i0 = document.getElementById('s0')
const $i1 = document.getElementById('s1')
const $i2 = document.getElementById('s2')
const $i3 = document.getElementById('s3')
const $i4 = document.getElementById('s4')
const $i5 = document.getElementById('s5')
const $i6 = document.getElementById('s6')
const $i7 = document.getElementById('s7')

var onLoaderino = 1;

var alfa_0,alfa_1,alfa_2,alfa_3,alfa_4,alfa_5,alfa_6,alfa_7;

const yearMetric = () => {
  const indexMetrica = $select.selectedIndex;
  var metrica;
  if(indexMetrica == 0){
    metrica = 'esperanza'
  }else if(indexMetrica == 1){
    metrica = 'credito_privado'
  }else if(indexMetrica == 2){
    metrica = 'Metrica 3'
  }

  var valorYear = $year.value;
  valorYear = valorYear.toString()
  const seleccionFinal = "Metrica:" + metrica[0].toUpperCase()+metrica.substring(1)
  $dataTitle.innerText = seleccionFinal
  $dataYear.innerText = valorYear

  $i0.innerText = paises[0]['nombre_ESP']
  $i1.innerText = paises[1]['nombre_ESP']
  $i2.innerText = paises[2]['nombre_ESP']
  $i3.innerText = paises[3]['nombre_ESP']
  $i4.innerText = paises[4]['nombre_ESP']
  $i5.innerText = paises[5]['nombre_ESP']
  $i6.innerText = paises[6]['nombre_ESP']
  $i7.innerText = paises[7]['nombre_ESP']

  $li0.innerText = paises[0][metrica][valorYear]
  $li1.innerText = paises[1][metrica][valorYear]
  $li2.innerText = paises[2][metrica][valorYear]
  $li3.innerText = paises[3][metrica][valorYear]
  $li4.innerText = paises[4][metrica][valorYear]
  $li5.innerText = paises[5][metrica][valorYear]
  $li6.innerText = paises[6][metrica][valorYear]
  $li7.innerText = paises[7][metrica][valorYear]


  if(onLoaderino == 0){
    console.log(onLoaderino)
    map.reloadWith({
      markers: markers,
      regionStyle: {
          initial: { fill: "#d1d5db" }
      },
      series: {
          markers: [
              {
                  attribute: "fill",
                  legend: {
                      title: "Something (marker)"
                  },
                  scale: {
                      mScale1: "#ffc371",
                      mScale2: "#c79efd"
                  },
                  values: {
                      // Notice: the key must be a number of the marker.
                      0: "mScale1",
                      1: "mScale2",
                      2: "mScale2"
                  }
              }
          ]
      },
      visualizeData: { 
          scale: ['#DEE007', '#3EBB01'],
          values :{
              [paises[0]['pais_id']]: [paises[0][metrica][valorYear]],
              [paises[1]['pais_id']]: [paises[1][metrica][valorYear]],
              [paises[2]['pais_id']]: [paises[2][metrica][valorYear]],
              [paises[3]['pais_id']]: [paises[3][metrica][valorYear]],
              [paises[4]['pais_id']]: [paises[4][metrica][valorYear]],
              [paises[5]['pais_id']]: [paises[5][metrica][valorYear]],
              [paises[6]['pais_id']]: [paises[6][metrica][valorYear]],
              [paises[7]['pais_id']]: [paises[7][metrica][valorYear]],
          }
      }  
  },);
    dataMap = {
      {{data[0]['pais_id']}}:{{data[0]['esperanza'][1990]}},
      {{data[1]['pais_id']}}:{{data[1]['esperanza'][1990]}},
      {{data[2]['pais_id']}}:{{data[2]['esperanza'][1990]}},
      {{data[3]['pais_id']}}:{{data[3]['esperanza'][1990]}},
      {{data[4]['pais_id']}}:{{data[4]['esperanza'][1990]}},
      {{data[5]['pais_id']}}:{{data[5]['esperanza'][1990]}},
      {{data[6]['pais_id']}}:{{data[6]['esperanza'][1990]}},
      {{data[7]['pais_id']}}:{{data[7]['esperanza'][1990]}},
      }

      
  }
  
  onLoaderino = 0,
      console.log(onLoaderino)


  // Seteo del mapa
 
}

yearMetric()

$select.addEventListener("change", yearMetric);
$year.addEventListener("change", yearMetric)
