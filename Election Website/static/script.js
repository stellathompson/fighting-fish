/*
 * script.js
 * Authors: Kritika Pandit, Stella Thompson, Daniel Lumbu, Yeseo Jeon, Luha Yang
 * This is javascript controls the piecharts by taking the information from the data set
 * and feeding it into the function. Two piecharts, one for the demographics of the county 
 * based on the race and the other for the voting results for 2 candidates, Trump and Clinton
 * is drawn.
 */


//Pie chart for the Demographics data from the elections
var demographicsData = [
    { category: 'hispanic', value: dermo[0]},
    { category: 'white', value: dermo[1]},
    { category: 'black', value: dermo[2]},
    { category: 'native', value: dermo[3]},
    { category: 'asian', value: dermo[4]},
    { category: 'pasific', value: dermo[5]}
];


// Pie chart for the Voting Results in 2016 elections
var votingResultsData = [
    { category: 'Trump ' + votesdiv[0] + '%' , value: votesdiv[0] },
    { category: 'Clinton ' + votesdiv[1] + '%', value: votesdiv[1] }

];


// This function that creates the piechart according to the given data
function createPieChart(containerId, data) {
    var width = 300;
    var height = 300;
    var radius = Math.min(width, height) / 2;

    
    var customColors = ['#563C5C', '#9F2B68', '#FAE6FA', '#BDB5D5', '#B768A2', '#86608E', '#78184A', '#702963', '#856088', '#D8BFD8'];

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

// Calling the function to create pie charts
createPieChart("#flower1", demographicsData);
createPieChart("#flower2", votingResultsData);
