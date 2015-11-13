/**
 * Created by gatluri on 11/12/2015.
 */
google.setOnLoadCallback(drawChart);
function drawChart() {

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Mentions', 80]

    ]);

    var options = {
        width: 4000, height: 500,
        redFrom: 90, redTo: 100,
        yellowFrom:75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

    chart.draw(data, options);

    setInterval(function() {
        data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
        chart.draw(data, options);
    }, 13000);
    setInterval(function() {
        data.setValue(1, 1, 40 + Math.round(60 * Math.random()));
        chart.draw(data, options);
    }, 5000);
    setInterval(function() {
        data.setValue(2, 1, 60 + Math.round(20 * Math.random()));
        chart.draw(data, options);
    }, 26000);
}