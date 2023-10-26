// fetch('/consulta/')
//     .then(response => response.json())
//     .then(data => {
//         // 'data' contiene los resultados de la consulta SQL en formato JSON
//         // Puedes procesar los datos y guardarlos en un arreglo para usarlos con Chart.js
//         const results = data.results;
//         // console.log(results)

//         const respuestas = [];
//         const totales = [];

//         for (let i = 0; i < results.length; i++) {
//             respuestas.push(results[i].respuesta);
//             totales.push(results[i].total);
//         }
//         // console.log( respuestas);
//         // console.log( totales);

//             var options = {
//               series: [{
//               data: totales
//             }],
//               chart: {
//               height: 350,
//               type: 'bar',

//             },
//             plotOptions: {
//               bar: {
//                 columnWidth: '45%',
//                 distributed: true,
//               }
//             },
//             dataLabels: { //mostrar el numero dentro de la barra
//               enabled: false
//             },
//             legend: { //mostrar abajo de la grafica los indicadores de cada color
//               show: true
//             },
//             xaxis: {
//               categories: respuestas, 
//               labels: {
//                 style: {
//                   fontSize: '12px'
//                 }
//               }
//             }
//             };
//             var chart = new ApexCharts(document.querySelector('#growthchart'), options);
//             chart.render();


//     })
//     .catch(error => {
//         console.error('Error al obtener los datos:', error);
//     });



var colores = ['#008FFB', '#00E396', '#feb019', '#ff4560', '#775dd0', '#546e7a', '#26a69a', '#d10ce8'];

