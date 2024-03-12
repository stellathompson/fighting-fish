/*
 * script.js
 * Authors: Kritika Pandit, Stella Thompson, Daniel Lumbu, Yeseo Jeon, Luha Yang
 * This is javascript controls the piecharts by taking the information from the data set
 * and feeding it into the function. Two piecharts, one for the demographics of the county 
 * based on the race and the other for the voting results for 2 candidates, Trump and Clinton
 * is drawn.
 */

var votingResultsColors = ['#856088', '#78184A']; 
var demographicsColors = ['#D8BFD8', '#5a3749', '#6d296d', '#7260a9', '#B768A2', '#86608E']; 


// Pie chart for the Voting Results in 2016 elections
var votingResultsData = [
    { category: 'Trump ' + votesdiv[0] + '%', value: votesdiv[0] },
    { category: 'Clinton ' + votesdiv[1] + '%', value: votesdiv[1] }
];


// Pie chart for the Demographics data from the elections
var demographicsData = [
    { category: 'hispanic', value: dermo[0]},
    { category: 'white', value: dermo[1]},
    { category: 'black', value: dermo[2]},
    { category: 'native', value: dermo[3]},
    { category: 'asian', value: dermo[4]},
    { category: 'pacific', value: dermo[5]}
];



// This function that creates the piechart according to the given data
function createPieChart(containerId, data, customColors) {
    var width = 300;
    var height = 300;
    var radius = Math.min(width, height) / 2;


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
         // Add text and lines outside the pie chart
    var text = svg.selectAll(".text")
    .data(data)
    .enter().append("text")
    .attr("transform", function(d) {
        var pos = arc.centroid(d);
        pos[0] = radius * (midAngle(d) < Math.PI ? 1.2 : -1.2); // Adjust position based on angle
        return "translate(" + pos + ")";
    })
    .attr("dy", ".35em")
    .style("text-anchor", function(d) {
        return (midAngle(d) < Math.PI ? "start" : "end"); // Align text based on angle
    })
    .text(function(d) { return d.data.category; });

// Add lines connecting text to pie slices
var lines = svg.selectAll(".line")
    .data(data)
    .enter().append("line")
    .attr("x1", function(d) { return arc.centroid(d)[0]; })
    .attr("y1", function(d) { return arc.centroid(d)[1]; })
    .attr("x2", function(d) {
        var pos = arc.centroid(d);
        pos[0] = radius * (midAngle(d) < Math.PI ? 1.05 : -1.05); // Adjust position based on angle
        return pos[0];
    })
    .attr("y2", function(d) {
        var pos = arc.centroid(d);
        pos[1] = radius * (midAngle(d) < Math.PI ? 1.05 : -1.05); // Adjust position based on angle
        return pos[1];
    })
    .attr("stroke", "black")
    .attr("stroke-width", 1);
}

// Calling the function to create pie charts
createPieChart("#flower1", demographicsData, demographicsColors);
createPieChart("#flower2", votingResultsData, votingResultsColors);
