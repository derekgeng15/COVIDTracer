var csv = require('./jquery.csv.js');
var accounts;
function readAccountsCSV(){
    accounts = $.csv.toObjects('./csvs/accounts');
}

function initMap() {
    const myLatLng = { lat: 40.47607247512519, lng: -74.67328796340085 };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: myLatLng,
        styles: [
            { elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
            { elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
            {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }],
            },
            {
                featureType: 'poi',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }],
            },
            {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{ color: '#263c3f' }],
            },
            {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#6b9a76' }],
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{ color: '#38414e' }],
            },
            {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#212a37' }],
            },
            {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#9ca5b3' }],
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{ color: '#746855' }],
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{ color: '#1f2835' }],
            },
            {
                featureType: 'road.highway',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#f3d19c' }],
            },
            {
                featureType: 'transit',
                elementType: 'geometry',
                stylers: [{ color: '#2f3948' }],
            },
            {
                featureType: 'transit.station',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#d59563' }],
            },
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{ color: '#17263c' }],
            },
            {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{ color: '#515c6d' }],
            },
            {
                featureType: 'water',
                elementType: 'labels.text.stroke',
                stylers: [{ color: '#17263c' }],
            }
        ]
    });
    for(i = 0; i < 4; i++)
        new google.maps.Marker({
            position: {lat : 40.47607247512519 + i * 0.001, lng : -74.67328796340085 + i * 0.001},
            map,
            title: 'Derek',
        });
    // new google.maps.Marker({
    //     position: { lat: 40.48337871907082, lng: -74.59945033152542 },
    //     map,
    //     title: 'Pradyun',
    // });
    const line = new google.maps.Polyline({
        path: [{ lat: 40.47607247512519, lng: -74.67328796340085 }, { lat: 40.48337871907082, lng: -74.59945033152542 }],
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2,
        title: 'line'
    });
    line.setMap(map)
}

readAccountsCSV()
initMap()