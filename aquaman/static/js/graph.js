$(function () {

    var url = window.location.pathname.split( '/' )
    var sensor = url[1];
    var name = '';
    var unit = '';

    switch (sensor) {
        case 'st':
            name = "Sump Tank";
            unit = "Temperature °C"
            break;
        case 'ft':
            name = "Fish Tank";
            unit = "Temperature °C"
            break;
        case 'at':
            name = "Air Temperature";
            unit = "Temperature °C"
            break;
        case 'ap':
            name = "Air Pressure";
            unit = "Pascals"
            break;
        case 'ls':
            name = "Light sensor";
            unit = "Lux"
            break;
    }

    $.getJSON("/graph_data/"+sensor, function(data) {
        var graph_data = JSON.parse(data);

        var data = graph_data.map(function(item){
            return [Date.parse(item['sub_date']), item['data']]
        });

        $('#graph').highcharts('StockChart',{
            
            title: {
                text: name
            },
        
            xAxis: {
                title: {
                    text: 'Time'
                },
                type: 'datetime'
            },
            
            yAxis: {
                title: {
                    text: unit
                }
            },
            rangeSelector : {
                buttons : [{
                    type : 'hour',
                    count : 1,
                    text : '1h'
                }, {
                    type : 'day',
                    count : 1,
                    text : '1D'
                }, {
                    type : 'all',
                    count : 1,
                    text : 'All'
                }],
                selected : 1,
                inputEnabled : false
            },
        
            tooltip: {
                crosshairs: true,
                shared: true,
            },
            
            legend: {
                enabled: true
            },
        
            series: [{
                name: unit,
                data: data
            }]
        
        });
    });
    
});