$.ajax({
  url: '/consulta_respuestas/' + 1 + '/',
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

// fetch('/consulta/')
//     .then(response => response.json())
//     .then(data => {
//         // 'data' contiene los resultados de la consulta SQL en formato JSON
//         // Puedes procesar los datos y guardarlos en un arreglo para usarlos con Chart.js
//         const results = data.results;
//         // console.log(results)

//         const respuestas = [];
//         const totales = [];

//         for (let i = 0; i < results.length; i++) {
//             respuestas.push(results[i].respuesta);
//             totales.push(results[i].total);
//         }
//         // console.log( respuestas);
//         // console.log( totales);

//             var options = {
//               series: [{
//               data: totales
//             }],
//               chart: {
//               height: 350,
//               type: 'bar',

//             },
//             plotOptions: {
//               bar: {
//                 columnWidth: '45%',
//                 distributed: true,
//               }
//             },
//             dataLabels: { //mostrar el numero dentro de la barra
//               enabled: false
//             },
//             legend: { //mostrar abajo de la grafica los indicadores de cada color
//               show: true
//             },
//             xaxis: {
//               categories: respuestas, 
//               labels: {
//                 style: {
//                   fontSize: '12px'
//                 }
//               }
//             }
//             };
//             var chart = new ApexCharts(document.querySelector('#growthchart'), options);
//             chart.render();


//     })
//     .catch(error => {
//         console.error('Error al obtener los datos:', error);
//     });



var colores = ['#008FFB', '#00E396', '#feb019', '#ff4560', '#775dd0', '#546e7a', '#26a69a', '#d10ce8'];

$.ajax({
  url: '/consulta_total',
  dataType: 'json',
  success: function (data) {
    //console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var nuevoTexto = totales[0];

    $("#lblTotalEncuestas").text(nuevoTexto);
    $("#lblTotalEncuestasBar").text(nuevoTexto+' encuestas');
    $("#progressBar").attr('style', 'width: '+nuevoTexto+'%;');
    $("#progressBar").attr('aria-valuenow', nuevoTexto);
    
    
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 1 + '/',
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: [{
        data: totales
      }],
      chart: {
        
        type: 'bar',

      },
      colors: colores,
      plotOptions: {

        bar: {
          columnWidth: '45%',
          borderRadius: 10,
          distributed: true,
        }
      },
      dataLabels: { //mostrar el numero dentro de la barra
        enabled: false
      },
      legend: { //mostrar abajo de la grafica los indicadores de cada color
        show: false
      },
      xaxis: {
        categories: respuestas,
        labels: {
          style: {
            colors: colores,
            fontSize: '12px'
          }
        }
      }
    };
    var chart = new ApexCharts(document.querySelector('#pregunta1'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 2 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }

    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: [{
        data: totales,
      }],
      chart: {
        type: 'bar',
        height: 274
      },
      plotOptions: {
        bar: {
          borderRadius: 10,
          horizontal: true,
        }
      },
      dataLabels: {
        enabled: false
      },
      xaxis: {
        categories: respuestas,
      },
    };
    var chart = new ApexCharts(document.querySelector('#pregunta2'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 3 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];


    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: totales,
      chart: {
        width: 300,
        type: 'donut',
        offsetY: -20,
      },
      dataLabels: {
        enabled: false
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 0
          },
          legend: {
            show: false
          }
        }
      }],
      legend: {
        position: 'bottom', 
        offsetY: 0,
        height: 0,
      },
      labels: respuestas 
    };
    var chart = new ApexCharts(document.querySelector('#pregunta3'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});


$.ajax({
  url: '/consulta_respuestas/' + 4 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data[2])

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }

    const totalp1 = data[0].total;
    const totalp2 = data[1].total;
    const totalp3 = data[2].total;

    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: [{
        data: [totalp1]
      },{
        data: [totalp2]
      },{
        data: [totalp1]
      }],
      chart: {
      type: 'bar',
      height: 430
      
    },
    plotOptions: {
      bar: {
        horizontal: true,
        columnHeight: '45%',
        borderRadius: 10,
        dataLabels: {
          position: 'top',
        },
      }
    },
    dataLabels: {
      enabled: true,
      offsetX: -6,
      style: {
        fontSize: '12px',
        
      }
    },
    stroke: {
      show: true,
      width: 1,
      colors: colores
    },
    tooltip: {
      shared: true,
      intersect: false
    },
    xaxis: {
      categories: respuestas,
    },
    };
    var chart = new ApexCharts(document.querySelector('#pregunta4'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 5 + '/',
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: [{
        data: totales
      }],
      chart: {
        height: 405,
        type: 'bar',

      },
      colors: colores,
      plotOptions: {
        bar: {
          columnWidth: '45%',
          borderRadius: 8,
          distributed: true,
        }
      },
      dataLabels: { //mostrar el numero dentro de la barra
        enabled: false
      },
      legend: { //mostrar abajo de la grafica los indicadores de cada color
        show: false
      },
      xaxis: {
        categories: respuestas,
        labels: {
          style: {
            colors: colores,
            fontSize: '12px'
          }
        }
      }
    };
    var chart = new ApexCharts(document.querySelector('#pregunta5'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 6 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: totales,
      chart: {
        width: 350,
        type: 'pie',
        offsetY: -20,
      },
      labels: respuestas,
      legend: {
        position: 'bottom', 
        horizontalAlign: 'center', 
 
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          },
          legend: {
            position: 'bottom',
            horizontalAlign: 'center' 
          }
        }
      }]
    };
    var chart = new ApexCharts(document.querySelector('#pregunta6'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 7 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: [{
        data: totales
      }],
      chart: {
        height: 350,
        type: 'bar',

      },
      colors: colores,
      plotOptions: {
        bar: {
          columnWidth: '45%',
          borderRadius: 8,
          distributed: true,
        }
      },
      dataLabels: { //mostrar el numero dentro de la barra
        enabled: false
      },
      legend: { //mostrar abajo de la grafica los indicadores de cada color
        show: false
      },
      xaxis: {
        categories: respuestas,
        labels: {
          style: {
            colors: colores,
            fontSize: '12px'
          }
        }
      }
    };
    var chart = new ApexCharts(document.querySelector('#pregunta7'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});

$.ajax({
  url: '/consulta_respuestas/' + 8 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);
    var options = {
      series: totales,
      chart: {
      width: 300,
      offsetY: -20,
      height: 280,
      type: 'polarArea'
    },
    labels: respuestas,
    fill: {
      opacity: 1
    },
    stroke: {
      width: 1,
      colors: undefined
    },
    yaxis: {
      show: false
    },
    legend: {
      position: 'bottom'
    },
    plotOptions: {
      polarArea: {
        rings: {
          strokeWidth: 0
        },
        spokes: {
          strokeWidth: 0
        },
      }
    },
    theme: {
      monochrome: {
        enabled: true,
        shadeTo: 'light',
        shadeIntensity: 0.6
      }
    }
    };
    var chart = new ApexCharts(document.querySelector('#pregunta8'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});


$.ajax({
  url: '/consulta_respuestas/' + 9 + '/',
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: totales,
      labels: respuestas,
      chart: {
        type: 'polarArea',
      },
      stroke: {
        colors: ['#fff']
      },
      fill: {
        opacity: 0.8
      },
      legend: {
        position: 'bottom' // Esto coloca el legend en la parte inferior
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          },
          legend: {
            position: 'bottom'
          }
        }
      }]
    };
    var chart = new ApexCharts(document.querySelector('#pregunta9'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});


$.ajax({
  url: '/consulta_respuestas/' + 10 + '/', 
  dataType: 'json',
  success: function (data) {
    // console.log(data)

    const respuestas = [];
    const totales = [];

    for (let i = 0; i < data.length; i++) {
      respuestas.push(data[i].respuesta);
      totales.push(data[i].total);
    }
    // console.log( respuestas);
    // console.log( totales);

    var options = {
      series: totales,
      chart: {
        type: 'donut',
      },
      plotOptions: {
        pie: {
          startAngle: -90,
          endAngle: 90,
          offsetY: 0
        }
      },
      labels: respuestas,
      legend: {
        position: 'bottom' 
      },
      grid: {
        padding: {
          bottom: -80
        }
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          },
          legend: {
            position: 'bottom'
          }
        }
      }]
    };
    var chart = new ApexCharts(document.querySelector('#pregunta10'), options);
    chart.render();
  },
  error: function (error) {
    console.log(error);
  }
});



























