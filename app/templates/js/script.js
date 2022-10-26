//primer parte

var markers = [
{% for i in data %}
{ name: "{{data[i]['nombre_EN']}}", coords: ["{{data[i]['latitud']}}", "{{data[i]['longitud']}}"] },
{% endfor %}
];

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
  markers : markers,
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

const yearMetric = () => {
  const indexMetrica = $select.selectedIndex;
  const valorYear = $year.value;
  const seleccionFinal = "Metrica seleccionada:"+indexMetrica+" del a;o:"+valorYear
  $dataTitle.innerText = seleccionFinal
}

const cambioMetrica = () => {
  console.log($select.selectedIndex);
  if ($select.selectedIndex == 0) {
    console.log('Esperanza de vida perro');
    $mapTitle.innerText = "Esperanza de vida";
    $dataTitle.innerText = 'Esperanza de vida';
  } else if ($select.selectedIndex == 1) {
    console.log('Metrica 2');
    $mapTitle.innerText = "Metrica 2";
    $dataTitle.innerText = 'Metrica 2';
  } else if ($select.selectedIndex == 2){
    console.log('Metrica 3')
    $mapTitle.innerText = "Metrica 3";
    $dataTitle.innerText = 'Metrica 3';
  }
};


$select.addEventListener("change", yearMetric);
$year.addEventListener("change", yearMetric)

window.addEventListener('resize', () => {
  map.updateSize()
})