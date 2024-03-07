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

// Function to create a pie chart

// foR THIS, I GOT HELP FROM A GITHUB PIECHART PROJECT ON FLOWERS, THEY HAD VERY NICE
// PIE-CHARTS, THESE ARE LITTLE  BIT WEIIRD:((()))
function createPieChart(containerId, data) {
    var width = 360;
    var height = 360;
    var radius = Math.min(width, height) / 2;
    var labelRadius = radius * 1.3;

    var color = d3.scaleOrdinal(d3.schemeCategory10);

    var arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);
    
    // For labeling the piecharts outside the chart:
    var outerArc = d3.arc()
        .innerRadius(labelRadius)
        .outerRadius(labelRadius);

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

    //This is for drawing lines from picharts to the labels:
    g.append("polyline")
        .attr("stroke", "black")
        .style("fill", "none")
        .attr("stroke-width", 1)
        .attr("points", function(d) {
            var posA = arc.centroid(d) // line start
            var posB = outerArc.centroid(d) // line end
            var posC = outerArc.centroid(d); // slightly changes to make line orthogonal
            posC[0] = labelRadius * 0.95 * (midAngle(d) < Math.PI ? 1 : -1);
            return [posA, posB, posC];
        });

   // Moving the label positioning to the outer arc
    g.append("text")
        .attr("transform", function(d) {
            var pos = outerArc.centroid(d);
            pos[0] = labelRadius * (midAngle(d) < Math.PI ? 1 : -1);
            return "translate("+ pos +")";
        })
        .style("text-anchor", function(d) {
            return midAngle(d) < Math.PI ? "start" : "end";
        })
        .text(function(d) { return d.data.category; });

    // Function to calculate the mid angle of the slice
    function midAngle(d) {
        return d.startAngle + (d.endAngle - d.startAngle) / 2;
    }
}


// Call the function to create pie charts
createPieChart("#flower1", demographicsData);
createPieChart("#flower2", votingResultsData);
