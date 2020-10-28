<!DOCTYPE html>
<html>
<head>
    <title>Leaflet Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css" />
    <link rel="stylesheet" href="css/style.css"/>
    <style>
.info {
    z-index: 1000;
    position: absolute;
    right: 40%;
    top: 5%;
    padding: 6px 8px;
    font: 14px Arial, Helvetica, sans-serif;
    text-align: center;
    background: white;
    background: rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
}

.info h1 {
    font-size: 16px;
    margin: 0 0 5px;
    color: #777777;
}


.legend {
    line-height: 18px;
    color: #333333;
    font-family: 'Open Sans', Helvetica, sans-serif;
    padding: 6px 8px;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
}

.legend i {
    width: 28px;
    height: 18px;
    float: left;
    margin-right: 8px;
    opacity: 0.7;
}


.legend p {
    font-size: 12px;
    line-height: 18px;
    margin: 0;
}
        
    </style>
</head>
<body>
    
    <div id="map"></div>
    
    <div class='info'><h1>Blood lead level in Philadelphia</h1><div class='update'>Hover over a census tract</div></div>

    <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>
        // Create Map Object
        var map = L.map('map',{ center: [40.003926, -75.135201], zoom: 11 });
        L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/base/{z}/{x}/{y}.png', {
            attribution: 'Tiles by <a href="http://mapc.org">MAPC</a>, Data by <a href="https://www.phila.gov/programs/lead-and-healthy-homes-program/">Philadelphai Open Data</a>',
            maxZoom: 17,
            minZoom: 9
        }).addTo(map);


        
        // Set style function that sets fill color property equal to blood lead
        function styleFunc(feature) {
    return {
        fillColor: setColorFunc(feature.properties.num_bll_5p),
        fillOpacity: 0.9,
        weight: 1,
        opacity: 1,
        color: '#fefbd8',
        dashArray: '3'
    };
}
function setColorFunc(density){
    return density > 15 ? '#800000' :
           density > 10 ? '#A0522D' :
           density > 5 ? '#DAA520' :
           density > 0 ? '#FFF8DC' :
                         '#BFBCBB';
};

// Add census tract of blood lead in Philadelphia GeoJSON Data
        var neighborhoodsLayer = null;
$.getJSON("C:/Users/willi/blood_lead.geojson",function(C:\Users\willi){
    neighborhoodsLayer = L.geoJson(C:\Users\willi, {
        style: styleFunc,
        onEachFeature: function(feature, layer){
            layer.bindPopup('Blood lead level: '+feature.properties.num_bll_5p);
        }
    }).addTo(map);
});

        // Set style function that sets fill color property equal to blood lead
        function styleFunc(feature) {
            return {
                fillColor: setColorFunc(feature.properties.num_bll_5p),
                fillOpacity: 0.9,
                weight: 1,
                opacity: 1,
                color: '#ffffff',
                dashArray: '3'
            };
        }

        // Set function for color ramp
        function setColorFunc(density){
            return density > 15 ? '#800000' :
                   density > 10 ? '#A0522D' :
                   density > 5 ? '#DAA520' :
                   density > 0 ? '#FFF8DC' :
                                 '#BFBCBB';
        };

        // Now we’ll use the onEachFeature option to add the listeners on our state layers:
        function onEachFeature(feature, layer){
            layer.on({
                mouseover: highlightFeature,
                mouseout: resetHighlight,
                click: zoomFeature
            });
            layer.bindPopup('Blood lead level: '+feature.properties.num_bll_5p);
        }
        
        // Now let’s make the states highlighted visually in some way when they are hovered with a mouse. First we’ll define an event listener for layer mouseover event:
        function highlightFeature(e){
            var layer = e.target;

            layer.setStyle({
                weight: 5,
                color: '#666',
                dashArray: '',
                fillOpacity: 0.7
            });
            // for different web browsers
            if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
                layer.bringToFront();
            }
        }
        
        
        // Define what happens on mouseout:
        function resetHighlight(e) {
            neighborhoodsLayer.resetStyle(e.target);
        }
        
        // As an additional touch, let’s define a click listener that zooms to the state: 
        function zoomFeature(e){
            console.log(e.target.getBounds());
            map.fitBounds(e.target.getBounds().pad(1.5));
        }
        
        // Create Leaflet Control Object for Legend
        var legend = L.control({position: 'bottomright'});
        
        // Function that runs when legend is added to map
        legend.onAdd = function (map) {
            // Create Div Element and Populate it with HTML
            var div = L.DomUtil.create('div', 'legend');            
            div.innerHTML += '<b>Blood lead level</b><br />';
            div.innerHTML += 'by census tract<br />';
            div.innerHTML += '<br>';
            div.innerHTML += '<i style="background: #800000"></i><p>15+</p>';
            div.innerHTML += '<i style="background: #A0522D"></i><p>10-15</p>';
            div.innerHTML += '<i style="background: #DAA520"></i><p>5-10</p>';
            div.innerHTML += '<i style="background: #DEB887"></i><p>0-5</p>';
            div.innerHTML += '<hr>';
            div.innerHTML += '<i style="background: #BFBCBB"></i><p>No Data</p>';
            
            // Return the Legend div containing the HTML content
            return div;
        };
        
        // Add Legend to Map
        legend.addTo(map);

        // Add Scale Bar to Map
        L.control.scale({position: 'bottomleft'}).addTo(map);


    </script>

</body>
</html>