//primer parte
var map = new jsVectorMap({
  selector: "#map",
  map: "world",
  regionStyle: {
    initial: {
      fill: '#d1d4db'
    }
  },
  onRegionSelected: function (index, isSelected, selectedRegions) {
    console.log(index, isSelected, selectedRegions);
  },
  onMarkerSelected: function (code, isSelected, selectedMarkers) {
    console.log(code, isSelected, selectedMarkers)
  },
  onRegionTooltipShow: function (event, tooltip, code) {
    if (code === 'RU') {
      tooltip.getElement().innerHTML = tooltip.text() + ' <b>(Hello Russia)</b>'
    }
  },
  onMarkerTooltipShow: function (event, tooltip, index) {
    tooltip.getElement().innerHTML = '<h5 class="mb-0">' + tooltip.text() + '</h5>' + '<p class="mb-0">Lorem ipsum dolor sit amet consectetur adipisicing elit.</p><small class="mb-0">Lorem ipsum dolor sit amet consectetur adipisicing elit.</small>'
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
          url: '../assets/images/marker.png',
          offset: [10, 0]
        },
        marker2title: {
          url: '../assets/images/marker2.png',
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


const $mapTitle = document.getElementById('mapTitle')

const $select = document.querySelector("#metrica")

const cambioMetrica = () => {
  console.log($select.selectedIndex);
  if ($select.selectedIndex == 0) {
    console.log('Esperanza de vida perro');
    $mapTitle.innerText = "Esperanza de vida";
  } else if ($select.selectedIndex == 1) {
    console.log('Metrica 2');
    $mapTitle.innerText = "Metrica 2";
  }
};


$select.addEventListener("change", cambioMetrica);