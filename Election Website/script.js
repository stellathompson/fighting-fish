document.addEventListener('DOMContentLoaded', function () {

    // Function to fetch data from the API
    async function fetchData() {
        state = document.getElementById("state_input").value;
        try{
            const response = await fetch('/api/pie_data/${state}');
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching data:', error)
            return null;
        }
    }

    // Update the pie chart based on the selected year and state
    async function updateChart() {
        currentYear = document.getElementById('yearSelector').value;
        const selectedState = "AZ";

        // Fetch data from the API for the selected state
        const data = await fetchData(selectedState);

        if (data) {
            // Update the chart with the new data
            drawPieChart(data);
        }
    }

    // Function to draw the pie chart
    function drawPieChart(data) {

        // Use D3.js to create a pie chart
        const width = 400;
        const height = 400;
        const radius = Math.min(width, height) / 2;

        const svg = d3.select('#pie-chart-container')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .append('g')
            .attr('transform', `translate(${width / 2},${height / 2})`);

        const pie = d3.pie().value(d => d.value);
        const path = d3.arc().outerRadius(radius).innerRadius(0);

        const color = d3.scaleOrdinal(d3.schemeCategory10)

        const arcs = svg.selectAll('arc')
            .data(pie(data))
            .enter()
            .append('g');

        arcs.append('path')
            .attr('d', path)
            .attr('fill', (d, i) => color(i)); 
    }
});