// color_dictionary = [ 

//     "#F0D5E3",
//     "#7571A1",
//     "#FFE46B",
//     "#48515C",
//     "#FFC697",
//     "#80B5A1",
//     "#BDFFE1",
//     "#98C2D9",
//     "#F5B23E",
//     "#6A8AC0",
//     "#959EA8",
//     "#E89BC6",
//     "#C5BDEF",
//     "#FFA275"
//     ]

// document.addEventListener('DOMContentLoaded', function() {

//     bgcolor = color_dictionary.slice(0,values.length)
//     var ctx1 = document.getElementById("pieChart").getContext('3d');
//     var pieChart = new Chart(ctx1, {
//       type: 'pie',
//       data: {
//         labels: labels,
//         datasets: [{
//           backgroundColor: bgcolor,
//           data: values
//         }]
//       }
//     });

//     var ctx2 = document.getElementById("barChart").getContext('3d');
//     var options = {
//         scales: {
//             xAxes: [{
//                 display: true,
//                 gridLines: {
//                     offsetGridLines: false
//                 }
//             }],
//             yAxes: [{
//                 display: true,
//                 ticks: {
//                   min: 0
//                 },
//                 gridLines: {
//                     offsetGridLines: false
//                 }
//             }]
//         }
//     }
//     var barChart = new Chart(ctx2, {
//       type: 'bar',
//       data: {
//         labels: labels,
//         datasets: [{
//           label: 'emotion summary',
//           backgroundColor: bgcolor,
//           data: values
//         }]
//       },
//       options: options

//     });




// })


const ctx = document.getElementById('myChart');
const ctx = document.getElementById('myChart').getContext('2d');
const ctx = $('#myChart');
const ctx = 'myChart';