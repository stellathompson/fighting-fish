/*
 * script.js
 * Kritika Pandit
 */

//Flower and Petals refer to the piechartt, each piechart is a flower with different colors(petals)

// Need to replace this with a py that has SQL queries that takes the data and
//makes a piechart accordingly

// I have made 2 piecharts as we wanted and we need a connection with the data 
// and figure out how to adjest it:


// this can be added in javascript or in a python file. it is same either way:

// For the demographics:
// hispanic, white, black, native, asian, pacific
// REFER TO PIECHARTS.PY TO SEE SOME HINTS.
// trump16, clinton16, trump20, biden20
var demographicsData = [
    { category: 'hispanic', value: dermo[0] },
    { category: 'white', value: dermo[1]},
    { category: 'black', value: dermo[2]},
    { category: 'native', value: dermo[3]},
    { category: 'asian', value: dermo[4]},
    { category: 'pasific', value: dermo[5]}
];


// foR THE VOTING RESULTS:
//trump16, clinton16, trump20, biden20
// nEED TO BE CAREFUL ON WHICH YEAR? 16 OR 2, NEED TO ADJUST THE SQL ACCORDINLGY

var votingResultsData = [
    { category: 'Trump ' + votesdiv[0] + '%' , value: votesdiv[0] },
    { category: 'Clinton ' + votesdiv[1] + '%', value: votesdiv[1] }

];

function createPieChart(containerId, data) {
    var width = 300;
    var height = 300;
    var radius = Math.min(width, height) / 2;


    var customColors = ['#0000FF', '#89CFF0', '#0096FF', '#6495ED', '#6F8FAF', '#191970', '#B6D0E2', '#4682B4', '#0818A8', '#008080'];

    var color = d3.scaleOrdinal()
        .domain(data.map(function(d) { return d.category; }))
        .range(customColors);


    var arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

    var pie = d3.pie()
        .sort(null)
        .value(function(d) { return d.value; });

    var svg = d3.select(containerId)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc");

    g.append("path")
        .attr("d", arc)
        .style("fill", function(d) { return color(d.data.category); });

    g.append("text")
        .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .text (function(d) { return d.data.category; });
}

// Call the function to create pie charts
createPieChart("#flower1", demographicsData);
createPieChart("#flower2", votingResultsData);
