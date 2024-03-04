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

        // Filter data based on the selected year
        const filteredData = data.map(entry => ({
            county: entry.county,
            value: +entry['trump${currentYear}']
        }))

        // Use D3.js to create a pie chart
        const width = 400;
        const height = 400;
        const radius = Math.min(width, height) / 2;

        const color = d3.scaleOrdinal(d3.schemeCategory10)

        const arc = d3.arc()
            .outerRadius(radius - 10)
            .innerRadius(0);

        const pie = d3.pie()
            .sort(null)
            .value(d => d.value)

        // Remove previous chart if it exists
        d3. select('#pieChart').selectAll('*').remove();

        // Append new SVG for the chart
        const svg = d3.select('#pieChart')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .append('g')
            .attr('transform', `translate(${width / 2},${height / 2})`);

        // Generate pie chart slices
        const g = svg.selectAll('.arc')
            .data(pie(filteredData))
            .enter().append('g')
            .attr('class', 'arc');

        // Draw slices
        g.append('path')
            .attr('d', arc)
            .style('fill', d => color(d.data.county));

        // Add labels
        g.append('text')
            .attr('transform', d => 'translate(${arc.centroid(d)})')
            .attr('dy', '.35m')
            .text(d => d.data.county); 
    }
});
