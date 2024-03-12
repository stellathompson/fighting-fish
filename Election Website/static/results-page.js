/*
 * script.js
 * Authors: Kritika Pandit, Stella Thompson, Daniel Lumbu, Yeseo Jeon, Luha Yang
 * This is javascript controls the piecharts by taking the information from the data set
 * and feeding it into the function. Two piecharts, one for the demographics of the county 
 * based on the race and the other for the voting results for 2 candidates, Trump and Clinton
 * is drawn.
 */

var votingResultsColors = ['#CD5C5C', '#3333cc']; 
var demographicsColors = ['#7F00FF', '#ffcccc', '#6d296d', '#7260a9', '#B768A2', '#483248']; 

// Pie chart for the Voting Results in 2016 elections
var votingResultsData = [
    { category: 'Trump ' + votesdiv[0] + '%', value: votesdiv[0] },
    { category: 'Clinton ' + votesdiv[1] + '%', value: votesdiv[1] }
];

// Pie chart for the Demographics data from the elections
var demographicsData = [
    { category: 'hispanic', value: demo[0]},
    { category: 'white', value: demo[1]},
    { category: 'black', value: demo[2]},
    { category: 'native', value: demo[3]},
    { category: 'asian', value: demo[4]},
    { category: 'pacific', value: demo[5]}
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

}

// Calling the function to create pie charts
createPieChart("#flower1", demographicsData, demographicsColors);
createPieChart("#flower2", votingResultsData, votingResultsColors);
