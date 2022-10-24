//primer parte
var map = new jsVectorMap({
    selector: "#map",
    map: "world",
    regionStyle: {
      initial: {
        fill: 'grey'
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

const $select = document.querySelector("#metrica")

const cambioMetrica = () => {
  console.log($select.selectedIndex);
  if($select.selectedIndex == 0) {
    console.log('Esperanza de vida perro')
  }
};

$select.addEventListener("change", cambioMetrica);