'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
});



function floatchart() {
  // (function () {
  //   var options = {
  //     chart: {
  //       type: 'line',
  //       height: 90,
  //       sparkline: {
  //         enabled: true
  //       }
  //     },
  //     dataLabels: {
  //       enabled: false
  //     },
  //     colors: ['#FFF'],
  //     stroke: {
  //       curve: 'smooth',
  //       width: 3
  //     },
  //     series: [
  //       {
  //         name: 'series1',
  //         data: [45, 66, 41, 89, 25, 44, 9, 54]
  //       }
  //     ],
  //     yaxis: {
  //       min: 5,
  //       max: 95
  //     },
  //     tooltip: {
  //       theme: 'dark',
  //       fixed: {
  //         enabled: false
  //       },
  //       x: {
  //         show: false
  //       },
  //       y: {
  //         title: {
  //           formatter: function (seriesName) {
  //             return 'Total Earning';
  //           }
  //         }
  //       },
  //       marker: {
  //         show: false
  //       }
  //     }
  //   };
  //   var chart = new ApexCharts(document.querySelector('#tab-chart-1'), options);
  //   chart.render();
  // })();




  // (function () {
  //   var options = {
  //     chart: {
  //       type: 'line',
  //       height: 90,
  //       sparkline: {
  //         enabled: true
  //       }
  //     },
  //     dataLabels: {
  //       enabled: false
  //     },
  //     colors: ['#FFF'],
  //     stroke: {
  //       curve: 'smooth',
  //       width: 3
  //     },
  //     series: [
  //       {
  //         name: 'series1',
  //         data: [35, 44, 9, 54, 45, 66, 41, 69]
  //       }
  //     ],
  //     yaxis: {
  //       min: 5,
  //       max: 95
  //     },
  //     tooltip: {
  //       theme: 'dark',
  //       fixed: {
  //         enabled: false
  //       },
  //       x: {
  //         show: false
  //       },
  //       y: {
  //         title: {
  //           formatter: function (seriesName) {
  //             return 'Total Earning';
  //           }
  //         }
  //       },
  //       marker: {
  //         show: false
  //       }
  //     }
  //   };
  //   var chart = new ApexCharts(document.querySelector('#tab-chart-2'), options);
  //   chart.render();
  // })();


  // (function () {
  //   var options = {
  //     chart: {
  //       type: 'bar',
  //       height: 480,
  //       stacked: true,
  //       toolbar: {
  //         show: false
  //       }
  //     },
  //     plotOptions: {
  //       bar: {
  //         horizontal: false,
  //         columnWidth: '50%'
  //       }
  //     },
  //     dataLabels: {
  //       enabled: false
  //     },
  //     colors: ['#d3eafd', '#2196f3', '#673ab7', '#e1d8f1'],
  //     series: [
  //       {
  //         name: 'Investment',
  //         data: [35, 125, 35, 35, 35, 80, 35, 20, 35, 45, 15, 75]
  //       },
  //       {
  //         name: 'Loss',
  //         data: [35, 15, 15, 35, 65, 40, 80, 25, 15, 85, 25, 75]
  //       },
  //       {
  //         name: 'Profit',
  //         data: [35, 145, 35, 35, 20, 105, 100, 10, 65, 45, 30, 10]
  //       },
  //       {
  //         name: 'Maintenance',
  //         data: [0, 0, 75, 0, 0, 115, 0, 0, 0, 0, 150, 0]
  //       }
  //     ],
  //     responsive: [
  //       {
  //         breakpoint: 480,
  //         options: {
  //           legend: {
  //             position: 'bottom',
  //             offsetX: -10,
  //             offsetY: 0
  //           }
  //         }
  //       }
  //     ],
  //     xaxis: {
  //       type: 'category',
  //       categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  //     },
  //     grid: {
  //       strokeDashArray: 4
  //     },
  //     tooltip: {
  //       theme: 'dark'
  //     }
  //   };
  //   var chart = new ApexCharts(document.querySelector('#growthchart'), options);
  //   chart.render();
  // })();


  // (function () {
  //   var options = {
  //     chart: {
  //       type: 'area',
  //       height: 95,
  //       stacked: true,
  //       sparkline: {
  //         enabled: true
  //       }
  //     },
  //     colors: ['#673ab7'],
  //     stroke: {
  //       curve: 'smooth',
  //       width: 1
  //     },
  //     series: [
  //       {
  //         data: [0, 15, 10, 50, 30, 40, 25]
  //       }
  //     ]
  //   };
  //   var chart = new ApexCharts(document.querySelector('#bajajchart'), options);
  //   chart.render();
  // })();

}
