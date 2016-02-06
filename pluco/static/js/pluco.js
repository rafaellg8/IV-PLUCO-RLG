$(function(){
  /** Aumentar o disminuir tamaño de fuente **/
  $("#aumentar").click( function() {
    var fontSize = parseInt($("body").css("font-size"));
    fontSize = fontSize + 4 + "px";
    $('body').css({'font-size':fontSize});
  });

  $("#disminuir").click( function() {
    var fontSize = parseInt($("body").css("font-size"));
    fontSize = fontSize - 4 + "px";
    $("body").css({'font-size':fontSize});
  });

  $("#reiniciar").click( function() {
  /*Recargamos la página*/
  location.reload();
  });


  /*--------------------------------------
  Aumentar las visitas
  ---------------------------------------*/


  /* --------------------------------------

  Obtener datos y mostar barra de visitas

  --------------------------------------*/

  $.ajax({
  url: "/foros/reclama_datos",
  type: 'get',
  success: function(datos) {
   console.log (datos.visits);
   console.log(datos.theme);
    Visualiza_datos(datos);
  },
  failure: function(datos) {
    alert('esto no vá');
  }
});


  function Visualiza_datos (datos) {

    $('#container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Número visitas'
        },
        xAxis: {
            categories: datos.theme
        },
        yAxis: {
            title: {
                text: 'Temas'
            }
        },
        series: [{
            name: 'visitas',
            data: datos.visits
        }]
    });
  }
});
