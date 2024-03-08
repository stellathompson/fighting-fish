function fetchTopStates() {
    const year = document.getElementById('year').value;

    fetch('/api/top_states/${year}')
        .then(response => response.json())
        .then(data => {
            // Call functions to render charts and demographic data
            renderTopStatesCharts(data.election_data);
            renderDemographicData(data.demographic_data);
        })
        .catch(error => console.error('Error fetching data:', error));
}

function renderTopStatesCharts(electionData) {
    // Assuming 'topStatesCharts' is the div where the charts will be rendered
    const chartContainer = d3.select('#topStatesCharts');

    // Clear previous content
    chartContainer.html('');

    // Example: Bar chart using D3
    const barChartContainer = chartContainer.append('div')
        .attr('id', 'barChartContainer');

    const barChart = d3.select('#barChartContainer')
        .selectAll('div')
        .data(electionData)
        .enter()
        .append('div')
        .style('width', d => `${d.vote_percentile * 5}px`) // Adjust width based on data
        .text(d => `${d.state_name}: ${d.vote_percentile}%`);

    // You can customize the bar chart further based on your needs

    // Other D3 chart implementations go here...
}

function renderDemographicData(demographicData) {
    // Assuming 'demographicData' is the div where demographic data will be rendered
    const demographicContainer = d3.select('#demographicData');

    // Clear previous content
    demographicContainer.html('');

    // Example: Render demographic data using D3
    demographicContainer.append('p').text('Demographic Data:');

    // Implement logic to render demographic data using D3
    // ...

    // You can customize the demographic data rendering further based on your needs

    // Other D3 demographic data implementations go here...
}
