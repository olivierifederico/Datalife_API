//primer parte

const nan = "---"
const paises = {{ data | safe }}

console.log(paises)

var markers = [];

for (i in paises) {
  markers.push({ name: paises[i]['nombre_EN'], coords: [paises[i]['latitud'], paises[i]['longitud']] })
}



var map = new jsVectorMap({
  selector: "#map",
  map: "world",
  regionStyle: {
    initial: {
      fill: '#d1d4db'
    }
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
  series: {
    markers: [{
      attribute: 'image',
      legend: {
        title: 'Some title!',
        vertical: true
      },
      scale: {
        marker1title: {
          url: 'https://picsum.photos/200',
          offset: [10, 300]
        },
        marker2title: {
          url: 'https://picsum.photos/200',
          offset: [0, 0]
        }
      },
      values: {
        0: 'marker1title',
        1: 'marker2title',
        2: 'marker2title',
        3: 'marker1title',
      }
    }],
    regions: [{
      attribute: 'fill',
      legend: {
        title: 'Something',
      },
      scale: {
        scale1: 'yellow',
        scale2: 'dodgerblue',
        scale3: 'forestgreen',
      },
      values: {
        "{{data[0]['pais_id']}}": 'scale1',
        "{{data[1]['pais_id']}}": 'scale1',
        "{{data[2]['pais_id']}}": 'scale2',
        "{{data[3]['pais_id']}}": 'scale2',
        "{{data[4]['pais_id']}}": 'scale2',
        "{{data[5]['pais_id']}}": 'scale3',
        "{{data[6]['pais_id']}}": 'scale3',
        "{{data[7]['pais_id']}}": 'scale3',
      }
    }]
  }
});


//segunda parte
{% for i in data %}
document.querySelector('#{{data[i]["pais_id"]}}').addEventListener('click', () => {
  map.setFocus({ region: '{{data[i]["pais_id"]}}', animate: true })
})
{% endfor %}



const $mapTitle = document.getElementById('mapTitle');
const $select = document.querySelector("#metrica");
const $dataTitle = document.getElementById('dataTitle');
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
}

yearMetric()

$select.addEventListener("change", yearMetric);
$year.addEventListener("change", yearMetric)

window.addEventListener('resize', () => {
  map.updateSize()
})