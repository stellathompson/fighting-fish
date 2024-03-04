// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from Flask API endpoint
    const state = 'AZ';
    fetch('/api/pie_data/${state}')
        .then(response => response.json())
        .then(data => {
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

            const arcs = svg.selectAll('arc')
                .data(pie(data))
                .enter()
                .append('g');

            arcs.append('path')
                .attr('d', path)
                .attr('fill', (d, i) => d3.schemeCategory10[i]); // Color scheme

            // Add labels if needed
            // arcs.append('text')
            //     .attr('transform', d => `translate(${path.centroid(d)})`)
            //     .attr('dy', '0.35em')
            //     .text(d => d.data.label);
        })
        .catch(error => console.error('Error fetching data:', error));
});